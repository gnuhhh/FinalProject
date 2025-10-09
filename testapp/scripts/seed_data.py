from testapp.models import Major, Test, Question
import importlib
import os
import sys

# them thư mục test_data vào path để có thể import
sys.path.append(os.path.join(os.path.dirname(__file__), 'test_data'))

def run():
    # 10 majors
    majors = [
        ("Công nghệ thông tin", "Dành cho người có tư duy logic, yêu thích công nghệ."),
        ("Kinh tế", "Phù hợp với người phân tích, thích tài chính."),
        ("Marketing", "Dành cho người sáng tạo và giao tiếp tốt."),
        ("Ngôn ngữ Anh", "Cho người yêu ngôn ngữ, thích giao tiếp quốc tế."),
        ("Luật", "Phù hợp với người logic và công bằng."),
        ("Y dược", "Cho người tỉ mỉ, yêu giúp đỡ người khác."),
        ("Sư phạm", "Dành cho người kiên nhẫn và yêu giáo dục."),
        ("Kiến trúc", "Cho người sáng tạo và có óc thẩm mỹ."),
        ("Du lịch & Nhà hàng - Khách sạn", "Cho người năng động, thích khám phá."),
        ("Tâm lý học", "Dành cho người biết lắng nghe và quan tâm con người.")
    ]

    # Tiêu đề 3 bài test cho mỗi chuyên ngành (theo chủ điểm phù hợp)
    test_titles_by_major = {
        "Công nghệ thông tin": [
            "Kỹ năng Giải quyết Vấn đề & Tư duy Phản biện",
            "Kỹ năng Giao tiếp & Làm việc Nhóm", 
            "Kỹ năng Quản lý Thời gian & Học hỏi Liên tục"
        ],
        "Kinh tế": [
            "Phân tích dữ liệu & Tư duy chiến lược",
            "Giao tiếp thuyết phục & Trình bày",
            "Đạo đức kinh doanh & Quản trị rủi ro"
        ],
        "Marketing": [
            "Sáng tạo ý tưởng & Nội dung",
            "Nghiên cứu thị trường & Insight",
            "Chiến lược truyền thông tích hợp"
        ],
        "Ngôn ngữ Anh": [
            "Ngữ pháp & Từ vựng",
            "Đọc hiểu & Tư duy phản biện",
            "Giao tiếp & Viết học thuật"
        ],
        "Luật": [
            "Nhận định pháp lý & Lập luận",
            "Phân tích tình huống & Quy phạm",
            "Đạo đức nghề luật & Tố tụng"
        ],
        "Y dược": [
            "Kiến thức nền tảng & An toàn",
            "Lâm sàng cơ bản & Quy trình",
            "Đạo đức y khoa & Giao tiếp bệnh nhân"
        ],
        "Sư phạm": [
            "Tâm lý học giáo dục & Động lực",
            "Thiết kế bài giảng & Đánh giá",
            "Quản lý lớp học & Giao tiếp"
        ],
        "Kiến trúc": [
            "Tư duy thẩm mỹ & Hình khối",
            "Công năng & Bền vững",
            "Lịch sử kiến trúc & Bối cảnh"
        ],
        "Du lịch & Nhà hàng - Khách sạn": [
            "Dịch vụ khách hàng & Quy trình",
            "Văn hoá – điểm đến & Lịch trình",
            "An toàn, vệ sinh & Xử lý tình huống"
        ],
        "Tâm lý học": [
            "Kỹ năng Thấu hiểu & Đồng cảm",
            "Kỹ năng Phân tích & Đánh giá",
            "Kỹ năng Đạo đức & Giới hạn nghề nghiệp"
        ]
    }

    # Hàm load test data từ file riêng
    def load_test_data(major_name):
        """Tự động import file test data cho chuyên ngành"""
        try:
            # Map tên chuyên ngành sang tên file thực tế
            file_mapping = {
                "Công nghệ thông tin": "cong_nghe_thong_tin_tests",
                "Kinh tế": "kinh_te_tests", 
                "Marketing": "marketing_tests",
                "Ngôn ngữ Anh": "ngon_ngu_anh_tests",
                "Luật": "luat_tests",
                "Y dược": "y_duoc_tests",
                "Sư phạm": "su_pham_tests",
                "Kiến trúc": "kien_truc_tests",
                "Du lịch & Nhà hàng - Khách sạn": "du_lich_nha_hang_khach_san_tests",
                "Tâm lý học": "tam_ly_hoc_tests"
            }
            
            if major_name not in file_mapping:
                print(f"⚠️ Không có mapping cho: {major_name}")
                return {}
                
            module_name = file_mapping[major_name]
            print(f"🔍 Đang tìm file: {module_name}")
            
            module = importlib.import_module(module_name)
            
            # Tìm biến chứa questions (thử nhiều tên khác nhau)
            possible_names = [
                "questions",  # Tên đơn giản nhất
                "cong_nghe_thong_tin_questions",  # Cho CNTT
                "kinh_te_questions",  # Cho Kinh tế
                "marketing_questions",  # Cho Marketing
                "ngon_ngu_anh_questions",  # Cho Ngôn ngữ Anh
                "luat_questions",  # Cho Luật
                "y_duoc_questions",  # Cho Y dược
                "su_pham_questions",  # Cho Sư phạm
                "kien_truc_questions",  # Cho Kiến trúc
                "du_lich_nha_hang_khach_san_questions",  # Cho Du lịch
                "tam_ly_hoc_questions",  # Cho Tâm lý học
            ]
            
            for name in possible_names:
                if hasattr(module, name):
                    print(f"✅ Tìm thấy biến: {name} trong {module_name}")
                    return getattr(module, name)
            
            print(f"⚠️ Không tìm thấy biến questions trong {module_name}")
            return {}
            
        except ImportError as e:
            print(f"⚠️ Không thể import {module_name}: {e}")
            return {}
        except Exception as e:
            print(f"⚠️ Lỗi khi load test data cho {major_name}: {e}")
            return {}

    # Load test data cho tất cả chuyên ngành
    test_data_cache = {}
    for major_name, _ in majors:
        test_data_cache[major_name] = load_test_data(major_name)
        if test_data_cache[major_name]:
            print(f"✅ Đã load test data cho: {major_name}")

    # Mẫu câu hỏi theo chuyên ngành (dự phòng)
    def make_question_fallback(major, test_title, i):
        base = i % 5
        if major == "Công nghệ thông tin":
            stems = [
                f"Trong bối cảnh dự án phần mềm, bước phù hợp nhất ở vị trí {i} là gì?",
                f"Khi gặp lỗi phát sinh ở môi trường staging, hành động ưu tiên của bạn là gì?",
                f"Để nâng cao chất lượng mã, thực hành nào nên áp dụng trước?",
                f"Trong buổi họp sprint review, bạn cần tập trung điều gì?",
                f"Khi ước lượng task, yếu tố nào không nên bỏ qua?",
            ]
            options = [
                ("Viết thêm tính năng ngay", "Tái hiện và cô lập lỗi", "Bỏ qua và deploy", "Chờ người khác sửa"),
                ("Code review 4 mắt", "Không viết test", "Bỏ qua tài liệu", "Trì hoãn merge"),
                ("Chất lượng đầu ra", "Cảm xúc cá nhân", "May rủi", "Sở thích công nghệ"),
                ("Tiêu chí hoàn thành (DoD)", "Tám chuyện", "Trình bày dài dòng", "Tránh phản hồi"),
                ("Rủi ro kỹ thuật", "Đổi ngôn ngữ lập trình", "Mua thêm server", "Like trên mạng")
            ]
        elif major == "Kinh tế":
            stems = [
                f"Khi phân tích thị trường, chỉ số nào hữu ích ở vị trí {i}?",
                f"Trong đánh giá dự án, điều gì phản ánh rủi ro tốt nhất?",
                f"Đồ thị nào phù hợp để so sánh nhóm dữ liệu?",
                f"Để trình bày cho lãnh đạo, trọng tâm là gì?",
                f"Khi dự báo sai lệch, bước kiểm tra đầu tiên là gì?",
            ]
            options = [
                ("Doanh số, biên lợi nhuận", "Màu logo", "Tên công ty", "Meme đang hot"),
                ("Phân tích độ nhạy", "Chọn theo cảm tính", "Tin đồn", "Đếm like"),
                ("Biểu đồ cột", "Biểu đồ tròn", "Ảnh minh hoạ", "Đoạn văn"),
                ("Câu chuyện dữ liệu & khuyến nghị", "Slide nhiều chữ", "Thuật ngữ khó", "Ảnh động"),
                ("Kiểm tra giả định & dữ liệu", "Đổi phần mềm", "Đoán lại", "Bỏ qua lỗi")
            ]
        elif major == "Marketing":
            stems = [
                f"Thông điệp cốt lõi cho chiến dịch ở vị trí {i} nên tập trung vào gì?",
                f"Để tìm insight khách hàng, bạn ưu tiên nguồn nào?",
                f"Ở giai đoạn triển khai, chỉ số nào quan trọng nhất?",
                f"Khi phối hợp kênh, nguyên tắc nào tối ưu?",
                f"Cách tốt nhất để thử nghiệm ý tưởng nội dung?",
            ]
            options = [
                ("Lợi ích cho khách hàng", "Tính năng nội bộ", "Lịch sử công ty", "Khẩu hiệu dài"),
                ("Nghiên cứu định tính/định lượng", "Tin đồn", "Một bài viết lẻ", "Ý kiến chủ quan"),
                ("Mục tiêu/KPI đã định", "Số slide", "Số hashtag", "Độ dài caption"),
                ("Nhất quán thông điệp", "Thay đổi liên tục", "Ngẫu hứng", "Chạy đơn lẻ"),
                ("A/B testing có kiểm soát", "Đăng tuỳ hứng", "Spam bài", "Đổi brand voice")
            ]
        elif major == "Ngôn ngữ Anh":
            stems = [
                f"Chọn từ phù hợp nhất cho ngữ cảnh ở vị trí {i}.",
                f"Cách diễn đạt trang trọng nên dùng trong email là?",
                f"Trong đọc hiểu, điều gì giúp nắm ý chính nhanh?",
                f"Khi viết học thuật, yếu tố nào cần ưu tiên?",
                f"Để cải thiện phát âm, bạn nên làm gì?",
            ]
            options = [
                ("Collocation tự nhiên", "Dịch từng chữ", "Từ hiếm gặp", "Từ sai ngữ cảnh"),
                ("I would appreciate it if...", "Send me now", "Gimme", "Pls asap"),
                ("Skimming/Scanning", "Đoán mò", "Đọc ngẫu nhiên", "Bỏ tiêu đề"),
                ("Mạch lạc & trích dẫn", "Emoji nhiều", "Viết tắt", "Thiếu bằng chứng"),
                ("Luyện IPA & shadowing", "Học qua loa", "Chỉ nghe nhạc", "Không ghi âm")
            ]
        elif major == "Luật":
            stems = [
                f"Trong tình huống {i}, văn bản nào có hiệu lực pháp lý cao hơn?",
                f"Khi lập luận, điều gì giúp thuyết phục nhất?",
                f"Nhận định nào sau đây phù hợp nguyên tắc suy đoán vô tội?",
                f"Khi xung đột quy phạm, hướng xử lý?",
                f"Vấn đề đạo đức nghề luật cần ưu tiên?",
            ]
            options = [
                ("Luật/hiến pháp", "Blog cá nhân", "Tin đồn", "Mạng xã hội"),
                ("Dẫn chiếu quy phạm & án lệ", "Cảm xúc", "Uy tín cá nhân", "Số trang văn bản"),
                ("Bị cáo không phải chứng minh vô tội", "Bắt buộc nhận tội", "Không cần xét xử", "Dựa vào dư luận"),
                ("Áp dụng văn bản hiệu lực cao/hẹp hơn", "Bỏ qua hết", "Theo ý kiến cá nhân", "Bốc thăm"),
                ("Bảo mật & xung đột lợi ích", "Quảng cáo quá mức", "Lách luật", "Tặng quà trái phép")
            ]
        elif major == "Y dược":
            stems = [
                f"Quy tắc an toàn cơ bản khi thao tác ở vị trí {i} là?",
                f"Với bệnh sử mơ hồ, hành động nào phù hợp?",
                f"Nguyên tắc dùng thuốc hợp lý là gì?",
                f"Trong giao tiếp bệnh nhân, điều gì cần nhất?",
                f"Đạo đức y khoa yêu cầu?",
            ]
            options = [
                ("Rửa tay & vô khuẩn", "Bỏ găng tay", "Dùng chung kim", "Không cần khẩu trang"),
                ("Khai thác thêm & cận lâm sàng", "Đoán bừa", "Kê đơn ngay", "Bỏ qua"),
                ("Đúng thuốc – liều – đường – thời gian", "Tuỳ cảm tính", "Theo quảng cáo", "Theo lời đồn"),
                ("Lắng nghe & đồng cảm", "Vội vàng", "Tránh giải thích", "Dọa nạt"),
                ("Ưu tiên an toàn người bệnh", "Bí mật hồ sơ", "Nhận quà", "Bán thuốc ép buộc")
            ]
        elif major == "Sư phạm":
            stems = [
                f"Động lực học tập được tăng bằng cách nào ở vị trí {i}?",
                f"Khi thiết kế đánh giá, điều gì quan trọng nhất?",
                f"Quản lý lớp học hiệu quả nhờ?",
                f"Hỗ trợ học sinh yếu cần?",
                f"Giao tiếp với phụ huynh nên?",
            ]
            options = [
                ("Mục tiêu rõ & phản hồi", "Phạt nặng", "Bài tập vô hạn", "Không giải thích"),
                ("Phù hợp mục tiêu & rubrics", "Chỉ thi cuối kỳ", "Điểm tuỳ hứng", "Đề mơ hồ"),
                ("Nội quy nhất quán", "Phớt lờ", "Nổi nóng", "Chủ quan"),
                ("Kế hoạch cá nhân hoá", "Bỏ mặc", "Chê bai", "Tăng bài vô lý"),
                ("Tôn trọng & hợp tác", "Đổ lỗi", "Mập mờ", "Tránh liên hệ")
            ]
        elif major == "Kiến trúc":
            stems = [
                f"Nguyên tắc thẩm mỹ cơ bản áp dụng ở vị trí {i}?",
                f"Đảm bảo công năng không gian nhờ?",
                f"Yếu tố bền vững ưu tiên là?",
                f"Bố cục tổng thể nên chú ý?",
                f"Ảnh hưởng bối cảnh lịch sử giúp?",
            ]
            options = [
                ("Cân bằng – nhịp điệu – tương phản", "Tích thật nhiều chi tiết", "Màu ngẫu hứng", "Không cần tỉ lệ"),
                ("Khảo sát nhu cầu sử dụng", "Theo ý thích", "Giảm lối đi", "Bỏ thông gió"),
                ("Vật liệu & năng lượng", "Sơn nhiều lớp", "Kính toàn bộ", "Không cách nhiệt"),
                ("Trục – điểm nhấn – dòng chảy", "Tùy tiện", "Bịt kín", "Cắt vụn"),
                ("Tạo bản sắc & phù hợp", "Sao chép vô tội vạ", "Bỏ qua văn hoá", "Ngẫu hứng")
            ]
        elif major == "Du lịch & Nhà hàng - Khách sạn":
            stems = [
                f"Chuẩn dịch vụ cơ bản với khách ở vị trí {i}?",
                f"Lập lịch trình tour cần ưu tiên?",
                f"An toàn & vệ sinh yêu cầu?",
                f"Xử lý phàn nàn hiệu quả bằng?",
                f"Giao tiếp đa văn hoá nên?",
            ]
            options = [
                ("Chào hỏi – lắng nghe – hỗ trợ", "Phớt lờ", "Tranh cãi", "Đùn đẩy"),
                ("Cân đối thời gian & trải nghiệm", "Nhồi nhét điểm đến", "Bỏ thời gian nghỉ", "Không kiểm tra đường"),
                ("Quy trình & tiêu chuẩn", "Làm theo cảm tính", "Giảm bước", "Bỏ sát khuẩn"),
                ("Xin lỗi – giải pháp – theo dõi", "Đổ lỗi", "Bỏ qua", "Chờ khách tự hết giận"),
                ("Tôn trọng khác biệt", "Áp đặt", "Đùa quá trớn", "Ngôn ngữ khó")
            ]
        elif major == "Tâm lý học":
            stems = [
                f"Khái niệm nền tảng phù hợp ở vị trí {i}?",
                f"Trong đánh giá, cần chú trọng?",
                f"Liên hệ giữa hành vi & nhận thức?",
                f"Thực hành đạo đức yêu cầu?",
                f"Kỹ năng tham vấn quan trọng?",
            ]
            options = [
                ("Điều kiện hoá – củng cố", "Tiên tri", "Mê tín", "Suy đoán vô căn"),
                ("Độ tin cậy – giá trị đo", "Ấn tượng", "Đoán ý", "Số câu hỏi ít"),
                ("Ảnh hưởng hai chiều", "Một chiều", "Không liên hệ", "Ngẫu nhiên"),
                ("Bảo mật – đồng ý tham gia", "Chia sẻ tự do", "Ép buộc", "Bỏ ghi chép"),
                ("Lắng nghe chủ động", "Cắt lời", "Đánh giá phán xét", "Áp đặt giải pháp")
            ]
        else:
            stems = [f"Câu hỏi tổng quát số {i}", f"Nội dung tình huống số {i}", f"Khái niệm liên quan số {i}", f"Ứng dụng thực tiễn số {i}", f"Nhận định đúng sai số {i}"]
            options = [("A", "B", "C", "D")] * 5

        stem = stems[base]
        A, B, C, D = options[base]
        return stem, A, B, C, D

    # Đáp án đúng theo chu kỳ A→B→C→D lặp lại
    def correct_letter(i):
        return "ABCD"[(i - 1) % 4]

    # Xoá dữ liệu cũ
    Question.objects.all().delete()
    Test.objects.all().delete()
    Major.objects.all().delete()

    # Tạo majors
    major_objs = {}
    for name, desc in majors:
        major_objs[name] = Major.objects.create(name=name, description=desc)

    # Tạo 3 bài test × 30 câu cho mỗi chuyên ngành
    for major_name, _ in majors:
        titles = test_titles_by_major[major_name]
        for t_index, t_title in enumerate(titles, start=1):
            test = Test.objects.create(
                title=f"{major_name} - {t_title}",
                major=major_objs[major_name],
                num_questions=30
            )
            
            # Kiểm tra xem có test data từ file không
            has_custom_data = (major_name in test_data_cache and 
                             test_data_cache[major_name] and 
                             t_title in test_data_cache[major_name])
            
            if has_custom_data:
                print(f"✅ Sử dụng custom data cho: {major_name} - {t_title}")
            
            for i in range(1, 31):
                if has_custom_data:
                    # Lấy câu hỏi từ file custom
                    questions_list = test_data_cache[major_name][t_title]
                    q_index = (i - 1) % len(questions_list)
                    q_data = questions_list[q_index]
                    stem = q_data["text"]
                    A, B, C, D = q_data["options"]
                    correct = q_data["correct"]
                else:
                    # Dùng fallback
                    stem, A, B, C, D = make_question_fallback(major_name, t_title, i)
                    correct = correct_letter(i)
                
                Question.objects.create(
                    test=test,
                    text=stem,
                    option_a=A,
                    option_b=B,
                    option_c=C,
                    option_d=D,
                    correct_answer=correct
                )

    print("✅ Đã tạo 10 chuyên ngành × 3 bài test × 30 câu hoàn tất!")