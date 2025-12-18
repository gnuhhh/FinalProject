# prediction/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Count, Avg, Max, Min, Sum
from django.contrib.auth.decorators import login_required
import numpy as np
from .models import Region, University, Major, AdmissionCriteria
import os
import json
from django.conf import settings
import pandas as pd

# Import module ML mới
from .ml import predict_quota_and_score_ml

@login_required(login_url='login')
def prediction_home(request):
    """Trang chủ dự đoán chỉ tiêu"""
    regions = Region.objects.all()
    
    universities = University.objects.none()
    region_id = request.GET.get('region_id')
    if region_id:
        universities = University.objects.filter(region_id=region_id)
    
    context = {
        'regions': regions,
        'universities': universities,
    }
    
    return render(request, 'prediction/prediction_home.html', context)

def get_universities(request):
    """API lấy danh sách trường theo khu vực + tìm kiếm"""
    region_id = request.GET.get('region_id')
    search_query = request.GET.get('search', '')
    
    universities = University.objects.filter(region_id=region_id)
    
    if search_query:
        universities = universities.filter(
            Q(name__icontains=search_query) | Q(code__icontains=search_query)
        )
    
    data = [{
        'id': uni.id, 
        'name': uni.name,
        'code': uni.code
    } for uni in universities]
    
    return JsonResponse(data, safe=False)

def get_majors_with_blocks(request):
    """API lấy danh sách ngành theo trường + các khối có sẵn"""
    university_id = request.GET.get('university_id')
    
    majors = Major.objects.filter(university_id=university_id)
    
    data = []
    for major in majors:
        criteria = AdmissionCriteria.objects.filter(major=major)
        
        all_blocks = set()
        for criterion in criteria:
            blocks = [block.strip() for block in criterion.combination.split(',')]
            all_blocks.update(blocks)
        
        if all_blocks:
            data.append({
                'id': major.id,
                'name': major.name,
                'code': major.code,
                'blocks': list(all_blocks)
            })
    
    return JsonResponse(data, safe=False)

@login_required(login_url='login')
def prediction_result(request):
    """Hiển thị kết quả dự đoán sử dụng logic ML mới"""
    if request.method == 'GET':
        major_id = request.GET.get('major_id')
        block = request.GET.get('block')
        
        if not major_id or not block:
            return render(request, 'prediction/error.html', {
                'error': 'Thiếu thông tin major_id hoặc block'
            })
        
        major = get_object_or_404(Major, id=major_id)
        
        # Lấy dữ liệu theo khối được chọn - lấy tất cả dữ liệu có sẵn
        criteria = AdmissionCriteria.objects.filter(
            major=major
        ).filter(
            Q(combination__icontains=block) | 
            Q(combination__icontains=block.upper()) |
            Q(combination__icontains=block.lower())
        ).order_by('year')  # Sắp xếp tăng dần theo năm
        
        print(f"📊 Đã tìm thấy {len(criteria)} bản ghi cho major {major_id}, khối {block}")
        
        # DEBUG: In ra dữ liệu thực tế
        for c in criteria:
            print(f"  - Năm {c.year}: chỉ tiêu={c.quota}, điểm={c.benchmark_score}")
        
        # Sử dụng logic ML mới để dự đoán
        prediction_data = calculate_ml_prediction(criteria, block, major)
        
        context = {
            'major': major,
            'block': block,
            'criteria': criteria,
            'prediction': prediction_data
        }
        
        return render(request, 'prediction/prediction_result.html', context)

def calculate_ml_prediction(criteria, selected_block, major):
    """Sử dụng logic ML mới để dự đoán"""
    print(f"🔍 Bắt đầu dự đoán ML với {len(criteria)} bản ghi, khối {selected_block}")
    
    if len(criteria) == 0:
        return create_fallback_prediction(selected_block, "Không có dữ liệu lịch sử")
    
    try:
        # Sắp xếp dữ liệu theo năm tăng dần (yêu cầu của ML model)
        criteria_sorted = sorted(criteria, key=lambda x: x.year)
        
        # Gọi hàm ML mới
        ml_result = predict_quota_and_score_ml(criteria_sorted, 2025)
        
        # Đảm bảo kết quả có đầy đủ thông tin cần thiết
        result = {
            'predicted_quota': ml_result['predicted_quota'],
            'predicted_score': ml_result['predicted_score'],
            'quota_trend': ml_result['quota_trend'],
            'score_trend': ml_result['score_trend'],
            'confidence': ml_result['confidence'],
            'message': generate_ml_message(criteria_sorted, ml_result['confidence']),
            'algorithm': ml_result['algorithm'],
            'historical_data': [
                {
                    'year': c.year,
                    'quota': c.quota,
                    'score': c.benchmark_score,
                    'combination': c.combination
                } for c in criteria_sorted
            ]
        }
        
        # Thêm thông tin model details nếu có
        if 'models' in ml_result:
            result['model_details'] = ml_result['models']
        if 'notes' in ml_result:
            result['notes'] = ml_result['notes']
        
        print(f"🎯 Kết quả dự đoán ML: {result}")
        return result
        
    except Exception as e:
        print(f"❌ Lỗi trong calculate_ml_prediction: {e}")
        import traceback
        traceback.print_exc()
        return create_fallback_prediction(selected_block, f"Lỗi xử lý ML: {str(e)}")

def generate_ml_message(criteria, confidence):
    """Tạo thông báo cho kết quả ML"""
    n_years = len(criteria)
    if n_years == 0:
        return "Không có dữ liệu lịch sử"
    
    years = [c.year for c in criteria]
    year_range = f"{min(years)}-{max(years)}"
    
    messages = {
        'high': f"Dự đoán độ tin cậy cao từ {n_years} năm dữ liệu ({year_range}) sử dụng Ensemble ML",
        'medium': f"Dự đoán từ {n_years} năm dữ liệu ({year_range}) sử dụng Machine Learning",
        'low': f"Dự đoán tham khảo từ {n_years} năm dữ liệu ({year_range})"
    }
    
    return messages.get(confidence, f"Dự đoán từ {n_years} năm dữ liệu")

def create_fallback_prediction(block, message):
    """Tạo dự đoán fallback khi ML thất bại"""
    return {
        'predicted_quota': 0,
        'predicted_score': 0,
        'quota_trend': 'unknown',
        'score_trend': 'unknown',
        'confidence': 'none',
        'message': message,
        'algorithm': 'fallback',
        'historical_data': []
    }

@login_required(login_url='login')
def statistics_dashboard(request):
    """Trang thống kê tổng quan tuyển sinh"""
    
    try:
        # Đọc từ database thay vì CSV để đảm bảo hoạt động
        total_universities = University.objects.count()
        total_majors = Major.objects.count()
        total_criteria = AdmissionCriteria.objects.count()
        
        # Thống kê cơ bản
        score_stats = AdmissionCriteria.objects.aggregate(
            avg_score=Avg('benchmark_score'),
            max_score=Max('benchmark_score'),
            min_score=Min('benchmark_score')
        )
        
        # Phân bổ theo vùng miền
        region_stats = []
        regions = Region.objects.all()
        for region in regions:
            uni_count = University.objects.filter(region=region).count()
            region_stats.append({
                'name': region.name,
                'uni_count': uni_count
            })
        
        # Top trường có nhiều ngành nhất
        top_universities = []
        universities = University.objects.annotate(major_count=Count('major'))
        for uni in universities.order_by('-major_count')[:10]:
            top_universities.append({
                'name': uni.name,
                'major_count': uni.major_count
            })
        
        # Top ngành được nhiều trường tuyển sinh
        top_majors = []
        majors = Major.objects.annotate(uni_count=Count('university'))
        for major in majors.order_by('-uni_count')[:10]:
            top_majors.append({
                'name': major.name,
                'uni_count': major.uni_count
            })
        
        # Phân bổ chỉ tiêu theo năm
        yearly_quota = []
        year_data = AdmissionCriteria.objects.values('year').annotate(
            total_quota=Sum('quota'),
            avg_score=Avg('benchmark_score')
        ).order_by('year')
        
        for data in year_data:
            yearly_quota.append({
                'year': data['year'],
                'total_quota': data['total_quota'] or 0,
                'avg_score': round(data['avg_score'] or 0, 2)
            })
        
        # Thống kê nâng cao
        advanced_stats = {'median_score': 0, 'mode_score': 0, 'std_dev': 0}
        
        # Lấy tất cả điểm để tính toán
        all_scores = list(AdmissionCriteria.objects.values_list('benchmark_score', flat=True))
        if all_scores:
            advanced_stats = {
                'median_score': round(np.median(all_scores), 2),
                'mode_score': round(max(set(all_scores), key=all_scores.count), 2) if all_scores else 0,
                'std_dev': round(np.std(all_scores), 2)
            }
        
        context = {
            'total_universities': total_universities,
            'total_majors': total_majors,
            'total_criteria': total_criteria,
            'region_stats': json.dumps(region_stats),
            'region_options': [region.name for region in regions],
            'year_options': sorted(set(data['year'] for data in year_data)),
            'top_universities': top_universities,
            'top_majors': top_majors,
            'score_stats': {
                'avg_score': round(score_stats['avg_score'] or 0, 2),
                'max_score': round(score_stats['max_score'] or 0, 2),
                'min_score': round(score_stats['min_score'] or 0, 2)
            },
            'yearly_quota': json.dumps(yearly_quota),
            'advanced_stats': advanced_stats,
        }
        
        print(f"📊 Thống kê từ database: {total_universities} trường, {total_majors} ngành")
        
        return render(request, 'prediction/statistics_dashboard.html', context)
        
    except Exception as e:
        print(f"❌ Lỗi thống kê: {e}")
        
        context = {
            'total_universities': 0,
            'total_majors': 0,
            'total_criteria': 0,
            'region_stats': json.dumps([]),
            'region_options': ['Miền Bắc', 'Miền Trung', 'Miền Nam'],
            'year_options': [2022, 2023, 2024],
            'top_universities': [],
            'top_majors': [],
            'score_stats': {'avg_score': 0, 'max_score': 0, 'min_score': 0},
            'yearly_quota': json.dumps([]),
            'advanced_stats': {'median_score': 0, 'mode_score': 0, 'std_dev': 0},
            'error': f'Không thể lấy dữ liệu thống kê: {str(e)}'
        }
        return render(request, 'prediction/statistics_dashboard.html', context)

def statistics_api(request):
    """API cho biểu đồ thống kê"""
    chart_type = request.GET.get('chart', 'region')
    
    try:
        if chart_type == 'region':
            # Biểu đồ phân bổ vùng miền
            data = Region.objects.annotate(
                uni_count=Count('university'),
                major_count=Count('university__major')
            ).values('name', 'uni_count', 'major_count')
            
        elif chart_type == 'yearly':
            # Biểu đồ xu hướng qua các năm
            data = AdmissionCriteria.objects.values('year').annotate(
                total_quota=Sum('quota'),
                avg_score=Avg('benchmark_score')
            ).order_by('year')
            
        elif chart_type == 'top_majors':
            # Top ngành hot
            data = Major.objects.values('name').annotate(
                uni_count=Count('university', distinct=True)
            ).order_by('-uni_count')[:10]
        
        return JsonResponse(list(data), safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)