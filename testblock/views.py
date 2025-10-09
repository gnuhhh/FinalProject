# testblock/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
import os
import sys
import django
import importlib.util
import json
from django.conf import settings

# Setup Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')
django.setup()

from .models import TestBlock, BlockQuestion, BlockTestResult, Subject, SubjectTestResult

# ========== CÁC HÀM HỖ TRỢ ==========
def get_subject_name(subject_code):
    """Lấy tên môn học từ mã môn"""
    name_mapping = {
        'A_TOAN': 'Toán học', 'A_LY': 'Vật lý', 'A_HOA': 'Hóa học',
        'B_TOAN': 'Toán học', 'B_HOA': 'Hóa học', 'B_SINH': 'Sinh học', 
        'C_VAN': 'Ngữ văn', 'C_SU': 'Lịch sử', 'C_DIA': 'Địa lý',
        'D_TOAN': 'Toán học', 'D_VAN': 'Ngữ văn', 'D_TA': 'Tiếng Anh',
        'A01_TOAN': 'Toán học', 'A01_LY': 'Vật lý', 'A01_TA': 'Tiếng Anh',
        'B01_TOAN': 'Toán học', 'B01_HOA': 'Hóa học', 'B01_TA': 'Tiếng Anh',
        'D07_TOAN': 'Toán học', 'D07_HOA': 'Hóa học', 'D07_TA': 'Tiếng Anh',
        'B02_TOAN': 'Toán học', 'B02_SINH': 'Sinh học', 'B02_DIA': 'Địa lý',
        'C01_VAN': 'Ngữ văn', 'C01_TOAN': 'Toán học', 'C01_LY': 'Vật lý',
        'D14_VAN': 'Ngữ văn', 'D14_LS': 'Lịch sử', 'D14_TA': 'Tiếng Anh',
        'D15_VAN': 'Ngữ văn', 'D15_DIA': 'Địa lý', 'D15_TA': 'Tiếng Anh'
    }
    return name_mapping.get(subject_code, 'Môn học')

# ========== CÁC VIEW CHÍNH ==========
def test_block_list(request):
    """Trang chủ - Danh sách khối thi"""
    test_blocks = TestBlock.objects.all()
    return render(request, 'testblock/test_block_list.html', {
        'test_blocks': test_blocks,
        'title': 'Test Khối Thi Đại Học'
    })

def subject_test_list(request, block_code):
    """Hiển thị danh sách môn học theo khối"""
    print(f"🎯 Đang hiển thị môn học khối: {block_code}")
    
    blocks_data = {
        'khoi-A': {
            'name': 'Khối A',
            'subjects': [
                {'code': 'A_TOAN', 'name': 'Toán học', 'description': 'Đại số, Giải tích, Hình học', 'total_questions': 50, 'time_limit': 90},
                {'code': 'A_LY', 'name': 'Vật lí', 'description': 'Cơ học, Điện tử, Quang học', 'total_questions': 50, 'time_limit': 90},
                {'code': 'A_HOA', 'name': 'Hóa học', 'description': 'Hóa vô cơ, Hóa hữu cơ', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-B': {
            'name': 'Khối B', 
            'subjects': [
                {'code': 'B_TOAN', 'name': 'Toán học', 'description': 'Toán phân tích và thống kê', 'total_questions': 50, 'time_limit': 90},
                {'code': 'B_HOA', 'name': 'Hóa học', 'description': 'Hóa sinh và hóa phân tích', 'total_questions': 50, 'time_limit': 90},
                {'code': 'B_SINH', 'name': 'Sinh học', 'description': 'Di truyền, Sinh học phân tử', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-C': {
            'name': 'Khối C',
            'subjects': [
                {'code': 'C_VAN', 'name': 'Ngữ văn', 'description': 'Văn học và Tiếng Việt', 'total_questions': 50, 'time_limit': 90},
                {'code': 'C_SU', 'name': 'Lịch sử', 'description': 'Lịch sử Việt Nam và Thế giới', 'total_questions': 50, 'time_limit': 90},
                {'code': 'C_DIA', 'name': 'Địa lí', 'description': 'Địa lý tự nhiên và kinh tế', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-D': {
            'name': 'Khối D',
            'subjects': [
                {'code': 'D_TOAN', 'name': 'Toán học', 'description': 'Toán tổng hợp', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D_VAN', 'name': 'Ngữ văn', 'description': 'Văn học và ngôn ngữ', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D_TA', 'name': 'Tiếng Anh', 'description': 'Tiếng Anh tổng quát', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-A01': {
            'name': 'Khối A01',
            'subjects': [
                {'code': 'A01_TOAN', 'name': 'Toán học', 'description': 'Toán cao cấp và ứng dụng', 'total_questions': 50, 'time_limit': 90},
                {'code': 'A01_LY', 'name': 'Vật lí', 'description': 'Vật lý đại cương và chuyên ngành', 'total_questions': 50, 'time_limit': 90},
                {'code': 'A01_TA', 'name': 'Tiếng Anh', 'description': 'Tiếng Anh kỹ thuật', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-B01': {
            'name': 'Khối B01',
            'subjects': [
                {'code': 'B01_TOAN', 'name': 'Toán học', 'description': 'Toán cao cấp và ứng dụng', 'total_questions': 50, 'time_limit': 90},
                {'code': 'B01_HOA', 'name': 'Hóa học', 'description': 'Hóa sinh và hóa phân tích', 'total_questions': 50, 'time_limit': 90},
                {'code': 'B01_TA', 'name': 'Tiếng Anh', 'description': 'Tiếng Anh kỹ thuật', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-D07': {
            'name': 'Khối D07',
            'subjects': [
                {'code': 'D07_TOAN', 'name': 'Toán học', 'description': 'Toán cao cấp và ứng dụng', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D07_HOA', 'name': 'Hóa học', 'description': 'Hóa sinh và hóa phân tích', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D07_TA', 'name': 'Tiếng Anh', 'description': 'Tiếng Anh kỹ thuật', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-B02': {
            'name': 'Khối B02',
            'subjects': [
                {'code': 'B02_TOAN', 'name': 'Toán học', 'description': 'Toán cao cấp và ứng dụng', 'total_questions': 50, 'time_limit': 90},
                {'code': 'B02_SINH', 'name': 'Sinh học', 'description': 'Sinh học phân tử và tế bào', 'total_questions': 50, 'time_limit': 90},
                {'code': 'B02_DIA', 'name': 'Địa lý', 'description': 'Địa lý tự nhiên và kinh tế', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-C01': {
            'name': 'Khối C01',
            'subjects': [
                {'code': 'C01_VAN', 'name': 'Ngữ văn', 'description': 'Văn học và ngôn ngữ', 'total_questions': 50, 'time_limit': 90},
                {'code': 'C01_TOAN', 'name': 'Toán học', 'description': 'Toán cao cấp và ứng dụng', 'total_questions': 50, 'time_limit': 90},
                {'code': 'C01_LY', 'name': 'Vật lý', 'description': 'Vật lý đại cương và ứng dụng', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-D14': {
            'name': 'Khối D14',
            'subjects': [
                {'code': 'D14_VAN', 'name': 'Ngữ văn', 'description': 'Văn học và ngôn ngữ', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D14_LS', 'name': 'Lịch sử', 'description': 'Lịch sử Việt Nam và thế giới', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D14_TA', 'name': 'Tiếng Anh', 'description': 'Tiếng Anh kỹ thuật', 'total_questions': 50, 'time_limit': 90}
            ]
        },
        'khoi-D15': {
            'name': 'Khối D15',
            'subjects': [
                {'code': 'D15_VAN', 'name': 'Ngữ văn', 'description': 'Văn học và ngôn ngữ', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D15_DIA', 'name': 'Địa lý', 'description': 'Địa lý tự nhiên và kinh tế', 'total_questions': 50, 'time_limit': 90},
                {'code': 'D15_TA', 'name': 'Tiếng Anh', 'description': 'Tiếng Anh kỹ thuật', 'total_questions': 50, 'time_limit': 90}
            ]
        }
    }
    
    block_info = blocks_data.get(block_code)
    if not block_info:
        return render(request, 'testblock/error.html', {'message': 'Khối không tồn tại'})
    
    return render(request, 'testblock/subject_test_list.html', {
        'block_code': block_code,
        'block_info': block_info
    })

def start_subject_test(request, block_code, subject_code):
    """Bắt đầu làm bài test môn học - CHỈ SỬ DỤNG DATABASE"""
    print(f"🚀 Bắt đầu làm bài: {block_code}/{subject_code}")
    subject_code = subject_code.upper()
    print(f"🔍 Đang tìm môn học với code: {subject_code}")
    # DEBUG: Kiểm tra database
    print("=== DEBUG DATABASE ===")
    print(f"Subject có trong DB: {[s.code for s in Subject.objects.all()]}")
    print(f"Tổng số câu hỏi: {BlockQuestion.objects.count()}")
    
    try:
        print(f"🔍 Đang tìm môn học với code: {subject_code}")
        subject_obj = Subject.objects.get(code=subject_code)
        print(f"✅ Tìm thấy môn học: {subject_obj.name} (code: {subject_obj.code})")
        
        # Lấy tất cả câu hỏi từ database
        db_questions = BlockQuestion.objects.filter(subject=subject_obj)
        print(f"🔍 Số câu hỏi tìm thấy: {db_questions.count()}")
        
        if db_questions.exists():
            print(f"✅ Lấy {db_questions.count()} câu hỏi từ database cho {subject_obj.name}")
            all_questions = []
            for q in db_questions:
                all_questions.append({
                    'id': q.id,
                    'question_text': q.text,
                    'options': [
                        f"A. {q.option_a}",
                        f"B. {q.option_b}",
                        f"C. {q.option_c}",
                        f"D. {q.option_d}"
                    ],
                    'correct_answer': q.correct_answer,
                    'explanation': ''
                })

            subject_name = subject_obj.name
            total_questions = len(all_questions)
            time_limit = 90
            print(f"✅ Đã tạo {total_questions} câu hỏi từ database")

        else:
            print(f"❌ KHÔNG CÓ CÂU HỎI TRONG DATABASE cho {subject_code}")
            return render(request, 'testblock/error.html', {
                'message': f'Không có câu hỏi nào cho môn học {subject_code}. Vui lòng liên hệ quản trị viên.'
            })

    except Subject.DoesNotExist:
        print(f"❌ Không tìm thấy môn học trong database: {subject_code}")
        return render(request, 'testblock/error.html', {
            'message': f'Môn học {subject_code} không tồn tại trong hệ thống.'
        })

    print(f"📊 Số câu hỏi: {total_questions}, Thời gian: {time_limit} phút")
    
    # Truyền dữ liệu cho template
    return render(request, "testblock/subject_test_infor.html", {
        "subject_code": subject_code,
        "block_code": block_code,
        "subject_name": subject_name,
        "total_questions": total_questions,
        "time_limit": time_limit,
        "questions": all_questions,
    })

def submit_subject_test(request, block_code, subject_code):
    """Xử lý kết quả bài test môn học - FIXED VERSION"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_answers = data.get('answers', {})
            time_taken = data.get('time_taken', 0)
            user_name = data.get('user_name', 'Thí sinh')
            
            print(f"📝 Nộp bài môn: {subject_code} trong khối {block_code}")
            print(f"📝 Số câu trả lời: {len(user_answers)}")
            
            # CHUYỂN SUBJECT_CODE SANG CHỮ HOA
            subject_code = subject_code.upper()
            
            # LẤY CÂU HỎI TỪ DATABASE
            try:
                subject_obj = Subject.objects.get(code=subject_code)
                db_questions = BlockQuestion.objects.filter(subject=subject_obj)
                
                if not db_questions.exists():
                    raise Exception("Không có câu hỏi trong database")
                    
                print(f"✅ Chấm điểm với {db_questions.count()} câu hỏi từ database")
                test_questions = []
                for q in db_questions:
                    test_questions.append({
                        'id': q.id,
                        'question_text': q.text,
                        'options': [
                            f"A. {q.option_a}",
                            f"B. {q.option_b}", 
                            f"C. {q.option_c}",
                            f"D. {q.option_d}"
                        ],
                        'correct_answer': q.correct_answer,
                        'explanation': ''
                    })
                    
            except Exception as e:
                print(f"❌ Lỗi khi lấy câu hỏi từ database: {e}")
                return JsonResponse({
                    'success': False, 
                    'error': 'Không thể lấy câu hỏi từ hệ thống. Vui lòng thử lại sau.'
                }, status=400)
            
            # CHẤM ĐIỂM
            correct_count = 0
            question_details = []
            
            print(f"🔍 Bắt đầu chấm điểm với {len(test_questions)} câu hỏi")
            
            for q_key, user_answer in user_answers.items():
                try:
                    # Lấy index từ key (ví dụ: "question_0" -> 0)
                    question_index = int(q_key.replace('question_', ''))
                    if 0 <= question_index < len(test_questions):
                        question = test_questions[question_index]
                        correct_answer = question.get('correct_answer')
                        is_correct = user_answer == correct_answer
                        
                        if is_correct:
                            correct_count += 1
                        
                        question_details.append({
                            'question_id': question.get('id'),
                            'question_text': question.get('question_text', ''),
                            'user_answer': user_answer,
                            'correct_answer': correct_answer,
                            'is_correct': is_correct,
                            'explanation': question.get('explanation', ''),
                            'options': question.get('options', [])
                        })
                except (ValueError, KeyError) as e:
                    print(f"⚠️ Lỗi xử lý câu hỏi {q_key}: {e}")
                    continue
            
            total_questions = len(test_questions)
            score = correct_count
            percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
            
            print(f"🎯 Kết quả: {score}/{total_questions} ({percentage:.1f}%)")
            
            # LƯU KẾT QUẢ
            try:
                result = SubjectTestResult.objects.create(
                    subject=subject_obj,
                    user_name=user_name,
                    score=score,
                    total_questions=total_questions,
                    percentage=percentage,
                    time_taken=time_taken,
                    question_details=json.dumps(question_details, ensure_ascii=False)
                )
                
                print(f"✅ Đã lưu kết quả: ID {result.id}")
                
                # FIX: Trả về JSON với redirect_url để frontend chuyển hướng
                return JsonResponse({
                    'success': True,
                    'result_id': result.id,
                    'score': score,
                    'total_questions': total_questions,
                    'percentage': round(percentage, 2),
                    'correct_answers': correct_count,
                    'time_taken': time_taken,
                    'redirect_url': f'/test-khoi/ket-qua/{result.id}/',  # URL đúng với pattern hiện tại
                    'message': 'Hoàn thành bài test!'
                })
                
            except Exception as e:
                print(f"❌ Lỗi khi lưu kết quả: {e}")
                return JsonResponse({
                    'success': False,
                    'error': 'Lỗi khi lưu kết quả. Vui lòng thử lại.'
                }, status=500)
            
        except Exception as e:
            print(f"❌ Lỗi khi xử lý kết quả: {e}")
            import traceback
            print("Chi tiết lỗi:", traceback.format_exc())
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

def subject_test_result(request, result_id):
    """Hiển thị kết quả bài test môn học - FIXED VERSION"""
    print(f"🎯 DEBUG: Vào subject_test_result với result_id = {result_id}")
    
    try:
        result = get_object_or_404(SubjectTestResult, id=result_id)
        print(f"🎯 DEBUG: Tìm thấy result - subject.code = {result.subject.code}")
        
        # Xác định block_code từ subject_code
        subject_code = result.subject.code
        if subject_code.startswith('A_'):
            block_code = 'khoi-A'
        elif subject_code.startswith('B_'):
            block_code = 'khoi-B' 
        elif subject_code.startswith('C_'):
            block_code = 'khoi-C'
        elif subject_code.startswith('D_'):
            block_code = 'khoi-D'
        elif subject_code.startswith('A01_'):
            block_code = 'khoi-A01'
        elif subject_code.startswith('B01_'):
            block_code = 'khoi-B01'
        elif subject_code.startswith('D07_'):
            block_code = 'khoi-D07'
        elif subject_code.startswith('B02_'):
            block_code = 'khoi-B02'
        elif subject_code.startswith('C01_'):
            block_code = 'khoi-C01'
        elif subject_code.startswith('D14_'):
            block_code = 'khoi-D14'
        elif subject_code.startswith('D15_'):
            block_code = 'khoi-D15'
        else:
            block_code = 'khoi-A'
        
        print(f"🎯 DEBUG: block_code = {block_code}")
        
        # Parse question_details từ JSON
        question_details = []
        if result.question_details:
            try:
                question_details = json.loads(result.question_details)
            except json.JSONDecodeError:
                question_details = []
        
        return render(request, 'testblock/subject_test_result.html', {
            'result': result,
            'question_details': question_details,
            'block_code': block_code,
            'title': f'Kết quả {result.subject.name}',
        })
        
    except Exception as e:
        print(f"❌ Lỗi khi hiển thị kết quả: {e}")
        import traceback
        traceback.print_exc()
        return render(request, 'testblock/error.html', {
            'message': 'Không thể hiển thị kết quả'
        })

def test_block_detail(request, block_id):
    """Chi tiết khối test"""
    test_block = get_object_or_404(TestBlock, id=block_id)
    questions = test_block.questions.all()
    
    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        user_answers = {}
        user_name = request.POST.get('user_name', '')
        
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            user_answers[question.id] = user_answer
            
            if user_answer == question.correct_answer:
                score += 1
        
        percentage = (score / total_questions) * 100 if total_questions > 0 else 0
        suggested_majors = suggest_majors_for_block(test_block.name, percentage)
        
        result = BlockTestResult.objects.create(
            test_block=test_block,
            user_name=user_name,
            score=score,
            total_questions=total_questions,
            percentage=percentage,
            suggested_majors=", ".join(suggested_majors)
        )
        
        request.session['user_answers'] = user_answers
        request.session['result_id'] = result.id
        
        return redirect('testblock:test_block_result', result_id=result.id)
    
    return render(request, 'testblock/test_block_detail.html', {
        'test_block': test_block,
        'questions': questions
    })

def test_block_result(request, result_id):
    """Kết quả khối test"""
    result = get_object_or_404(BlockTestResult, id=result_id)
    questions = result.test_block.questions.all()
    user_answers = request.session.get('user_answers', {})
    
    suggested_majors_list = result.suggested_majors.split(", ") if result.suggested_majors else []
    
    return render(request, 'testblock/test_block_result.html', {
        'result': result,
        'questions': questions,
        'user_answers': user_answers,
        'suggested_majors': suggested_majors_list,
        'title': f'Kết quả {result.test_block.name}'
    })

def test_block_result_detail(request, result_id):
    """Chi tiết kết quả khối test"""
    result = get_object_or_404(BlockTestResult, id=result_id)
    questions = result.test_block.questions.all()
    user_answers = request.session.get('user_answers', {})
    
    return render(request, 'testblock/test_block_result_detail.html', {
        'result': result,
        'questions': questions,
        'user_answers': user_answers,
        'title': f'Chi tiết kết quả {result.test_block.name}'
    })

def suggest_majors_for_block(block_name, percentage):
    """Gợi ý ngành học dựa trên khối và điểm số"""
    suggestions = {
        "Khối A": [
            {"name": "Công nghệ thông tin", "min_score": 70},
            {"name": "Kỹ thuật điện", "min_score": 60},
            {"name": "Cơ khí", "min_score": 50},
            {"name": "Xây dựng", "min_score": 40}
        ],
        "Khối B": [
            {"name": "Y dược", "min_score": 75},
            {"name": "Công nghệ sinh học", "min_score": 65},
            {"name": "Nông nghiệp", "min_score": 55},
            {"name": "Môi trường", "min_score": 45}
        ],
        "Khối C": [
            {"name": "Luật", "min_score": 70},
            {"name": "Báo chí", "min_score": 60},
            {"name": "Sư phạm", "min_score": 50},
            {"name": "Du lịch", "min_score": 40}
        ],
        "Khối D": [
            {"name": "Ngôn ngữ Anh", "min_score": 65},
            {"name": "Marketing", "min_score": 55},
            {"name": "Quan hệ quốc tế", "min_score": 45},
            {"name": "Tâm lý học", "min_score": 35}
        ]
    }
    
    suggested = []
    if block_name in suggestions:
        for major in suggestions[block_name]:
            if percentage >= major["min_score"]:
                suggested.append(major["name"])
    
    return suggested if suggested else ["Các ngành phù hợp với khối thi"]