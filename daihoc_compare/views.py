from django.shortcuts import render, redirect
from admission_predictor.models import University, Major

def compare_universities(request):
    """Trang chọn trường để so sánh"""
    universities = University.objects.all().order_by('name')
    
    context = {
        'title': 'So sánh trường đại học',
        'universities': universities,
    }
    return render(request, 'daihoc_compare/compare.html', context)

def compare_result(request):
    """Hiển thị kết quả so sánh"""
    if request.method == 'POST':
        try:
            uni1_id = request.POST.get('university1')
            uni2_id = request.POST.get('university2')
            
            uni1 = University.objects.get(id=uni1_id)
            uni2 = University.objects.get(id=uni2_id)
            
            # Lấy các ngành phổ biến của 2 trường
            uni1_majors = Major.objects.filter(university=uni1).order_by('-benchmark_2024')[:8]
            uni2_majors = Major.objects.filter(university=uni2).order_by('-benchmark_2024')[:8]
            
            # Dữ liệu mẫu - bạn có thể cập nhật thành dữ liệu thực
            comparison_data = {
                'uni1': {
                    'name': uni1.name,
                    'code': uni1.code,
                    'location': uni1.location,
                    'type': uni1.get_type_display(),
                    'website': uni1.website,
                    'tuition': '15-25 triệu/kỳ' if uni1.type == 'public' else '30-50 triệu/kỳ',
                    'facilities': 'Thư viện hiện đại, phòng lab, ký túc xá, khu thể thao',
                    'campuses': f'{uni1.location}, Hồ Chí Minh, Đà Nẵng',
                    'employment_rate': 95.5,
                    'scholarships': 'Học bổng toàn phần, bán phần, tài năng, khuyến học',
                    'avg_score': 25.5,
                    'description': f'Trường {uni1.type} hàng đầu tại {uni1.location}'
                },
                'uni2': {
                    'name': uni2.name,
                    'code': uni2.code,
                    'location': uni2.location,
                    'type': uni2.get_type_display(),
                    'website': uni2.website,
                    'tuition': '12-20 triệu/kỳ' if uni2.type == 'public' else '25-45 triệu/kỳ',
                    'facilities': 'Khu thể thao, trung tâm nghiên cứu, canteen, thư viện',
                    'campuses': f'{uni2.location}, Hà Nội, Cần Thơ',
                    'employment_rate': 92.3,
                    'scholarships': 'Học bổng khuyến học, vượt khó, tài năng',
                    'avg_score': 24.8,
                    'description': f'Trường {uni2.type} chất lượng cao tại {uni2.location}'
                }
            }
            
            context = {
                'title': f'So sánh {uni1.name} vs {uni2.name}',
                'uni1': comparison_data['uni1'],
                'uni2': comparison_data['uni2'],
                'uni1_majors': uni1_majors,
                'uni2_majors': uni2_majors,
            }
            
            return render(request, 'daihoc_compare/result.html', context)
            
        except Exception as e:
            print(f"❌ Lỗi so sánh: {e}")
            return render(request, 'daihoc_compare/error.html', {
                'message': 'Có lỗi xảy ra khi so sánh. Vui lòng thử lại.'
            })
    
    return redirect('daihoc_compare:compare_universities')