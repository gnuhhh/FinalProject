# Voice/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import speech_recognition as sr
import pyttsx3
from datetime import datetime
from django.db.models import Q

# Khởi tạo text-to-speech engine
try:
    engine = pyttsx3.init()
except:
    engine = None

# ========== VOICE SEARCH CHUYỂN HƯỚNG ĐẾN TRANG TRƯỜNG HỌC ==========

@csrf_exempt
def voice_search_start(request):
    """
    Bắt đầu tìm kiếm bằng giọng nói và trả về school_id để redirect
    """
    try:
        print("🎤 Voice search started - Frontend should show listening indicator")
        
        # Khởi tạo recognizer
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        with microphone as source:
            print("🎤 Đang điều chỉnh microphone...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✅ Microphone đã sẵn sàng!")
            
            print("🎤 Đang nghe... (nói trong 8 giây)")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
            
            print("🔍 Đang nhận diện giọng nói...")
            text = recognizer.recognize_google(audio, language='vi-VN')
            text = text.strip()
            
            print(f"📝 Đã nhận diện: {text}")
            
            # Xử lý lệnh thoại và tìm school_id
            result = process_voice_command(text)
            
            # Lưu kết quả vào session
            request.session['voice_result'] = result
            request.session.modified = True
            
            print(f"🎯 Voice result ready: {result}")
            
            return JsonResponse(result)
            
    except sr.WaitTimeoutError:
        error_msg = "❌ Không phát hiện giọng nói. Vui lòng thử lại."
        print(error_msg)
        return JsonResponse({'error': error_msg, 'success': False})
    except sr.UnknownValueError:
        error_msg = "❌ Không thể nhận diện giọng nói. Vui lòng nói rõ hơn."
        print(error_msg)
        return JsonResponse({'error': error_msg, 'success': False})
    except Exception as e:
        error_msg = f"❌ Lỗi hệ thống: {str(e)}"
        print(error_msg)
        return JsonResponse({'error': error_msg, 'success': False})

def process_voice_command(text):
    """
    Xử lý lệnh thoại và trả về thông tin chi tiết bao gồm school_id
    """
    print(f"🔍 Processing voice command: {text}")
    
    # Chuẩn hóa văn bản
    text = text.lower().strip()
    
    # Tìm trường học trong database
    school = find_school_by_name(text)
    
    if school:
        return {
            'transcript': text,
            'school_id': school.id,
            'school_name': school.schoolName,  # SỬA: schoolName thay vì name
            'search_type': 'school_detail',
            'confidence': 0.9,
            'timestamp': datetime.now().isoformat(),
            'actions': ['redirect_to_school'],
            'redirect_url': f'/school/{school.id}/',
            'success': True
        }
    else:
        return {
            'transcript': text,
            'error': 'Không tìm thấy trường học phù hợp',
            'search_type': 'unknown',
            'confidence': 0.3,
            'timestamp': datetime.now().isoformat(),
            'actions': ['show_error'],
            'success': False
        }

def find_school_by_name(school_name):
    """
    Tìm trường học theo tên trong database - SỬ DỤNG schoolName VÀ schoolId
    """
    try:
        # THỬ IMPORT MODEL SCHOOL
        School = None
        try:
            from schools.models import School
            print("✅ Imported School model from schools app")
        except ImportError:
            try:
                from school.models import School
                print("✅ Imported School model from school app")
            except ImportError:
                print("❌ Cannot import School model, using fallback data")
                return find_school_fallback(school_name)
        
        if School is None:
            return find_school_fallback(school_name)
        
        # Chuẩn hóa tên tìm kiếm
        search_name = school_name.lower()
        
        # Loại bỏ các từ thừa
        remove_words = ['đại học', 'trường', 'university', 'college', 'học viện', 'viện', 'tìm', 'kiếm']
        for word in remove_words:
            search_name = search_name.replace(word, '')
        
        search_name = search_name.strip()
        
        print(f"🔍 Searching for school: '{search_name}'")
        
        # SỬ DỤNG ĐÚNG FIELD NAME: schoolName và schoolId
        schools = School.objects.filter(
            Q(schoolName__icontains=search_name) |
            Q(schoolId__icontains=search_name) |
            Q(schoolName__icontains=school_name) |
            Q(schoolId__icontains=school_name)
        )
        
        print(f"🔍 Found {schools.count()} schools")
        
        if schools.exists():
            # Ưu tiên kết quả khớp nhất
            exact_match = schools.filter(
                Q(schoolName__iexact=search_name) |
                Q(schoolId__iexact=search_name)
            ).first()
            
            if exact_match:
                print(f"✅ Exact match: {exact_match.schoolName} (ID: {exact_match.schoolId})")
                return exact_match
            
            # Trả về kết quả đầu tiên
            first_school = schools.first()
            print(f"✅ First match: {first_school.schoolName} (ID: {first_school.schoolId})")
            return first_school
        
        print("❌ No schools found in database")
        return find_school_fallback(school_name)
        
    except Exception as e:
        print(f"❌ Error finding school: {e}")
        return find_school_fallback(school_name)

def find_school_fallback(school_name):
    """
    Fallback: sử dụng dữ liệu trường học thực tế từ danh sách của bạn
    """
    print(f"🔍 Using fallback search for: {school_name}")
    
    # Dữ liệu trường học THỰC TẾ từ danh sách của bạn
    school_mapping = {
        # Đại học Y Hà Nội
        'y hà nội': {'id': 1, 'name': 'Trường Đại học Y Hà Nội', 'abbreviation': 'YHB'},
        'y hn': {'id': 1, 'name': 'Trường Đại học Y Hà Nội', 'abbreviation': 'YHB'},
        'y sĩ': {'id': 1, 'name': 'Trường Đại học Y Hà Nội', 'abbreviation': 'YHB'},
        'bác sĩ': {'id': 1, 'name': 'Trường Đại học Y Hà Nội', 'abbreviation': 'YHB'},
        'yhb': {'id': 1, 'name': 'Trường Đại học Y Hà Nội', 'abbreviation': 'YHB'},
        'y': {'id': 1, 'name': 'Trường Đại học Y Hà Nội', 'abbreviation': 'YHB'},
        'đại học y': {'id': 1, 'name': 'Trường Đại học Y Hà Nội', 'abbreviation': 'YHB'},
        
        # Đại học Xây dựng Hà Nội
        'xây dựng': {'id': 2, 'name': 'Trường Đại học Xây dựng Hà Nội', 'abbreviation': 'XDA'},
        'xây dựng hà nội': {'id': 2, 'name': 'Trường Đại học Xây dựng Hà Nội', 'abbreviation': 'XDA'},
        'xda': {'id': 2, 'name': 'Trường Đại học Xây dựng Hà Nội', 'abbreviation': 'XDA'},
        'kiến trúc': {'id': 2, 'name': 'Trường Đại học Xây dựng Hà Nội', 'abbreviation': 'XDA'},
        'xây dựng hn': {'id': 2, 'name': 'Trường Đại học Xây dựng Hà Nội', 'abbreviation': 'XDA'},
        
        # Đại học Văn hóa Hà Nội
        'văn hóa': {'id': 3, 'name': 'Trường Đại học Văn hóa Hà Nội', 'abbreviation': 'VHH'},
        'văn hóa hà nội': {'id': 3, 'name': 'Trường Đại học Văn hóa Hà Nội', 'abbreviation': 'VHH'},
        'vhh': {'id': 3, 'name': 'Trường Đại học Văn hóa Hà Nội', 'abbreviation': 'VHH'},
        'văn hóa hn': {'id': 3, 'name': 'Trường Đại học Văn hóa Hà Nội', 'abbreviation': 'VHH'},
        
        # Đại học Thương mại
        'thương mại': {'id': 4, 'name': 'Trường Đại học Thương mại', 'abbreviation': 'TMU'},
        'tmu': {'id': 4, 'name': 'Trường Đại học Thương mại', 'abbreviation': 'TMU'},
        'kinh doanh': {'id': 4, 'name': 'Trường Đại học Thương mại', 'abbreviation': 'TMU'},
        'thương mại hn': {'id': 4, 'name': 'Trường Đại học Thương mại', 'abbreviation': 'TMU'},
        
        # Đại học Thủy lợi
        'thủy lợi': {'id': 5, 'name': 'Trường Đại học Thủy lợi', 'abbreviation': 'TLA'},
        'tla': {'id': 5, 'name': 'Trường Đại học Thủy lợi', 'abbreviation': 'TLA'},
        'thủy lợi hn': {'id': 5, 'name': 'Trường Đại học Thủy lợi', 'abbreviation': 'TLA'},
        
        # Đại học Công nghiệp TP.HCM
        'công nghiệp': {'id': 6, 'name': 'Trường Đại học Công nghiệp TP.HCM', 'abbreviation': 'IUH'},
        'công nghiệp hcm': {'id': 6, 'name': 'Trường Đại học Công nghiệp TP.HCM', 'abbreviation': 'IUH'},
        'iuh': {'id': 6, 'name': 'Trường Đại học Công nghiệp TP.HCM', 'abbreviation': 'IUH'},
        'công nghiệp tphcm': {'id': 6, 'name': 'Trường Đại học Công nghiệp TP.HCM', 'abbreviation': 'IUH'},
        
        # Đại học Khoa học Tự nhiên – ĐHQG TPHCM
        'khoa học tự nhiên': {'id': 7, 'name': 'Trường Đại học Khoa học Tự nhiên – ĐHQG TPHCM', 'abbreviation': 'QST'},
        'tự nhiên': {'id': 7, 'name': 'Trường Đại học Khoa học Tự nhiên – ĐHQG TPHCM', 'abbreviation': 'QST'},
        'qst': {'id': 7, 'name': 'Trường Đại học Khoa học Tự nhiên – ĐHQG TPHCM', 'abbreviation': 'QST'},
        'khtn': {'id': 7, 'name': 'Trường Đại học Khoa học Tự nhiên – ĐHQG TPHCM', 'abbreviation': 'QST'},
        
        # Đại học Khoa học Xã hội và Nhân văn – ĐHQG TP.HCM
        'khoa học xã hội': {'id': 8, 'name': 'Trường Đại học Khoa học xã hội và Nhân văn – ĐHQG TP.HCM', 'abbreviation': 'QSX'},
        'xã hội nhân văn': {'id': 8, 'name': 'Trường Đại học Khoa học xã hội và Nhân văn – ĐHQG TP.HCM', 'abbreviation': 'QSX'},
        'qsx': {'id': 8, 'name': 'Trường Đại học Khoa học xã hội và Nhân văn – ĐHQG TP.HCM', 'abbreviation': 'QSX'},
        'khxhnv': {'id': 8, 'name': 'Trường Đại học Khoa học xã hội và Nhân văn – ĐHQG TP.HCM', 'abbreviation': 'QSX'},
        
        # Cao đẳng Y tế Hà Nội
        'cao đẳng y tế': {'id': 9, 'name': 'Trường Cao đẳng Y tế Hà Nội', 'abbreviation': 'CYZ'},
        'y tế hà nội': {'id': 9, 'name': 'Trường Cao đẳng Y tế Hà Nội', 'abbreviation': 'CYZ'},
        'cyz': {'id': 9, 'name': 'Trường Cao đẳng Y tế Hà Nội', 'abbreviation': 'CYZ'},
        'cao đẳng y': {'id': 9, 'name': 'Trường Cao đẳng Y tế Hà Nội', 'abbreviation': 'CYZ'},
        
        # Cao đẳng Y tế Hà Đông
        'y tế hà đông': {'id': 10, 'name': 'Trường Cao đẳng Y tế Hà Đông', 'abbreviation': 'CYM'},
        'hà đông': {'id': 10, 'name': 'Trường Cao đẳng Y tế Hà Đông', 'abbreviation': 'CYM'},
        'cym': {'id': 10, 'name': 'Trường Cao đẳng Y tế Hà Đông', 'abbreviation': 'CYM'},
        
        # Cao đẳng Y khoa Phạm Ngọc Thạch
        'phạm ngọc thạch': {'id': 11, 'name': 'Trường Cao đẳng Y khoa Phạm Ngọc Thạch', 'abbreviation': 'CBK'},
        'y khoa phạm ngọc thạch': {'id': 11, 'name': 'Trường Cao đẳng Y khoa Phạm Ngọc Thạch', 'abbreviation': 'CBK'},
        'cbk': {'id': 11, 'name': 'Trường Cao đẳng Y khoa Phạm Ngọc Thạch', 'abbreviation': 'CBK'},
        'pnt': {'id': 11, 'name': 'Trường Cao đẳng Y khoa Phạm Ngọc Thạch', 'abbreviation': 'CBK'},
        
        # Cao đẳng Y Dược Tuệ Tĩnh Hà Nội
        'tuệ tĩnh': {'id': 12, 'name': 'Trường Cao đẳng Y Dược Tuệ Tĩnh Hà Nội', 'abbreviation': 'TCD0176'},
        'y dược tuệ tĩnh': {'id': 12, 'name': 'Trường Cao đẳng Y Dược Tuệ Tĩnh Hà Nội', 'abbreviation': 'TCD0176'},
        'tcd0176': {'id': 12, 'name': 'Trường Cao đẳng Y Dược Tuệ Tĩnh Hà Nội', 'abbreviation': 'TCD0176'},
        
        # Cao đẳng Y Dược Hà Nội
        'y dược hà nội': {'id': 13, 'name': 'Trường Cao đẳng Y Dược Hà Nội', 'abbreviation': 'CDD1919'},
        'cdd1919': {'id': 13, 'name': 'Trường Cao đẳng Y Dược Hà Nội', 'abbreviation': 'CDD1919'},
        'y dược hn': {'id': 13, 'name': 'Trường Cao đẳng Y Dược Hà Nội', 'abbreviation': 'CDD1919'},
        
        # Cao đẳng Y Dược Sài Gòn
        'y dược sài gòn': {'id': 14, 'name': 'Trường Cao đẳng Y Dược Sài Gòn', 'abbreviation': 'CDD4102'},
        'sài gòn': {'id': 14, 'name': 'Trường Cao đẳng Y Dược Sài Gòn', 'abbreviation': 'CDD4102'},
        'cdd4102': {'id': 14, 'name': 'Trường Cao đẳng Y Dược Sài Gòn', 'abbreviation': 'CDD4102'},
        'y dược sg': {'id': 14, 'name': 'Trường Cao đẳng Y Dược Sài Gòn', 'abbreviation': 'CDD4102'},
        
        # Cao đẳng Nông nghiệp Nam Bộ
        'nông nghiệp': {'id': 15, 'name': 'Trường Cao đẳng Nông nghiệp Nam Bộ', 'abbreviation': 'CDT5301'},
        'nông nghiệp nam bộ': {'id': 15, 'name': 'Trường Cao đẳng Nông nghiệp Nam Bộ', 'abbreviation': 'CDT5301'},
        'cdt5301': {'id': 15, 'name': 'Trường Cao đẳng Nông nghiệp Nam Bộ', 'abbreviation': 'CDT5301'},
        
        # Cao đẳng Xây dựng Tp. Hồ Chí Minh
        'xây dựng hcm': {'id': 16, 'name': 'Trường Cao đẳng Xây dựng Tp. Hồ Chí Minh', 'abbreviation': 'CDT0213'},
        'xây dựng tphcm': {'id': 16, 'name': 'Trường Cao đẳng Xây dựng Tp. Hồ Chí Minh', 'abbreviation': 'CDT0213'},
        'cdt0213': {'id': 16, 'name': 'Trường Cao đẳng Xây dựng Tp. Hồ Chí Minh', 'abbreviation': 'CDT0213'},
        
        # Cao Đẳng Việt Mỹ
        'việt mỹ': {'id': 17, 'name': 'Trường Cao Đẳng Việt Mỹ', 'abbreviation': 'CDD0208'},
        'cao đẳng việt mỹ': {'id': 17, 'name': 'Trường Cao Đẳng Việt Mỹ', 'abbreviation': 'CDD0208'},
        'cdd0208': {'id': 17, 'name': 'Trường Cao Đẳng Việt Mỹ', 'abbreviation': 'CDD0208'},
        
        # Cao đẳng Viễn Đông
        'viễn đông': {'id': 18, 'name': 'Trường Cao đẳng Viễn Đông', 'abbreviation': 'CDD0223'},
        'cao đẳng viễn đông': {'id': 18, 'name': 'Trường Cao đẳng Viễn Đông', 'abbreviation': 'CDD0223'},
        'cdd0223': {'id': 18, 'name': 'Trường Cao đẳng Viễn Đông', 'abbreviation': 'CDD0223'},
    }
    
    # Tìm kiếm trong mapping
    search_name = school_name.lower().strip()
    print(f"🔍 Searching for: '{search_name}'")
    
    # Loại bỏ các từ thừa để tìm kiếm chính xác hơn
    remove_words = ['đại học', 'trường', 'university', 'college', 'học viện', 'viện', 'tìm', 'kiếm', 'trường']
    clean_search_name = search_name
    for word in remove_words:
        clean_search_name = clean_search_name.replace(word, '')
    clean_search_name = clean_search_name.strip()
    
    print(f"🔍 Clean search name: '{clean_search_name}'")
    
    # Ưu tiên 1: Tìm kiếm chính xác
    for key, school_data in school_mapping.items():
        if key == clean_search_name:
            print(f"✅ Exact fallback match: {school_data['name']}")
            return create_mock_school(school_data)
    
    # Ưu tiên 2: Tìm kiếm chứa từ khóa
    for key, school_data in school_mapping.items():
        if key in clean_search_name:
            print(f"✅ Partial fallback match: {school_data['name']}")
            return create_mock_school(school_data)
    
    # Ưu tiên 3: Tìm kiếm trong tên đầy đủ
    for key, school_data in school_mapping.items():
        if clean_search_name in school_data['name'].lower():
            print(f"✅ Name fallback match: {school_data['name']}")
            return create_mock_school(school_data)
    
    # Ưu tiên 4: Tìm kiếm trong abbreviation
    for key, school_data in school_mapping.items():
        if clean_search_name in school_data['abbreviation'].lower():
            print(f"✅ Abbreviation fallback match: {school_data['name']}")
            return create_mock_school(school_data)
    
    print("❌ No fallback match found")
    return None

def create_mock_school(data):
    """Tạo object School giả từ dữ liệu - SỬA ĐỂ TƯƠNG THÍCH VỚI MODEL THẬT"""
    class MockSchool:
        def __init__(self, school_data):
            self.id = school_data['id']
            self.schoolName = school_data['name']  # SỬA: schoolName thay vì name
            self.schoolId = school_data.get('abbreviation', '')  # SỬA: schoolId thay vì abbreviation
    
    return MockSchool(data)

@csrf_exempt
def voice_search_stop(request):
    """Dừng tìm kiếm bằng giọng nói"""
    print("⏹️ Voice search stopped")
    return JsonResponse({'status': 'stopped', 'success': True})

def voice_search_get_result(request):
    """Lấy kết quả tìm kiếm bằng giọng nói"""
    result = request.session.get('voice_result', {})
    return JsonResponse(result)

def check_voice_availability(request):
    """Kiểm tra tính khả dụng của voice search"""
    try:
        # Kiểm tra microphone
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        return JsonResponse({
            'available': True,
            'message': 'Voice search is available',
            'success': True
        })
    except Exception as e:
        return JsonResponse({
            'available': False,
            'message': f'Voice search not available: {str(e)}',
            'success': False
        })

# ========== CÁC FUNCTION CŨ GIỮ NGUYÊN ==========

# THÊM VIEW MỚI - Voice search demo page
def voice_search_demo(request):
    """
    Trang demo voice search
    """
    return render(request, 'voice_search.html')

@csrf_exempt
def voice_command(request):
    """
    Xử lý voice command từ client - Phiên bản đơn giản
    """
    if request.method == 'POST':
        try:
            # Nhận dữ liệu từ client
            data = json.loads(request.body)
            command = data.get('command', '')
            
            # Xử lý command đơn giản
            if 'chào' in command.lower() or 'hello' in command.lower():
                response_text = f"Xin chào! Tôi đã nhận lệnh: {command}"
            elif 'tìm kiếm' in command.lower():
                response_text = f"Đang tìm kiếm: {command}"
            else:
                response_text = f"Đã nhận lệnh: {command}"
            
            return JsonResponse({
                'status': 'success', 
                'message': response_text,
                'command': command,
                'success': True
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error', 
                'message': f'Lỗi xử lý: {str(e)}',
                'success': False
            })
    
    return JsonResponse({
        'status': 'error', 
        'message': 'Chỉ hỗ trợ POST request',
        'success': False
    })

@csrf_exempt
def listen_microphone(request):
    """
    Nghe giọng nói từ microphone và chuyển thành text - Phiên bản đơn giản
    """
    if request.method == 'POST':
        try:
            recognizer = sr.Recognizer()
            
            with sr.Microphone() as source:
                print("Đang nghe... Hãy nói gì đó!")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
                
            text = recognizer.recognize_google(audio, language='vi-VN')
            
            return JsonResponse({
                'status': 'success',
                'text': text,
                'message': 'Nhận diện giọng nói thành công',
                'success': True
            })
            
        except sr.UnknownValueError:
            return JsonResponse({
                'status': 'error',
                'message': 'Không thể nhận diện giọng nói',
                'success': False
            })
        except sr.RequestError as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi kết nối đến service: {str(e)}',
                'success': False
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi: {str(e)}',
                'success': False
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ POST request',
        'success': False
    })

@csrf_exempt
def speak_text(request):
    """
    Chuyển text thành giọng nói
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            
            if engine is None:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Text-to-speech engine không khả dụng',
                    'success': False
                })
            
            engine.say(text)
            engine.runAndWait()
            
            return JsonResponse({
                'status': 'success',
                'message': f'Đã phát âm: {text}',
                'success': True
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi phát âm: {str(e)}',
                'success': False
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ POST request',
        'success': False
    })

def voice_home(request):
    """
    Trang chủ voice app
    """
    return JsonResponse({
        'status': 'success',
        'message': 'Voice app đang hoạt động',
        'services': {
            'basic_voice': {
                'voice_command': '/voice/command/',
                'listen': '/voice/listen/',
                'speak': '/voice/speak/'
            },
            'advanced_voice_search': {
                'start': '/voice/api/voice-search/start/',
                'stop': '/voice/api/voice-search/stop/',
                'get_result': '/voice/api/voice-search/get-result/',
                'check_availability': '/voice/api/voice-search/check-availability/',
            }
        },
        'description': 'Sử dụng Basic Voice cho chức năng đơn giản, Advanced Voice Search cho tìm kiếm nâng cao',
        'success': True
    })

def search(request):
    """
    Xử lý tìm kiếm thông thường
    """
    return JsonResponse({
        'status': 'success',
        'message': 'Search endpoint - Sử dụng voice search cho tìm kiếm bằng giọng nói',
        'success': True
    })

def profile(request):
    """
    Xử lý profile
    """
    return JsonResponse({
        'status': 'success',
        'message': 'Profile endpoint',
        'success': True
    })

# Test endpoint để kiểm tra voice search
@csrf_exempt
def voice_search_test(request):
    """Endpoint test để kiểm tra voice search"""
    test_queries = [
        "đại học y hà nội",
        "xây dựng", 
        "thương mại",
        "y hà nội",
        "yhb",
        "tmu"
    ]
    
    results = {}
    for query in test_queries:
        results[query] = process_voice_command(query)
    
    return JsonResponse({
        'test_results': results,
        'message': 'Test voice search functionality',
        'success': True
    })
    
def process_voice_command(text):
    """
    Xử lý lệnh thoại và trả về thông tin chi tiết - HỖ TRỢ THÀNH PHỐ
    """
    print(f"🔍 Processing voice command: {text}")
    
    # Chuẩn hóa văn bản
    text = text.lower().strip()
    
    # KIỂM TRA TÌM KIẾM THEO THÀNH PHỐ TRƯỚC
    city_result = process_city_search(text)
    if city_result:
        return city_result
    
    # Nếu không phải tìm kiếm thành phố, tìm trường học cụ thể
    school = find_school_by_name(text)
    
    if school:
        return {
            'transcript': text,
            'school_id': school.id,
            'school_name': school.schoolName,
            'search_type': 'school_detail',
            'confidence': 0.9,
            'timestamp': datetime.now().isoformat(),
            'actions': ['redirect_to_school'],
            'redirect_url': f'/school/{school.id}/',
            'success': True
        }
    else:
        return {
            'transcript': text,
            'error': 'Không tìm thấy trường học phù hợp',
            'search_type': 'unknown',
            'confidence': 0.3,
            'timestamp': datetime.now().isoformat(),
            'actions': ['show_error'],
            'success': False
        }

def process_city_search(text):
    """
    Xử lý tìm kiếm theo thành phố - SỬ DỤNG URLs CÓ SẴN
    """
    city_mapping = {
        'hà nội': {
            'redirect_url': '/school/hanoi/',
            'name': 'Hà Nội',
            'description': 'Các trường đại học tại Hà Nội'
        },
        'hà nội': {
            'redirect_url': '/school/hanoi/',
            'name': 'Hà Nội', 
            'description': 'Các trường đại học tại Hà Nội'
        },
        'hn': {
            'redirect_url': '/school/hanoi/',
            'name': 'Hà Nội',
            'description': 'Các trường đại học tại Hà Nội'
        },
        'hồ chí minh': {
            'redirect_url': '/school/tphcm/',
            'name': 'Thành phố Hồ Chí Minh',
            'description': 'Các trường đại học tại TP.HCM'
        },
        'hcm': {
            'redirect_url': '/school/tphcm/',
            'name': 'Thành phố Hồ Chí Minh',
            'description': 'Các trường đại học tại TP.HCM'
        },
        'tphcm': {
            'redirect_url': '/school/tphcm/',
            'name': 'Thành phố Hồ Chí Minh',
            'description': 'Các trường đại học tại TP.HCM'
        },
        'tp hcm': {
            'redirect_url': '/school/tphcm/',
            'name': 'Thành phố Hồ Chí Minh',
            'description': 'Các trường đại học tại TP.HCM'
        },
        'sài gòn': {
            'redirect_url': '/school/tphcm/',
            'name': 'Thành phố Hồ Chí Minh',
            'description': 'Các trường đại học tại TP.HCM'
        },
        'sg': {
            'redirect_url': '/school/tphcm/',
            'name': 'Thành phố Hồ Chí Minh',
            'description': 'Các trường đại học tại TP.HCM'
        },
        'thành phố hồ chí minh': {
            'redirect_url': '/school/tphcm/',
            'name': 'Thành phố Hồ Chí Minh',
            'description': 'Các trường đại học tại TP.HCM'
        }
    }
    
    for city_key, city_data in city_mapping.items():
        if city_key in text:
            print(f"🎯 City search detected: {city_data['name']} -> {city_data['redirect_url']}")
            return {
                'transcript': text,
                'city_name': city_data['name'],
                'city_description': city_data['description'],
                'search_type': 'city',
                'confidence': 0.8,
                'timestamp': datetime.now().isoformat(),
                'actions': ['redirect_to_city'],
                'redirect_url': city_data['redirect_url'],
                'success': True
            }
    
    return None