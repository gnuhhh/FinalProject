import os
import sys
import django
import importlib.util

# Thêm path đến thư mục gốc project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')
django.setup()

from testblock.models import TestBlock, BlockQuestion as Question, Subject


def load_module_from_file(file_path, module_name):
    """Load module từ file path"""
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"❌ Lỗi load module {module_name}: {e}")
        return None


def import_subject_modules():
    """Import các module môn học từ thư mục test_data"""
    test_data_path = os.path.join(BASE_DIR, 'testblock', 'scripts', 'test_data')
    print(f"📁 Đang tìm thư mục test_data: {test_data_path}")
    
    if not os.path.exists(test_data_path):
        print(f"❌ Thư mục test_data không tồn tại: {test_data_path}")
        return {}
    
    print("📂 Các file trong thư mục test_data:")
    for file in os.listdir(test_data_path):
        print(f"   - {file}")
    
    modules = {}
    subject_files = {
        'toan': 'toan.py',
        'vat_ly': 'vat_ly.py', 
        'hoa': 'hoa.py',
        'sinh_hoc': 'sinh_hoc.py',
        'van': 'van.py',
        'tieng_anh': 'tieng_anh.py',
        'lich_su': 'lich_su.py',
        'dia_ly': 'dia_ly.py'
    }
    
    for subject_name, filename in subject_files.items():
        file_path = os.path.join(test_data_path, filename)
        if os.path.exists(file_path):
            print(f"🔍 Đang load {filename}...")
            module = load_module_from_file(file_path, subject_name)
            if module:
                modules[subject_name] = module
                print(f"✅ Đã load thành công: {filename}")
            else:
                print(f"❌ Không thể load: {filename}")
        else:
            print(f"⚠️  File không tồn tại: {filename}")
    
    return modules


def create_subjects():
    """Tạo các môn học theo định nghĩa trong models.py"""
    # 🟢 SỬA: Tạo đúng các mã môn học theo SUBJECT_CHOICES trong models.py
    subject_mapping = {
        'A_TOAN': {'name': 'Toán học', 'code': 'A_TOAN'},
        'A_LY': {'name': 'Vật lý', 'code': 'A_LY'},
        'A_HOA': {'name': 'Hóa học', 'code': 'A_HOA'},
        'B_TOAN': {'name': 'Toán học', 'code': 'B_TOAN'},
        'B_HOA': {'name': 'Hóa học', 'code': 'B_HOA'},
        'B_SINH': {'name': 'Sinh học', 'code': 'B_SINH'},
        'C_VAN': {'name': 'Ngữ văn', 'code': 'C_VAN'},
        'C_SU': {'name': 'Lịch sử', 'code': 'C_SU'},
        'C_DIA': {'name': 'Địa lý', 'code': 'C_DIA'},
        'D_TOAN': {'name': 'Toán học', 'code': 'D_TOAN'},
        'D_VAN': {'name': 'Ngữ văn', 'code': 'D_VAN'},
        'D_TA': {'name': 'Tiếng Anh', 'code': 'D_TA'},
        'A01_TOAN': {'name': 'Toán học', 'code': 'A01_TOAN'},
        'A01_LY': {'name': 'Vật lý', 'code': 'A01_LY'},
        'A01_TA': {'name': 'Tiếng Anh', 'code': 'A01_TA'},
        'B01_TOAN': {'name': 'Toán học', 'code': 'B01_TOAN'},
        'B01_HOA': {'name': 'Hóa học', 'code': 'B01_HOA'},
        'B01_TA': {'name': 'Tiếng Anh', 'code': 'B01_TA'},
        'D07_TOAN': {'name': 'Toán học', 'code': 'D07_TOAN'},
        'D07_HOA': {'name': 'Hóa học', 'code': 'D07_HOA'},
        'D07_TA': {'name': 'Tiếng Anh', 'code': 'D07_TA'},
        'B02_TOAN': {'name': 'Toán học', 'code': 'B02_TOAN'},
        'B02_SINH': {'name': 'Sinh học', 'code': 'B02_SINH'},
        'B02_DIA': {'name': 'Địa lý', 'code': 'B02_DIA'},
        'C01_VAN': {'name': 'Ngữ văn', 'code': 'C01_VAN'},
        'C01_TOAN': {'name': 'Toán học', 'code': 'C01_TOAN'},
        'C01_LY': {'name': 'Vật lý', 'code': 'C01_LY'},
        'D14_VAN': {'name': 'Ngữ văn', 'code': 'D14_VAN'},
        'D14_LS': {'name': 'Lịch sử', 'code': 'D14_LS'},
        'D14_TA': {'name': 'Tiếng Anh', 'code': 'D14_TA'},
        'D15_VAN': {'name': 'Ngữ văn', 'code': 'D15_VAN'},
        'D15_DIA': {'name': 'Địa lý', 'code': 'D15_DIA'},
        'D15_TA': {'name': 'Tiếng Anh', 'code': 'D15_TA'}
    }
    
    subjects = {}
    for code, data in subject_mapping.items():
        try:
            subject, created = Subject.objects.get_or_create(
                code=code,
                defaults={
                    'name': data['name'],
                    'description': f'Môn {data["name"]}',
                    'time_limit': 90,
                    'total_questions': 50
                }
            )
            subjects[code] = subject
            if created:
                print(f"✅ Đã tạo môn: {data['name']} ({code})")
            else:
                print(f"📚 Môn đã tồn tại: {data['name']} ({code})")
        except Exception as e:
            print(f"❌ Lỗi khi tạo môn {data['name']}: {e}")
    
    return subjects


def run():
    print("🎯 Đang tạo dữ liệu Test Khối từ câu hỏi thực...")

    # Tạo các môn học trước
    subjects = create_subjects()

    # Import các module môn học
    subject_modules = import_subject_modules()

    if not subject_modules:
        print("❌ Không thể load bất kỳ module môn học nào!")
        return

    print(f"✅ Đã load thành công {len(subject_modules)} module môn học")

    # Xóa dữ liệu cũ
    Question.objects.all().delete()
    TestBlock.objects.all().delete()

    # 🟢 SỬA: Sử dụng đúng subject_code thay vì subject_key
    test_blocks = {
        "Khối A": {
            "description": "Toán - Lý - Hóa",
            "subjects": [
                {"module_key": "toan", "subject_code": "A_TOAN", "name": "Toán học"},
                {"module_key": "vat_ly", "subject_code": "A_LY", "name": "Vật lý"},
                {"module_key": "hoa", "subject_code": "A_HOA", "name": "Hóa học"}
            ],
            "questions_per_subject": 50
        },
        "Khối A1": {
            "description": "Toán - Lý - Anh", 
            "subjects": [
                {"module_key": "toan", "subject_code": "A01_TOAN", "name": "Toán học"},
                {"module_key": "vat_ly", "subject_code": "A01_LY", "name": "Vật lý"},
                {"module_key": "tieng_anh", "subject_code": "A01_TA", "name": "Tiếng Anh"}
            ],
            "questions_per_subject": 50
        },
        "Khối B": {
            "description": "Toán - Hóa - Sinh",
            "subjects": [
                {"module_key": "toan", "subject_code": "B_TOAN", "name": "Toán học"},
                {"module_key": "hoa", "subject_code": "B_HOA", "name": "Hóa học"},
                {"module_key": "sinh_hoc", "subject_code": "B_SINH", "name": "Sinh học"}
            ],
            "questions_per_subject": 50
        },
        "Khối C": {
            "description": "Văn - Sử - Địa",
            "subjects": [
                {"module_key": "van", "subject_code": "C_VAN", "name": "Ngữ văn"},
                {"module_key": "lich_su", "subject_code": "C_SU", "name": "Lịch sử"},
                {"module_key": "dia_ly", "subject_code": "C_DIA", "name": "Địa lý"}
            ],
            "questions_per_subject": 50
        },
        "Khối D": {
            "description": "Toán - Văn - Anh",
            "subjects": [
                {"module_key": "toan", "subject_code": "D_TOAN", "name": "Toán học"},
                {"module_key": "van", "subject_code": "D_VAN", "name": "Ngữ văn"},
                {"module_key": "tieng_anh", "subject_code": "D_TA", "name": "Tiếng Anh"}
            ],
            "questions_per_subject": 50
        },
        # THÊM CÁC KHỐI MỚI
        "Khối B01": {
            "description": "Toán - Hóa - Anh",
            "subjects": [
                {"module_key": "toan", "subject_code": "B01_TOAN", "name": "Toán học"},
                {"module_key": "hoa", "subject_code": "B01_HOA", "name": "Hóa học"},
                {"module_key": "tieng_anh", "subject_code": "B01_TA", "name": "Tiếng Anh"}
            ],
            "questions_per_subject": 50
        },
        "Khối D07": {
            "description": "Toán - Hóa - Anh",
            "subjects": [
                {"module_key": "toan", "subject_code": "D07_TOAN", "name": "Toán học"},
                {"module_key": "hoa", "subject_code": "D07_HOA", "name": "Hóa học"},
                {"module_key": "tieng_anh", "subject_code": "D07_TA", "name": "Tiếng Anh"}
            ],
            "questions_per_subject": 50
        },
        "Khối B02": {
            "description": "Toán - Sinh - Địa",
            "subjects": [
                {"module_key": "toan", "subject_code": "B02_TOAN", "name": "Toán học"},
                {"module_key": "sinh_hoc", "subject_code": "B02_SINH", "name": "Sinh học"},
                {"module_key": "dia_ly", "subject_code": "B02_DIA", "name": "Địa lý"}
            ],
            "questions_per_subject": 50
        },
        "Khối C01": {
            "description": "Văn - Toán - Lý",
            "subjects": [
                {"module_key": "van", "subject_code": "C01_VAN", "name": "Ngữ văn"},
                {"module_key": "toan", "subject_code": "C01_TOAN", "name": "Toán học"},
                {"module_key": "vat_ly", "subject_code": "C01_LY", "name": "Vật lý"}
            ],
            "questions_per_subject": 50
        },
        "Khối D14": {
            "description": "Văn - Sử - Anh",
            "subjects": [
                {"module_key": "van", "subject_code": "D14_VAN", "name": "Ngữ văn"},
                {"module_key": "lich_su", "subject_code": "D14_LS", "name": "Lịch sử"},
                {"module_key": "tieng_anh", "subject_code": "D14_TA", "name": "Tiếng Anh"}
            ],
            "questions_per_subject": 50
        },
        "Khối D15": {
            "description": "Văn - Địa - Anh",
            "subjects": [
                {"module_key": "van", "subject_code": "D15_VAN", "name": "Ngữ văn"},
                {"module_key": "dia_ly", "subject_code": "D15_DIA", "name": "Địa lý"},
                {"module_key": "tieng_anh", "subject_code": "D15_TA", "name": "Tiếng Anh"}
            ],
            "questions_per_subject": 50
        }
    }

    # Tạo test block và import câu hỏi
    for block_name, block_info in test_blocks.items():
        test_block = TestBlock.objects.create(
            name=block_name,
            description=block_info["description"],
            num_questions=block_info["questions_per_subject"] * len(block_info["subjects"])
        )
        print(f"\n✅ Đã tạo: {block_name}")

        total_questions = 0
        for subject_info in block_info["subjects"]:
            module_key = subject_info["module_key"]
            subject_code = subject_info["subject_code"]  # 🟢 SỬA: dùng subject_code
            
            if module_key in subject_modules and subject_code in subjects:
                questions_imported = import_questions_for_subject(
                    test_block, 
                    subject_modules[module_key],
                    subjects[subject_code],  # 🟢 SỬA: truyền subject_code
                    subject_info["name"],
                    block_info["questions_per_subject"]
                )
                total_questions += questions_imported
                print(f"   📚 {subject_info['name']}: {questions_imported} câu hỏi")
            else:
                print(f"   ❌ Không tìm thấy module hoặc subject cho: {subject_info['name']}")

        print(f"✅ {block_name}: Tổng cộng {total_questions} câu hỏi")

    print("\n🎯 Đã tạo dữ liệu Test Khối hoàn tất!")


def import_questions_for_subject(test_block, question_module, subject, subject_name, num_questions):
    """Import câu hỏi từ module vào database"""
    try:
        questions_data = None
        possible_attrs = [
            'toan_questions', 'vat_ly_questions', 'hoa_questions',
            'sinh_hoc_questions', 'van_questions', 'tieng_anh_questions',
            'lich_su_questions', 'dia_ly_questions', 'questions', 'data',
            'question_list', 'quiz_data'
        ]

        for attr in possible_attrs:
            if hasattr(question_module, attr):
                questions_data = getattr(question_module, attr)
                print(f"   ✅ Tìm thấy biến: {attr} với {len(questions_data) if questions_data else 0} câu hỏi")
                break

        if not questions_data:
            print(f"   ⚠️  Không tìm thấy dữ liệu câu hỏi trong module {subject_name}")
            return 0

        if not isinstance(questions_data, list):
            print(f"   ⚠️  Dữ liệu không phải list: {type(questions_data)}")
            return 0

        questions_created = 0
        max_questions = min(num_questions, len(questions_data))

        print(f"   📝 Đang import {max_questions} câu hỏi...")

        for i in range(max_questions):
            q_data = questions_data[i]

            if not isinstance(q_data, dict):
                print(f"   ⚠️  Câu hỏi {i} không phải dictionary: {type(q_data)}")
                continue

            question_text = None
            options = []
            correct_answer = None

            if 'cau_hoi' in q_data and 'lua_chon' in q_data and 'dap_an' in q_data:
                question_text = q_data['cau_hoi']
                lua_chon = q_data['lua_chon']

                if isinstance(lua_chon, dict):
                    options = [
                        lua_chon.get('A', ''),
                        lua_chon.get('B', ''),
                        lua_chon.get('C', ''),
                        lua_chon.get('D', '')
                    ]
                correct_answer = q_data['dap_an']

            elif 'question' in q_data and 'options' in q_data and 'answer' in q_data:
                question_text = q_data['question']
                options = q_data['options']
                correct_answer = q_data['answer']

            else:
                print(f"   ⚠️  Câu hỏi {i} có cấu trúc không hợp lệ: {q_data.keys()}")
                continue

            if not question_text or len(options) < 4 or not correct_answer:
                print(f"   ⚠️  Câu hỏi {i} thiếu dữ liệu")
                continue

            # 🟢 BỎ KIỂM TRA TRÙNG LẶP để import tất cả câu hỏi
            Question.objects.create(
                test_block=test_block,
                subject=subject,
                text=question_text,
                option_a=options[0] if len(options) > 0 else '',
                option_b=options[1] if len(options) > 1 else '',
                option_c=options[2] if len(options) > 2 else '',
                option_d=options[3] if len(options) > 3 else '',
                correct_answer=correct_answer
            )
            questions_created += 1

        return questions_created

    except Exception as e:
        print(f"   ❌ Lỗi khi import câu hỏi cho {subject_name}: {str(e)}")
        import traceback
        traceback.print_exc()
        return 0


if __name__ == '__main__':
    run()