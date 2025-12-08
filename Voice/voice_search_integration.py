# Voice/voice_search_integration.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .voice_search import VoiceSearch
import threading
import queue

# Khởi tạo VoiceSearch instance
voice_search_engine = VoiceSearch()
voice_active = False
result_queue = queue.Queue()

# Callback functions để gửi kết quả về frontend
def on_voice_start(data):
    print("🎤 Voice search started - Frontend should show listening indicator")

def on_voice_result(result):
    print(f"📝 Voice result ready for frontend: {result}")
    # 🔥 QUAN TRỌNG: Clear queue trước khi thêm kết quả mới
    while not result_queue.empty():
        try:
            result_queue.get_nowait()
        except:
            pass
    # Lưu kết quả vào queue để frontend lấy
    result_queue.put(result)

def on_voice_error(error):
    print(f"❌ Voice error: {error}")

def on_voice_stop(data):
    print("⏹️ Voice search stopped")

# Thiết lập callbacks
voice_search_engine.set_callback('on_start', on_voice_start)
voice_search_engine.set_callback('on_result', on_voice_result)
voice_search_engine.set_callback('on_error', on_voice_error)
voice_search_engine.set_callback('on_stop', on_voice_stop)

@csrf_exempt
def start_voice_search(request):
    """
    Bắt đầu quá trình voice search
    """
    global voice_active
    
    if request.method == 'POST':
        try:
            if voice_active:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Voice search đang chạy'
                })
            
            # 🔥 QUAN TRỌNG: Clear queue trước khi bắt đầu lần nghe mới
            while not result_queue.empty():
                try:
                    result_queue.get_nowait()
                except:
                    pass
            
            success = voice_search_engine.start_listening()
            
            if success:
                voice_active = True
                return JsonResponse({
                    'status': 'success',
                    'message': 'Voice search đã được kích hoạt',
                    'listening': True
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Không thể khởi động voice search'
                })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi khởi động voice search: {str(e)}'
            })
    
    # Cho phép GET để test
    return JsonResponse({
        'status': 'success',
        'message': 'Voice search endpoint is ready',
        'method': 'Use POST to start voice search'
    })

@csrf_exempt
def stop_voice_search(request):
    """
    Dừng quá trình voice search
    """
    global voice_active
    
    if request.method == 'POST':
        voice_search_engine.stop_listening()
        voice_active = False
        
        return JsonResponse({
            'status': 'success',
            'message': 'Voice search đã dừng',
            'listening': False
        })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ POST request'
    })

@csrf_exempt
def process_voice_command(request):
    """
    Xử lý voice command từ client và trả về kết quả ngay lập tức
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            voice_text = data.get('text', '')
            
            # Xử lý command bằng VoiceSearch engine
            processed_result = voice_search_engine.process_text_command(voice_text)
            
            return JsonResponse({
                'status': 'success',
                'command': voice_text,
                'result': processed_result,
                'message': 'Xử lý command thành công'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi xử lý command: {str(e)}'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ POST request'
    })

@csrf_exempt
def get_voice_result(request):
    """
    Endpoint để frontend lấy kết quả voice recognition
    """
    try:
        # Lấy kết quả từ queue (non-blocking)
        if not result_queue.empty():
            result = result_queue.get_nowait()
            # 🔥 QUAN TRỌNG: Clear queue sau khi lấy kết quả
            while not result_queue.empty():
                try:
                    result_queue.get_nowait()
                except:
                    pass
            return JsonResponse({
                'status': 'success',
                'result': result,
                'has_result': True
            })
        else:
            return JsonResponse({
                'status': 'success',
                'has_result': False,
                'message': 'Chưa có kết quả'
            })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Lỗi lấy kết quả: {str(e)}'
        })

@csrf_exempt
def get_search_suggestions(request):
    """
    Gợi ý tìm kiếm dựa trên input - DÙNG SQL DATABASE
    """
    if request.method == 'GET':
        try:
            query = request.GET.get('query', '')
            
            # Import models từ app school
            from school.models import School, Major
            
            suggestions = []
            
            # Tìm kiếm trường học
            schools = School.objects.filter(name__icontains=query)[:5]
            for school in schools:
                suggestions.append({
                    'type': 'school',
                    'value': school.name,
                    'display': f'🏫 {school.name}',
                    'action': 'filter_school'
                })
            
            # Tìm kiếm ngành học
            majors = Major.objects.filter(name__icontains=query)[:5]
            for major in majors:
                suggestions.append({
                    'type': 'major',
                    'value': major.name,
                    'display': f'🎓 {major.name}',
                    'action': 'filter_major'
                })
            
            return JsonResponse({
                'status': 'success',
                'query': query,
                'suggestions': suggestions,
                'message': 'Đã tạo gợi ý tìm kiếm từ SQL Database'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi tạo gợi ý: {str(e)}'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ GET request'
    })

@csrf_exempt
def check_voice_availability(request):
    """
    Kiểm tra tính khả dụng của voice search
    """
    if request.method == 'GET':
        try:
            available = voice_search_engine.is_available()
            
            return JsonResponse({
                'status': 'success',
                'available': available,
                'microphone': available,
                'speech_recognition': True,
                'message': 'Voice search khả dụng' if available else 'Microphone không khả dụng'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'available': False,
                'microphone': False,
                'error': str(e),
                'message': 'Voice search không khả dụng'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ GET request'
    })

# 🔥 THAY THẾ HOÀN TOÀN BẰNG SQL DATABASE
@csrf_exempt
def search_handler(request):
    """
    Xử lý tìm kiếm từ voice search result - CHỈ DÙNG SQL DATABASE
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query', '')
            filters = data.get('filters', {})
            search_type = data.get('search_type', '')

            print(f"🎯 SEARCH HANDLER - SQL DATABASE ONLY: query='{query}', filters={filters}, type={search_type}")

            # Import models từ app school - CHỈ DÙNG SQL DATABASE
            from school.models import School, SchoolMajor, Major

            # TÌM KIẾM THEO TRƯỜNG ĐẠI HỌC
            if filters.get('university'):
                university_name = filters['university']
                print(f"🔍 Tìm kiếm trường trong SQL DATABASE: {university_name}")
                
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
                    # Không tìm thấy trường, tìm theo tên gần đúng
                    all_schools = School.objects.all()
                    matched_schools = []
                    
                    for school in all_schools:
                        if university_name.lower() in school.name.lower():
                            matched_schools.append(school)
                    
                    if matched_schools:
                        school = matched_schools[0]
                        return JsonResponse({
                            'status': 'success',
                            'query': query,
                            'filters': filters,
                            'search_type': search_type,
                            'school_name': school.name,
                            'school_id': school.id,
                            'redirect_url': f'/school/{school.id}/',
                            'redirect': True,
                            'message': f'Đã tìm thấy trường: {school.name} (SQL Database)'
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
                print(f"🔍 Tìm kiếm ngành trong SQL DATABASE: {major_name}")
                
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
                print(f"🔍 Tìm kiếm chung trong SQL DATABASE: {query}")
                
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
            print(f"❌ Lỗi SQL Database: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi xử lý tìm kiếm SQL Database: {str(e)}'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ POST request'
    })