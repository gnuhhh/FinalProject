# Voice/voice_search_sql.py
"""
Voice Search với SQL Database - THAY THẾ HOÀN TOÀN CSV
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def search_handler_sql(request):
    """
    Xử lý tìm kiếm từ voice search result - CHỈ DÙNG SQL DATABASE
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query', '')
            filters = data.get('filters', {})
            search_type = data.get('search_type', '')

            print(f"🎯 SEARCH HANDLER SQL: query='{query}', filters={filters}, type={search_type}")

            # Import models từ app school - CHỈ DÙNG SQL DATABASE
            from school.models import School, SchoolMajor, Major

            # TÌM KIẾM THEO TRƯỜNG ĐẠI HỌC
            if filters.get('university'):
                university_name = filters['university']
                print(f"🔍 Tìm kiếm trường trong SQL: {university_name}")
                
                # Tìm trường trong SQL Database
                schools = School.objects.filter(name__icontains=university_name)
                
                if schools.exists():
                    school = schools.first()
                    print(f"✅ Tìm thấy trường trong SQL: {school.name} (ID: {school.id})")
                    
                    # Lấy các ngành của trường từ SQL
                    school_majors = SchoolMajor.objects.filter(school=school).select_related('major')[:10]
                    
                    return JsonResponse({
                        'status': 'success',
                        'query': query,
                        'filters': filters,
                        'search_type': search_type,
                        'school_name': school.name,
                        'school_id': school.id,
                        'majors_count': school_majors.count(),
                        'redirect_url': f'/school/{school.id}/',  # Chuyển đến trang chi tiết trường
                        'redirect': True,
                        'message': f'Đã tìm thấy {school_majors.count()} ngành tại {school.name} (SQL Database)'
                    })
                else:
                    return JsonResponse({
                        'status': 'success',
                        'query': query,
                        'filters': filters,
                        'search_type': search_type,
                        'count': 0,
                        'data': [],
                        'redirect': False,
                        'message': f'Không tìm thấy trường "{university_name}" trong SQL Database'
                    })

            # TÌM KIẾM THEO NGÀNH HỌC
            elif filters.get('major'):
                major_name = filters['major']
                print(f"🔍 Tìm kiếm ngành trong SQL: {major_name}")
                
                # Tìm ngành trong SQL Database
                majors = Major.objects.filter(name__icontains=major_name)
                
                if majors.exists():
                    major = majors.first()
                    # Tìm các trường có ngành này từ SQL
                    school_majors = SchoolMajor.objects.filter(major=major).select_related('school')[:10]
                    
                    return JsonResponse({
                        'status': 'success',
                        'query': query,
                        'filters': filters,
                        'search_type': search_type,
                        'major_name': major.name,
                        'schools_count': school_majors.count(),
                        'redirect_url': '/school/',  # Chuyển đến trang danh sách trường
                        'redirect': True,
                        'message': f'Đã tìm thấy {school_majors.count()} trường có ngành {major.name} (SQL Database)'
                    })
                else:
                    return JsonResponse({
                        'status': 'success',
                        'query': query,
                        'filters': filters,
                        'search_type': search_type,
                        'count': 0,
                        'data': [],
                        'redirect': False,
                        'message': f'Không tìm thấy ngành "{major_name}" trong SQL Database'
                    })

            # TÌM KIẾM CHUNG
            else:
                print(f"🔍 Tìm kiếm chung trong SQL: {query}")
                
                # Tìm trường theo tên trong SQL
                schools = School.objects.filter(name__icontains=query)[:5]
                # Tìm ngành theo tên trong SQL
                majors = Major.objects.filter(name__icontains=query)[:5]
                
                total_results = schools.count() + majors.count()
                
                return JsonResponse({
                    'status': 'success',
                    'query': query,
                    'filters': filters,
                    'search_type': search_type,
                    'schools_count': schools.count(),
                    'majors_count': majors.count(),
                    'total_results': total_results,
                    'redirect_url': '/school/',  # Chuyển đến trang danh sách trường
                    'redirect': True,
                    'message': f'Đã tìm thấy {total_results} kết quả cho "{query}" trong SQL Database'
                })
                
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi xử lý tìm kiếm SQL: {str(e)}'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ POST request'
    })