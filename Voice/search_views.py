# Voice/search_views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from school.models import School, Major, SchoolMajor  # IMPORT MODELS THỰC TẾ

@csrf_exempt
def handle_voice_search(request):
    """
    Xử lý tìm kiếm từ kết quả voice recognition và trả về URL chuyển hướng
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            search_filters = data.get('filters', {})
            search_type = data.get('search_type', 'general')
            query = data.get('query', '')
            
            # Tìm thông tin để chuyển hướng
            redirect_info = find_redirect_target(search_filters, search_type, query)
            
            return JsonResponse({
                'status': 'success',
                'redirect': True,
                'redirect_url': redirect_info['url'],
                'school_name': redirect_info['name'],
                'school_id': redirect_info.get('school_id'),
                'message': f'Chuyển hướng đến {redirect_info["name"]}'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Lỗi tìm kiếm: {str(e)}'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Chỉ hỗ trợ POST request'
    })

def find_redirect_target(filters, search_type, query):
    """
    Tìm URL chuyển hướng dựa trên kết quả voice search
    Sử dụng database thực tế
    """
    
    # === THÊM PHẦN TỪ KHÓA CHUYỂN HƯỚNG NHANH ===
    quick_redirects = {
        'trang chủ': {'url': '/', 'name': 'Trang chủ', 'type': 'quick'},
        'home': {'url': '/', 'name': 'Trang chủ', 'type': 'quick'},
        'đăng nhập': {'url': '/login/', 'name': 'Đăng nhập', 'type': 'quick'},
        'đăng ký': {'url': '/register/', 'name': 'Đăng ký', 'type': 'quick'},
        'tư vấn': {'url': '/advise/', 'name': 'Tư vấn', 'type': 'quick'},
        'chỉ tiêu': {'url': '/prediction/', 'name': 'Dự đoán chỉ tiêu', 'type': 'quick'},
        'so sánh': {'url': '/compare/', 'name': 'So sánh trường', 'type': 'quick'},
        'tin tức': {'url': '/news/', 'name': 'Tin tức', 'type': 'quick'},
        'chat': {'url': '/chat/', 'name': 'Trò chuyện', 'type': 'quick'},
        'hồ sơ': {'url': '/user_profile/', 'name': 'Hồ sơ cá nhân', 'type': 'quick'},
        'tuyển sinh': {'url': '/admission/', 'name': 'Thông tin tuyển sinh', 'type': 'quick'},
        'ngành học': {'url': '/majors/', 'name': 'Danh sách ngành học', 'type': 'quick'},
        'học bổng': {'url': '/scholarship/', 'name': 'Học bổng', 'type': 'quick'},
        'liên hệ': {'url': '/contact/', 'name': 'Liên hệ', 'type': 'quick'},
        'hướng dẫn': {'url': '/guide/', 'name': 'Hướng dẫn', 'type': 'quick'},
        'thống kê': {'url': '/prediction/statistics/', 'name': 'Thống kê', 'type': 'quick'},
        'kiểm tra': {'url': '/test-khoi/', 'name': 'Kiểm tra', 'type': 'quick'},
        'khối': {'url': '/test-khoi/', 'name': 'Kiểm tra khối', 'type': 'quick'},
        'chuyên nghành': {'url': '/tests/', 'name': 'Bài test chuyên nghành', 'type': 'quick'},
        'dự đoán': {'url': '/du-doan-dai-hoc/du-doan-dai-hoc/', 'name': 'Dự đoán đại học', 'type': 'quick'},
        'định hướng': {'url': '/question/', 'name': 'Câu hỏi định hướng', 'type': 'quick'},
    }
    
    # Kiểm tra từ khóa chuyển hướng nhanh trước
    lower_query = query.lower() if query else ""
    for keyword, redirect_info in quick_redirects.items():
        if keyword in lower_query:
            print(f"✅ Chuyển hướng nhanh: '{keyword}' -> {redirect_info['url']}")
            return redirect_info
    
    # Tìm kiếm theo tên trường
    if search_type == 'university' and 'university' in filters:
        school_name = filters['university']
        school = find_school_by_name(school_name)
        if school:
            return {
                'url': f'/school/{school.id}/',  # URL theo ID
                'name': school.schoolName,
                'school_id': school.id,
                'type': 'school'
            }
    
    # Tìm kiếm theo ngành học
    elif search_type == 'major' and 'major' in filters:
        major_name = filters['major']
        school = find_school_by_major(major_name)
        if school:
            return {
                'url': f'/school/{school.id}/',
                'name': school.schoolName,
                'school_id': school.id,
                'type': 'major',
                'major': major_name
            }
    
    # Tìm kiếm tổng quát
    elif search_type == 'general' and query:
        # Thử tìm trường trước
        school = find_school_by_name(query)
        if school:
            return {
                'url': f'/school/{school.id}/',
                'name': school.schoolName,
                'school_id': school.id,
                'type': 'school'
            }
        
        # Thử tìm theo ngành
        school = find_school_by_major(query)
        if school:
            return {
                'url': f'/school/{school.id}/',
                'name': school.schoolName,
                'school_id': school.id,
                'type': 'major'
            }
    
    # Mặc định nếu không tìm thấy
    return {
        'url': '/school/',  # Trang danh sách trường
        'name': 'Danh sách trường',
        'type': 'default'
    }

def find_school_by_name(school_name):
    """
    Tìm trường theo tên (tìm kiếm gần đúng)
    """
    try:
        # Tìm trường có tên chứa từ khóa
        schools = School.objects.filter(schoolName__icontains=school_name)
        if schools.exists():
            print(f"✅ Tìm thấy trường trực tiếp: {schools.first().schoolName}")
            return schools.first()
        
        # Ánh xạ từ khóa thông dụng - SỬA LẠI CHO CHÍNH XÁC
        keyword_mapping = {
            'bách khoa': 'Bách Khoa',
            'bách khoa hà nội': 'Bách Khoa Hà Nội',
            'bách khoa hcm': 'Bách Khoa',
            'fpt': 'FPT', 
            'kinh tế': 'Kinh Tế',
            'kinh tế quốc dân': 'Kinh Tế Quốc Dân',
            'công nghệ': 'Công Nghệ',
            'công nghiệp': 'Công Nghiệp',  # THÊM DÒNG NÀY
            'đại học công nghiệp': 'Công Nghiệp',  # THÊM DÒNG NÀY
            'y học': 'Y',
            'y khoa': 'Y',
            'y hà nội': 'Y Hà Nội',
            'luật': 'Luật',
            'luật hà nội': 'Luật Hà Nội',
            'xây dựng': 'Xây Dựng',
            'kiến trúc': 'Kiến Trúc',
            'sư phạm': 'Sư Phạm',
            'sư phạm hà nội': 'Sư Phạm Hà Nội',
            'thương mại': 'Thương Mại',
            'ngoại thương': 'Ngoại Thương',
            'giao thông': 'Giao Thông',
            'giao thông vận tải': 'Giao Thông Vận Tải',
            'nông nghiệp': 'Nông Nghiệp'
        }
        
        for keyword, school_keyword in keyword_mapping.items():
            if keyword in school_name.lower():
                print(f"🔍 Tìm trường theo keyword: '{keyword}' -> '{school_keyword}'")
                schools = School.objects.filter(schoolName__icontains=school_keyword)
                if schools.exists():
                    print(f"✅ Tìm thấy trường: {schools.first().schoolName}")
                    return schools.first()
        
        print(f"❌ Không tìm thấy trường cho: {school_name}")
        return None
    except Exception as e:
        print(f"❌ Lỗi tìm trường theo tên: {e}")
        return None

def find_school_by_major(major_name):
    """
    Tìm trường theo ngành học
    """
    try:
        # Tìm ngành có tên chứa từ khóa
        majors = Major.objects.filter(major_name__icontains=major_name)
        if majors.exists():
            # Lấy trường đầu tiên có ngành này
            school_major = SchoolMajor.objects.filter(major=majors.first()).first()
            if school_major:
                return school_major.school
        
        # Ánh xạ ngành học thông dụng
        major_mapping = {
            'công nghệ thông tin': ['Công Nghệ Thông Tin', 'CNTT', 'IT'],
            'quản trị kinh doanh': ['Quản Trị Kinh Doanh', 'QTKD' ,'kinh doanh'],
            'kế toán': ['Kế Toán'],
            'tài chính ngân hàng': ['Tài Chính Ngân Hàng','Tài chính'],
            'marketing': ['Marketing'],
            'kỹ thuật điện tử': ['Kỹ Thuật Điện Tử','Điện tử'],
            'kỹ thuật cơ khí': ['Kỹ Thuật Cơ Khí','Cơ khí'],
            'xây dựng': ['Xây Dựng'],
            'kiến trúc': ['Kiến Trúc'],
            'y khoa': ['Y Khoa', 'Bác Sĩ'],
            'dược': ['Dược','dược sĩ'],
            'luật': ['Luật','luật sư'],
            'sư phạm': ['Sư Phạm','Giáo viên'],
            'du lịch': ['Du Lịch'],
            'nhà hàng khách sạn': ['Nhà Hàng Khách Sạn', 'Quản Trị Khách Sạn']
        }
        
        for major_key, search_terms in major_mapping.items():
            if major_key in major_name.lower():
                for term in search_terms:
                    majors = Major.objects.filter(major_name__icontains=term)
                    if majors.exists():
                        school_major = SchoolMajor.objects.filter(major=majors.first()).first()
                        if school_major:
                            return school_major.school
        
        return None
    except Exception as e:
        print(f"Lỗi tìm trường theo ngành: {e}")
        return None