from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Major

def predict_admission(request):
    """Trang chủ dự đoán khả năng đậu"""
    return render(request, 'admission_predictor/predict_admission.html', {
        'title': 'Dự đoán khả năng đậu Đại học'
    })

def predict_admission_result(request):
    """Xử lý và hiển thị kết quả dự đoán"""
    if request.method == 'POST':
        try:
            # Lấy điểm từ form
            block = request.POST.get('block')
            subject_1_score = float(request.POST.get('subject_1_score', 0))
            subject_2_score = float(request.POST.get('subject_2_score', 0))
            subject_3_score = float(request.POST.get('subject_3_score', 0))
            
            total_score = subject_1_score + subject_2_score + subject_3_score
            
            print(f"🎯 Điểm nhập: {total_score} - Khối {block}")
            
            # Lấy các ngành phù hợp
            suitable_majors = Major.objects.filter(
                block=block,
                benchmark_2024__lte=total_score
            ).select_related('university').order_by('benchmark_2024')
            
            # Phân loại kết quả
            high_chance = suitable_majors.filter(benchmark_2024__lte=total_score - 2)
            medium_chance = suitable_majors.filter(
                benchmark_2024__gt=total_score - 2,
                benchmark_2024__lte=total_score - 0.5
            )
            low_chance = suitable_majors.filter(
                benchmark_2024__gt=total_score - 0.5,
                benchmark_2024__lte=total_score
            )
            
            context = {
                'title': 'Kết quả dự đoán',
                'total_score': total_score,
                'block': block,
                'subject_scores': {
                    'subject_1': subject_1_score,
                    'subject_2': subject_2_score, 
                    'subject_3': subject_3_score,
                },
                'high_chance_majors': high_chance,
                'medium_chance_majors': medium_chance,
                'low_chance_majors': low_chance,
                'high_chance_count': high_chance.count(),
                'medium_chance_count': medium_chance.count(),
                'low_chance_count': low_chance.count(),
            }
            
            return render(request, 'admission_predictor/predict_result.html', context)
            
        except Exception as e:
            print(f"❌ Lỗi dự đoán: {e}")
            return render(request, 'admission_predictor/error.html', {
                'message': 'Có lỗi xảy ra khi xử lý dự liệu. Vui lòng thử lại.'
            })
    
    return redirect('admission_predictor:predict_admission')

def api_get_majors(request):
    """API lấy danh sách ngành theo khối và điểm"""
    if request.method == 'GET':
        try:
            block = request.GET.get('block')
            min_score = float(request.GET.get('min_score', 0))
            max_score = float(request.GET.get('max_score', 30))
            
            majors = Major.objects.filter(
                block=block,
                benchmark_2024__gte=min_score,
                benchmark_2024__lte=max_score
            ).select_related('university').order_by('benchmark_2024')
            
            data = []
            for major in majors:
                data.append({
                    'id': major.id,
                    'name': major.name,
                    'university': major.university.name,
                    'location': major.university.location,
                    'benchmark': major.benchmark_2024,
                    'quota': major.admission_quota,
                    'subjects': f"{major.subject_1}, {major.subject_2}, {major.subject_3}"
                })
            
            return JsonResponse({'success': True, 'majors': data})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Method not allowed'})