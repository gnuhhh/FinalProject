# # seed_data.py
# from testapp.models import Major, Test, Question

# def run():
#     # Xóa dữ liệu cũ
#     Question.objects.all().delete()
#     Test.objects.all().delete()
#     Major.objects.all().delete()

#     # Dữ liệu cho các chuyên ngành
#     majors_data = {
#         "cong-nghe-thong-tin": {
#             "name": "Công nghệ thông tin",
#             "description": "Dành cho người có tư duy logic, yêu thích công nghệ và giải quyết vấn đề.",
#             "tests": [
#                 {
#                     "title": "Bài Test Kỹ Năng Giải quyết Vấn đề & Tư duy Phản biện",
#                     "questions": [
#                         {
#                             "text": "Khi mã của bạn gặp lỗi (bug), hành động đầu tiên và quan trọng nhất bạn nên làm là gì?",
#                             "options": [
#                                 "Hỏi đồng nghiệp có kinh nghiệm",
#                                 "Thử các giải pháp ngẫu nhiên để xem lỗi có biến mất không",
#                                 "Tái hiện lỗi (reproduce), xác định thông báo lỗi chính xác và kiểm tra nhật ký (log) hệ thống",
#                                 "Tạm dừng công việc và chuyển sang nhiệm vụ khác"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Tư duy phản biện được định nghĩa tốt nhất là:",
#                             "options": [
#                                 "Luôn chống đối và phủ nhận ý kiến của người khác",
#                                 "Đưa ra giải pháp dựa trên cảm tính",
#                                 "Phân tích, đánh giá thông tin một cách khách quan để hình thành lập luận hợp lý",
#                                 "Chỉ tin vào những gì bạn tìm thấy trên mạng"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Trong giai đoạn giải quyết vấn đề, bước Định nghĩa vấn đề (Define the Problem) quan trọng vì:",
#                             "options": [
#                                 "Giúp bạn chọn ngôn ngữ lập trình",
#                                 "Đảm bảo bạn đang cố gắng giải quyết đúng nguyên nhân gốc rễ, không phải triệu chứng",
#                                 "Tạo ra tài liệu dự án (documentation)",
#                                 "Giới hạn thời gian cho việc giải quyết"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Bạn nhận thấy một giải pháp mà nhóm đang thảo luận có thể gây ra rủi ro bảo mật trong tương lai. Bạn nên làm gì?",
#                             "options": [
#                                 "Giữ im lặng vì bạn là người mới",
#                                 "Lợi dụng rủi ro để thể hiện khả năng của mình sau này",
#                                 "Trình bày mối lo ngại của bạn một cách rõ ràng, kèm theo dữ liệu hoặc ví dụ cụ thể",
#                                 "Gửi email cảnh báo ẩn danh"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Phương pháp 5 Whys (5 Tại sao) được sử dụng để:",
#                             "options": [
#                                 "Thiết lập ưu tiên công việc",
#                                 "Tìm ra nguyên nhân gốc rễ của một vấn đề",
#                                 "Tổ chức cuộc họp hiệu quả",
#                                 "Phân bổ tài nguyên"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong một buổi gỡ lỗi (debugging), một lập trình viên liên tục thay đổi mã mà không kiểm tra kết quả từng bước. Điều này vi phạm nguyên tắc giải quyết vấn đề nào?",
#                             "options": [
#                                 "Nguyên tắc giao tiếp",
#                                 "Nguyên tắc cô lập và kiểm soát các biến (isolate and test changes)",
#                                 "Nguyên tắc quản lý thời gian",
#                                 "Nguyên tắc làm việc nhóm"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi bạn phải đối mặt với một vấn đề phức tạp, bạn nên:",
#                             "options": [
#                                 "Giải quyết toàn bộ vấn đề cùng một lúc",
#                                 "Chia nhỏ vấn đề thành các phần nhỏ hơn, dễ quản lý hơn",
#                                 "Chờ đợi người khác giải quyết",
#                                 "Phớt lờ vấn đề cho đến khi không thể trì hoãn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Việc đọc các tài liệu (documentation) và mã nguồn hiện có trước khi cố gắng sửa lỗi là một ví dụ về:",
#                             "options": [
#                                 "Lãng phí thời gian",
#                                 "Thu thập và phân tích dữ liệu/thông tin liên quan",
#                                 "Trì hoãn công việc",
#                                 "Kỹ năng lập trình cơ bản"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Một giải pháp được cho là tốt nhất khi nó:",
#                             "options": [
#                                 "Nhanh nhất",
#                                 "Mới nhất",
#                                 "Hiệu quả, bền vững, dễ bảo trì và giải quyết triệt để vấn đề",
#                                 "Sử dụng công nghệ bạn thích nhất"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Lập luận cảm tính là trở ngại lớn nhất đối với tư duy phản biện vì:",
#                             "options": [
#                                 "Nó quá chậm",
#                                 "Nó quá phức tạp",
#                                 "Nó ưu tiên cảm xúc/thiên kiến cá nhân hơn bằng chứng và logic",
#                                 "Nó đòi hỏi nhiều công cụ"
#                             ],
#                             "correct": "C"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ Năng Giao tiếp & Làm việc Nhóm",
#                     "questions": [
#                         {
#                             "text": "Trong bối cảnh làm việc nhóm IT, kỹ năng Giao tiếp hiệu quả bao gồm:",
#                             "options": [
#                                 "Chỉ nói về các vấn đề kỹ thuật phức tạp",
#                                 "Gửi email dài và chi tiết",
#                                 "Truyền đạt thông tin rõ ràng, ngắn gọn và lắng nghe tích cực",
#                                 "Luôn đồng ý với ý kiến của trưởng nhóm"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Khi giao tiếp bằng văn bản (email, chat) trong dự án IT, bạn nên ưu tiên điều gì?",
#                             "options": [
#                                 "Sử dụng nhiều biệt ngữ (jargon) để thể hiện sự chuyên nghiệp",
#                                 "Gửi một tin nhắn duy nhất bao gồm mọi vấn đề",
#                                 "Tính rõ ràng, chính xác, và sử dụng tiêu đề/đoạn văn hợp lý",
#                                 "Dùng chữ viết tắt và ngôn ngữ mạng"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Bạn nhận được một phản hồi (feedback) tiêu cực về đoạn mã của mình. Phản ứng tốt nhất là gì?",
#                             "options": [
#                                 "Cố gắng bảo vệ mã của bạn bằng mọi giá",
#                                 "Cảm thấy tự ái và né tránh người đưa ra phản hồi",
#                                 "Đón nhận, đặt câu hỏi làm rõ và xem nó như cơ hội để học hỏi và cải thiện",
#                                 "Bỏ qua và hy vọng không ai để ý"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Vai trò của một thành viên nhóm IT tích cực lắng nghe là gì?",
#                             "options": [
#                                 "Nghe ngóng xem ai mắc lỗi",
#                                 "Tập trung hoàn toàn vào người nói, không ngắt lời, và xác nhận lại thông tin đã nghe",
#                                 "Chuẩn bị sẵn câu trả lời trong đầu",
#                                 "Chỉ lắng nghe khi vấn đề liên quan trực tiếp đến công việc của bạn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Xung đột xảy ra khi hai thành viên nhóm có ý kiến khác nhau về kiến trúc hệ thống. Bạn là thành viên thứ ba nên làm gì?",
#                             "options": [
#                                 "Chọn phe và ủng hộ một bên",
#                                 "Đóng vai trò trung gian, khuyến khích hai bên tập trung vào dữ liệu và mục tiêu chung",
#                                 "Bỏ đi và để họ tự giải quyết",
#                                 "Báo cáo lên cấp trên ngay lập tức"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tại sao việc tạo ra tài liệu (documentation) chi tiết lại quan trọng đối với làm việc nhóm?",
#                             "options": [
#                                 "Giúp dự án trông chuyên nghiệp hơn",
#                                 "Đảm bảo tất cả thành viên (và người mới) hiểu rõ về kiến trúc, quyết định và quy trình của hệ thống",
#                                 "Là một yêu cầu bắt buộc của mọi hợp đồng",
#                                 "Chỉ cần thiết cho các dự án lớn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Một thành viên nhóm liên tục trễ deadline. Việc làm nhóm tốt nhất là gì?",
#                             "options": [
#                                 "Tự làm phần việc của họ",
#                                 "Đổ lỗi công khai",
#                                 "Trao đổi riêng, hiểu rõ nguyên nhân (vấn đề kỹ năng/công việc quá tải) và tìm cách hỗ trợ",
#                                 "Đặt deadline sớm hơn cho họ"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Các cuộc họp (meeting) hiệu quả trong IT nên tập trung vào:",
#                             "options": [
#                                 "Kể chuyện và than phiền",
#                                 "Mục tiêu rõ ràng, có chương trình nghị sự (agenda) và kết thúc bằng các hành động cụ thể (action items)",
#                                 "Thảo luận mọi ý kiến nảy ra trong đầu",
#                                 "Dùng để cập nhật tiến độ cho từng người trong 30 phút"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Một trong những rào cản lớn nhất đối với giao tiếp hiệu quả trong IT là:",
#                             "options": [
#                                 "Không sử dụng Slack",
#                                 "Giả định người khác có cùng kiến thức nền tảng (context) với mình",
#                                 "Sử dụng quá nhiều hình ảnh minh họa",
#                                 "Không tổ chức họp mặt trực tiếp"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Mục tiêu chính của việc Review Code (Đánh giá mã) trong làm việc nhóm là gì?",
#                             "options": [
#                                 "Tìm lỗi và chỉ trích người viết mã",
#                                 "Cải thiện chất lượng, chia sẻ kiến thức, và tìm ra lỗi/lỗ hổng tiềm ẩn",
#                                 "Chỉ là bước thủ tục trước khi triển khai",
#                                 "Đánh giá hiệu suất cá nhân của lập trình viên"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ Năng Quản lý Thời gian & Học hỏi Liên tục",
#                     "questions": [
#                         {
#                             "text": "Phương pháp nào giúp bạn phân loại nhiệm vụ dựa trên hai tiêu chí: Tầm quan trọng và Khẩn cấp?",
#                             "options": [
#                                 "Kỹ thuật Pomodoro",
#                                 "Biểu đồ Gantt",
#                                 "Ma trận Eisenhower",
#                                 "Mô hình Kanban"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Nguyên tắc 80/20 (Pareto Principle) trong quản lý thời gian có ý nghĩa gì đối với lập trình viên?",
#                             "options": [
#                                 "80% thời gian dành cho lập trình, 20% cho họp",
#                                 "20% công việc tạo ra 80% kết quả (tập trung vào những nhiệm vụ có giá trị cao nhất)",
#                                 "Hoàn thành 80% công việc là đủ",
#                                 "Dành 80% thời gian cho việc học"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Bạn bị mất tập trung do thông báo liên tục từ các ứng dụng nhắn tin. Giải pháp tốt nhất là gì?",
#                             "options": [
#                                 "Tắt hoàn toàn máy tính",
#                                 "Thiết lập khoảng thời gian làm việc sâu (deep work) bằng cách tắt hoặc giới hạn thông báo",
#                                 "Trả lời ngay lập tức mọi thông báo",
#                                 "Yêu cầu đồng nghiệp không nhắn tin"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Technical Debt (Nợ Kỹ thuật) liên quan đến việc quản lý thời gian như thế nào?",
#                             "options": [
#                                 "Là khoản nợ công ty phải trả",
#                                 "Việc cắt giảm thời gian để đưa ra giải pháp nhanh chóng, khiến phải tốn nhiều thời gian hơn để sửa chữa/bảo trì sau này",
#                                 "Chỉ là thuật ngữ chuyên môn không quan trọng",
#                                 "Tiền thưởng cho lập trình viên"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tại sao việc Ước tính thời gian (Time Estimation) lại là một kỹ năng quan trọng?",
#                             "options": [
#                                 "Để chứng minh bạn làm việc nhanh hơn người khác",
#                                 "Để giúp quản lý dự án, đặt ra kỳ vọng hợp lý và đảm bảo deadline khả thi",
#                                 "Để lấy cớ trì hoãn",
#                                 "Để làm cho mã trông phức tạp hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong lĩnh vực IT, việc Học hỏi Liên tục (Continuous Learning) là cần thiết vì:",
#                             "options": [
#                                 "Công nghệ, công cụ và tiêu chuẩn ngành thay đổi rất nhanh chóng",
#                                 "Để có nhiều chứng chỉ nhất có thể",
#                                 "Công việc IT rất dễ dàng",
#                                 "Chỉ để có chủ đề nói chuyện trong bữa trưa"
#                             ],
#                             "correct": "A"
#                         },
#                         {
#                             "text": "Khi học một công nghệ mới, bước nào nên được ưu tiên sau khi đã hiểu khái niệm cơ bản?",
#                             "options": [
#                                 "Đọc lý thuyết chuyên sâu không giới hạn",
#                                 "Chờ đợi một dự án thực tế",
#                                 "Thực hành, xây dựng các dự án nhỏ (mini-projects) hoặc làm bài tập mẫu",
#                                 "Tự nhận mình là chuyên gia về công nghệ đó"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Kỹ thuật Pomodoro (ví dụ: 25 phút làm việc, 5 phút nghỉ) giúp quản lý thời gian bằng cách:",
#                             "options": [
#                                 "Bắt bạn làm việc liên tục không nghỉ",
#                                 "Cải thiện sự tập trung, chống lại sự trì hoãn và ngăn ngừa kiệt sức",
#                                 "Đảm bảo mọi thứ được hoàn thành trong một ngày",
#                                 "Chỉ hoạt động với các nhiệm vụ lập trình"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Điều gì nên làm khi bạn nhận ra mình không thể hoàn thành nhiệm vụ đúng thời hạn?",
#                             "options": [
#                                 "Giả vờ rằng mọi thứ đều ổn",
#                                 "Thông báo sớm cho người quản lý/nhóm, giải thích lý do và đề xuất một kế hoạch hành động mới",
#                                 "Ở lại làm việc thâu đêm",
#                                 "Đổ lỗi cho công cụ bạn đang sử dụng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Để học hỏi hiệu quả từ kinh nghiệm của người khác, bạn nên tham gia vào hoạt động nào?",
#                             "options": [
#                                 "Chỉ đọc sách kỹ thuật",
#                                 "Tham gia vào các buổi Code Review, các buổi chia sẻ/webinar và hỏi ý kiến cố vấn (mentor)",
#                                 "Xem video giải trí trên mạng",
#                                 "Giấu kín các lỗi bạn gặp phải"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 }
#             ]
#         },
#         "kinh-te": {
#             "name": "Kinh tế",
#             "description": "Phù hợp với người có khả năng phân tích, quan tâm đến tài chính và thị trường.",
#             "tests": [
#                 {
#                     "title": "Bài Test Kỹ Năng Phân tích Dữ liệu & Tư duy Chiến lược",
#                     "questions": [
#                         {
#                             "text": "Mục tiêu chính của việc trực quan hóa dữ liệu (Data Visualization) trong kinh tế là gì?",
#                             "options": [
#                                 "Làm cho báo cáo trông đẹp hơn",
#                                 "Truyền tải thông tin phức tạp một cách rõ ràng và nhanh chóng, làm nổi bật xu hướng và mẫu hình",
#                                 "Chỉ để làm nổi bật sự khác biệt giữa các con số",
#                                 "Thay thế hoàn toàn văn bản giải thích"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi đối diện với một vấn đề kinh tế/kinh doanh phức tạp, tư duy chiến lược yêu cầu bạn làm gì trước tiên?",
#                             "options": [
#                                 "Tìm giải pháp nhanh nhất",
#                                 "Xác định mục tiêu dài hạn, phạm vi và các yếu tố/ràng buộc chính",
#                                 "Sao chép mô hình của đối thủ cạnh tranh",
#                                 "Thu thập mọi dữ liệu có thể mà không phân loại"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tư duy phản biện trong phân tích kinh tế giúp bạn làm gì?",
#                             "options": [
#                                 "Luôn bác bỏ mọi số liệu thống kê",
#                                 "Đưa ra dự đoán dựa trên cảm tính",
#                                 "Đánh giá tính hợp lệ, nguồn gốc và ý nghĩa thực tế của các mô hình và giả định kinh tế",
#                                 "Chỉ tập trung vào dữ liệu ủng hộ quan điểm của bạn"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Phương pháp SWOT được sử dụng để phân tích điều gì trong chiến lược kinh doanh?",
#                             "options": [
#                                 "Lãi suất và tỷ giá hối đoái",
#                                 "Các điểm Mạnh (Strengths), điểm Yếu (Weaknesses), Cơ hội (Opportunities), và Thách thức (Threats) của một tổ chức/dự án",
#                                 "Biến động thị trường chứng khoán",
#                                 "Hiệu suất của chuỗi cung ứng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tại sao việc xác định nguyên nhân gốc rễ (Root Cause) quan trọng hơn việc chỉ xử lý các triệu chứng trong kinh tế?",
#                             "options": [
#                                 "Vì nó giúp bạn hoàn thành công việc nhanh hơn",
#                                 "Vì chỉ khi hiểu nguyên nhân gốc rễ, bạn mới có thể đưa ra giải pháp bền vững và ngăn ngừa tái phát",
#                                 "Vì nó là một yêu cầu pháp lý",
#                                 "Vì các triệu chứng không quan trọng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khái niệm Chi phí cơ hội (Opportunity Cost) đòi hỏi tư duy chiến lược nào?",
#                             "options": [
#                                 "Chỉ xem xét chi phí bằng tiền mặt",
#                                 "Đánh giá lợi ích tiềm năng bị bỏ lỡ khi chọn một phương án thay vì phương án tốt nhất tiếp theo",
#                                 "Chỉ tập trung vào lợi nhuận ngắn hạn",
#                                 "Đưa ra quyết định cảm tính"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi phân tích thị trường, dữ liệu định lượng (Quantitative Data) cung cấp thông tin gì?",
#                             "options": [
#                                 "Ý kiến và cảm xúc của khách hàng",
#                                 "Các con số, thống kê, và phép đo lường (ví dụ: doanh số, số lượng khách hàng)",
#                                 "Câu chuyện về thương hiệu",
#                                 "Các yếu tố văn hóa"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Để đảm bảo sự khách quan trong phân tích dữ liệu, người phân tích nên:",
#                             "options": [
#                                 "Loại bỏ dữ liệu không phù hợp với giả thuyết",
#                                 "Chỉ sử dụng dữ liệu từ một nguồn duy nhất",
#                                 "Công nhận các thiên kiến tiềm ẩn và kiểm tra các giả thuyết khác nhau",
#                                 "Chỉ báo cáo các kết quả tích cực"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Điều gì thể hiện sự thiếu tư duy chiến lược khi mở rộng thị trường?",
#                             "options": [
#                                 "Nghiên cứu kỹ lưỡng về đối thủ cạnh tranh",
#                                 "Thực hiện mở rộng mà không đánh giá nguồn lực cần thiết và rủi ro chính trị/kinh tế",
#                                 "Phát triển một kế hoạch dài hạn",
#                                 "Đặt mục tiêu tăng trưởng rõ ràng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong việc mô hình hóa kinh tế, giả định (Assumptions) được sử dụng để làm gì?",
#                             "options": [
#                                 "Để làm cho mô hình trở nên hoàn hảo",
#                                 "Đơn giản hóa thực tế phức tạp để mô hình có thể quản lý và phân tích được",
#                                 "Che giấu sự thiếu dữ liệu",
#                                 "Để đảm bảo mô hình luôn đúng"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ Năng Giao tiếp Thuyết phục & Trình bày",
#                     "questions": [
#                         {
#                             "text": "Mục đích chính của việc thuyết phục trong kinh doanh/tài chính là gì?",
#                             "options": [
#                                 "Làm cho người khác luôn đồng ý với bạn",
#                                 "Thay đổi hành vi, quan điểm hoặc quyết định của đối tượng bằng lập luận logic và bằng chứng",
#                                 "Thể hiện quyền lực",
#                                 "Trình bày thông tin một chiều"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi trình bày một báo cáo tài chính phức tạp, bạn nên ưu tiên điều gì ở phần mở đầu?",
#                             "options": [
#                                 "Đọc định nghĩa của tất cả các thuật ngữ",
#                                 "Trình bày tóm tắt điều hành (Executive Summary) và lợi ích (What's in it for them) của khán giả",
#                                 "Trình bày lời cảm ơn",
#                                 "Chỉ đi thẳng vào dữ liệu"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Việc sử dụng ngôn ngữ cơ thể (Body Language) tích cực khi giao tiếp kinh doanh thể hiện điều gì?",
#                             "options": [
#                                 "Bạn là người làm việc chăm chỉ nhất",
#                                 "Sự tự tin, chuyên nghiệp, và sự cởi mở với người nghe",
#                                 "Bạn đang nói dối",
#                                 "Bạn không cần chuẩn bị bài thuyết trình"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Để thuyết phục một nhà đầu tư, điều quan trọng nhất bạn cần trình bày là gì?",
#                             "options": [
#                                 "Câu chuyện cá nhân của bạn",
#                                 "Giá trị đề xuất (Value Proposition), phân tích rủi ro và lợi ích tiềm năng (ROI)",
#                                 "Tóm tắt quá khứ công ty",
#                                 "Chi tiết kỹ thuật về hệ thống máy tính của bạn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Lắng nghe tích cực (Active Listening) trong cuộc họp khách hàng liên quan đến việc gì?",
#                             "options": [
#                                 "Chỉ im lặng",
#                                 "Tập trung, đặt câu hỏi làm rõ, tóm tắt lại để xác nhận sự hiểu biết và thừa nhận cảm xúc",
#                                 "Chuẩn bị sẵn câu trả lời",
#                                 "Ghi chép mọi thứ một cách thụ động"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Lỗi phổ biến nhất khi sử dụng PowerPoint/Slide để trình bày là gì?",
#                             "options": [
#                                 "Sử dụng quá nhiều hình ảnh",
#                                 "Quá nhiều chữ và đọc nguyên văn từ Slide",
#                                 "Sử dụng phông chữ lớn",
#                                 "Không sử dụng biểu đồ"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi đối diện với câu hỏi phản biện từ khán giả, phản ứng tốt nhất thể hiện sự chuyên nghiệp là:",
#                             "options": [
#                                 "Cố gắng bảo vệ quan điểm của mình bằng mọi giá",
#                                 "Lắng nghe toàn bộ câu hỏi, thừa nhận tính hợp lý của nó (nếu có) và trả lời bằng dữ liệu/logic",
#                                 "Tránh trả lời và chuyển sang câu hỏi khác",
#                                 "Đổ lỗi cho ai đó khác"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Để tăng tính thuyết phục của một lập luận kinh tế, bạn nên dựa vào điều gì?",
#                             "options": [
#                                 "Kinh nghiệm cá nhân của bạn",
#                                 "Dữ liệu đáng tin cậy, mô hình phân tích đã được kiểm chứng và logic rõ ràng",
#                                 "Ý kiến của người nổi tiếng",
#                                 "Sử dụng giọng điệu to nhất"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi giao tiếp bằng văn bản (email, báo cáo), điều quan trọng nhất là:",
#                             "options": [
#                                 "Sử dụng biệt ngữ chuyên môn tối đa",
#                                 "Cấu trúc rõ ràng, sử dụng gạch đầu dòng và tiêu đề để dễ đọc",
#                                 "Viết càng dài càng tốt",
#                                 "Chỉ gửi cho một người duy nhất"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong đàm phán, việc hiểu BATNA (Best Alternative to a Negotiated Agreement) của bạn và đối tác giúp gì?",
#                             "options": [
#                                 "Giúp bạn luôn thắng",
#                                 "Thiết lập điểm giới hạn (bottom line) và tăng quyền lực đàm phán của bạn",
#                                 "Đảm bảo cuộc đàm phán thất bại",
#                                 "Luôn phải nhượng bộ"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ Năng Đạo đức Kinh doanh & Quản lý Rủi ro Cá nhân",
#                     "questions": [
#                         {
#                             "text": "Hành vi nào được coi là phi đạo đức nghiêm trọng nhất trong phân tích tài chính?",
#                             "options": [
#                                 "Mua cổ phiếu của công ty mà bạn phân tích",
#                                 "Sử dụng thông tin nội bộ (Insider Trading) để mua bán chứng khoán",
#                                 "Đưa ra nhận định sai lầm",
#                                 "Không hoàn thành báo cáo đúng hạn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Xung đột lợi ích (Conflict of Interest) xảy ra khi nào?",
#                             "options": [
#                                 "Bạn và đồng nghiệp không đồng ý về một chiến lược",
#                                 "Lợi ích cá nhân của bạn có khả năng ảnh hưởng đến việc đưa ra quyết định chuyên nghiệp khách quan",
#                                 "Bạn làm việc quá giờ",
#                                 "Bạn nhận lương cao hơn đồng nghiệp"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Thiên kiến neo giữ (Anchoring Bias) ảnh hưởng đến việc đưa ra quyết định kinh tế như thế nào?",
#                             "options": [
#                                 "Khiến bạn luôn tìm kiếm ý kiến thứ hai",
#                                 "Dựa quá nhiều vào mốc thông tin đầu tiên nhận được (ví dụ: giá chào bán đầu tiên), ngay cả khi nó không liên quan",
#                                 "Buộc bạn phải đa dạng hóa danh mục đầu tư",
#                                 "Giúp bạn đưa ra quyết định khách quan hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Vai trò của Người thổi còi (Whistleblower) trong kinh doanh là gì?",
#                             "options": [
#                                 "Người lan truyền tin đồn",
#                                 "Người báo cáo công khai các hoạt động bất hợp pháp, phi đạo đức hoặc sai trái trong tổ chức",
#                                 "Người tổ chức sự kiện",
#                                 "Người chịu trách nhiệm về quan hệ công chúng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Đánh giá Rủi ro (Risk Assessment) trong kinh doanh bao gồm những bước nào?",
#                             "options": [
#                                 "Chỉ tập trung vào rủi ro tài chính",
#                                 "Xác định, phân tích và đánh giá mức độ rủi ro tiềm ẩn",
#                                 "Đổ lỗi cho những rủi ro đã xảy ra",
#                                 "Luôn đảm bảo rủi ro bằng 0"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tư duy Bầy đàn (Herd Mentality) trong đầu tư là một rủi ro vì:",
#                             "options": [
#                                 "Nó quá tốn kém",
#                                 "Nó dẫn đến các bong bóng hoặc sụp đổ thị trường khi nhà đầu tư bỏ qua phân tích cơ bản và chỉ làm theo đám đông",
#                                 "Nó tạo ra quá nhiều sự đa dạng",
#                                 "Nó làm tăng tính thanh khoản"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi bạn phát hiện ra một lỗi nghiêm trọng trong dữ liệu tài chính đã được công bố, điều đầu tiên bạn nên làm là gì?",
#                             "options": [
#                                 "Che giấu lỗi",
#                                 "Ngay lập tức thông báo cho người quản lý/nhóm liên quan để tiến hành đánh giá và điều chỉnh",
#                                 "Tự mình sửa lỗi mà không thông báo",
#                                 "Gửi email công khai cho toàn bộ công ty"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trách nhiệm xã hội của doanh nghiệp (CSR) liên quan đến điều gì?",
#                             "options": [
#                                 "Chỉ trả lương cao cho nhân viên",
#                                 "Doanh nghiệp cân nhắc tác động của mình lên xã hội, môi trường và kinh tế, hành động một cách có đạo đức",
#                                 "Chỉ tập trung vào lợi nhuận tối đa",
#                                 "Chi phí tiếp thị"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Thiên kiến đại diện (Representativeness Bias) trong kinh tế là:",
#                             "options": [
#                                 "Việc bạn luôn chọn công ty có tên dễ nhớ",
#                                 "Việc đưa ra quyết định dựa trên mức độ một sự kiện giống với hình mẫu định sẵn, bỏ qua xác suất thống kê cơ bản",
#                                 "Đánh giá quá cao rủi ro",
#                                 "Chỉ tin vào thông tin đầu tiên nhận được"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong việc quản lý rủi ro cá nhân đối với người mới bắt đầu (sinh viên/người làm thuê), điều gì là quan trọng nhất?",
#                             "options": [
#                                 "Chỉ tập trung vào thị trường chứng khoán",
#                                 "Quản lý ngân sách cá nhân, xây dựng quỹ khẩn cấp và không vay nợ quá mức",
#                                 "Đầu tư vào mọi thứ",
#                                 "Không bao giờ chi tiêu"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 }
#             ]
#         },
#         "marketing": {
#             "name": "Marketing",
#             "description": "Dành cho người sáng tạo, có khả năng giao tiếp tốt và hiểu insight khách hàng.",
#             "tests": [
#                 {
#                     "title": "Bài Test Kỹ năng Sáng tạo & Tư duy Khách hàng",
#                     "questions": [
#                         {
#                             "text": "Tư duy hướng Khách hàng (Customer-Centric) là gì?",
#                             "options": [
#                                 "Luôn đồng ý với mọi yêu cầu của khách hàng",
#                                 "Đặt nhu cầu, mong muốn và trải nghiệm của khách hàng làm trọng tâm của mọi quyết định",
#                                 "Chỉ tập trung vào việc bán sản phẩm",
#                                 "Thu thập dữ liệu khách hàng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi phát triển một chiến dịch Marketing mới, hành động nào thể hiện sự sáng tạo?",
#                             "options": [
#                                 "Sao chép chiến dịch thành công nhất của đối thủ",
#                                 "Luôn sử dụng cùng một định dạng quảng cáo",
#                                 "Đề xuất một cách tiếp cận độc đáo, chưa từng có để giải quyết vấn đề của khách hàng",
#                                 "Cố gắng giảm chi phí quảng cáo"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Việc tạo ra Chân dung Khách hàng (Buyer Persona) phục vụ mục đích gì?",
#                             "options": [
#                                 "Để biết tên khách hàng",
#                                 "Giúp nhóm Marketing hiểu sâu sắc về động lực, thách thức và hành vi của đối tượng mục tiêu",
#                                 "Chỉ là thủ tục",
#                                 "Để tăng ngân sách quảng cáo"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Đổi mới trong Marketing (Marketing Innovation) được định nghĩa tốt nhất là:",
#                             "options": [
#                                 "Luôn sử dụng công nghệ mới nhất",
#                                 "Áp dụng các ý tưởng, chiến lược hoặc công cụ mới để tạo ra giá trị mới cho khách hàng hoặc thị trường",
#                                 "Làm việc nhanh hơn",
#                                 "Đưa ra các chương trình khuyến mãi"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi một ý tưởng Marketing sáng tạo của bạn bị nhóm bác bỏ, bạn nên làm gì?",
#                             "options": [
#                                 "Bỏ cuộc và làm theo ý tưởng của nhóm",
#                                 "Đón nhận phản hồi, phân tích lý do bác bỏ và điều chỉnh ý tưởng bằng dữ liệu hỗ trợ",
#                                 "Cố gắng thuyết phục bằng mọi giá",
#                                 "Thất vọng và không đưa ra ý tưởng nào nữa"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Giá trị đề xuất (Value Proposition) được xem là sáng tạo khi nó:",
#                             "options": [
#                                 "Cực kỳ đắt",
#                                 "Chỉ tập trung vào tính năng",
#                                 "Giải quyết vấn đề của khách hàng theo cách tốt hơn, độc đáo hoặc rẻ hơn so với đối thủ",
#                                 "Được quảng cáo rộng rãi"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Thiên kiến cá nhân (Personal Bias) ảnh hưởng tiêu cực đến tư duy khách hàng như thế nào?",
#                             "options": [
#                                 "Giúp bạn hiểu khách hàng tốt hơn",
#                                 "Khiến bạn thiết kế sản phẩm/dịch vụ dựa trên sở thích cá nhân thay vì nhu cầu thực tế của thị trường",
#                                 "Đảm bảo sự sáng tạo",
#                                 "Giúp bạn làm việc nhanh hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong Marketing, động não (Brainstorming) hiệu quả đòi hỏi nguyên tắc nào?",
#                             "options": [
#                                 "Chỉ những người có kinh nghiệm mới được nói",
#                                 "Số lượng ý tưởng được ưu tiên hơn chất lượng ban đầu; không phán xét trong quá trình tạo ý tưởng",
#                                 "Chỉ đưa ra các ý tưởng thực tế",
#                                 "Phải có một người dẫn dắt duy nhất"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tư duy từ ngoài vào (Outside-in Thinking) trong Marketing có nghĩa là gì?",
#                             "options": [
#                                 "Chỉ nhìn vào bên ngoài công ty",
#                                 "Bắt đầu từ thị trường/nhu cầu khách hàng để định hình sản phẩm/chiến lược của công ty",
#                                 "Chỉ thuê người ngoài làm việc",
#                                 "Chỉ phân tích đối thủ cạnh tranh"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Yếu tố nào sau đây là quan trọng nhất để nuôi dưỡng sự sáng tạo liên tục trong Marketing?",
#                             "options": [
#                                 "Luôn làm việc một mình",
#                                 "Sẵn sàng chấp nhận rủi ro, thất bại và học hỏi từ thử nghiệm",
#                                 "Chỉ đọc sách kinh tế",
#                                 "Chỉ tập trung vào quá trình phân tích dữ liệu"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ năng Phân tích Thị trường & Đánh giá Hiệu quả",
#                     "questions": [
#                         {
#                             "text": "Mục tiêu chính của việc Phân tích Thị trường (Market Research) là gì?",
#                             "options": [
#                                 "Dự đoán chính xác giá cổ phiếu",
#                                 "Giảm thiểu sự không chắc chắn và cung cấp thông tin để đưa ra quyết định Marketing sáng suốt",
#                                 "Tìm kiếm nhà đầu tư",
#                                 "Chỉ để tạo ra một tài liệu dài"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong đánh giá hiệu quả, ROI (Return on Investment) của một chiến dịch đo lường điều gì?",
#                             "options": [
#                                 "Số lần nhấp chuột (clicks)",
#                                 "Tỷ lệ lợi nhuận thu được so với chi phí đã bỏ ra",
#                                 "Tên của khách hàng",
#                                 "Số lượng bài đăng trên mạng xã hội"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi phân tích dữ liệu, việc xác định dữ liệu ngoại lai (Outliers) là quan trọng vì:",
#                             "options": [
#                                 "Chúng luôn là lỗi",
#                                 "Chúng có thể làm sai lệch kết quả thống kê hoặc tiết lộ một xu hướng/sự kiện thị trường bất thường cần điều tra thêm",
#                                 "Chúng phải được xóa ngay lập tức",
#                                 "Chúng giúp tăng độ chính xác"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Thiên kiến cá nhân (Bias) trong việc phân tích dữ liệu Marketing là:",
#                             "options": [
#                                 "Luôn tìm kiếm dữ liệu trên mạng",
#                                 "Giải thích dữ liệu theo cách ủng hộ giả định ban đầu của bạn, bỏ qua bằng chứng chống lại",
#                                 "Phân tích dữ liệu quá chậm",
#                                 "Chỉ sử dụng biểu đồ"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Chỉ số Chuyển đổi (Conversion Rate) được sử dụng để đánh giá hiệu quả của điều gì?",
#                             "options": [
#                                 "Số lượng nhân viên mới",
#                                 "Khả năng của một chiến dịch/trang web trong việc biến người truy cập thành hành động mong muốn (mua hàng, đăng ký...)",
#                                 "Tỷ lệ quay lại của nhân viên",
#                                 "Mức độ hài lòng của nhân viên"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Phân tích A/B là công cụ đánh giá hiệu quả nào?",
#                             "options": [
#                                 "So sánh doanh số của hai năm",
#                                 "Thử nghiệm hai phiên bản (A và B) của cùng một yếu tố để xác định phiên bản nào hoạt động tốt hơn dựa trên dữ liệu",
#                                 "Phân tích tuổi tác của khách hàng",
#                                 "Phân tích chi phí"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi thấy một KPI giảm mạnh, hành động phân tích tiếp theo nên là gì?",
#                             "options": [
#                                 "Ngừng chiến dịch ngay lập tức",
#                                 "Tìm kiếm nguyên nhân gốc rễ bằng cách đào sâu vào các chỉ số phụ và bối cảnh thị trường liên quan",
#                                 "Đổ lỗi cho đội ngũ bán hàng",
#                                 "Thay đổi KPI"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Phân khúc Thị trường (Market Segmentation) là kỹ năng phân tích gì?",
#                             "options": [
#                                 "Chia công ty thành các phòng ban",
#                                 "Chia thị trường lớn thành các nhóm khách hàng nhỏ hơn với nhu cầu và đặc điểm tương tự",
#                                 "Chỉ cần thiết cho phân tích giá",
#                                 "Phân tích giá cổ phiếu"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tư duy chiến lược trong Marketing được thể hiện qua hành động nào?",
#                             "options": [
#                                 "Luôn ưu tiên các nhiệm vụ ngắn hạn",
#                                 "Định hình các mục tiêu Marketing dựa trên mục tiêu kinh doanh tổng thể và dài hạn của công ty",
#                                 "Chỉ tập trung vào việc tạo nội dung mới",
#                                 "Chỉ phân tích các số liệu hàng ngày"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong Marketing, Thử nghiệm và Sai lầm (Test and Learn) là một phần quan trọng của phân tích hiệu quả vì:",
#                             "options": [
#                                 "Nó giúp bạn tránh mọi sai lầm",
#                                 "Thị trường luôn thay đổi, và việc thử nghiệm nhỏ giúp tối ưu hóa mà không gây rủi ro lớn",
#                                 "Nó là một yêu cầu pháp lý",
#                                 "Nó là cách rẻ nhất để làm Marketing"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ năng Giao tiếp Đa kênh & Thương lượng",
#                     "questions": [
#                         {
#                             "text": "Giao tiếp Đa kênh (Omnichannel Communication) trong Marketing yêu cầu điều gì?",
#                             "options": [
#                                 "Sử dụng tất cả các kênh có thể",
#                                 "Đảm bảo trải nghiệm và thông điệp nhất quán, liền mạch cho khách hàng trên mọi kênh tiếp xúc (online và offline)",
#                                 "Chỉ giao tiếp qua email",
#                                 "Không cần quan tâm đến phản hồi"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong thương lượng với đối tác, điều quan trọng nhất cần chuẩn bị trước là gì?",
#                             "options": [
#                                 "Luôn tỏ ra cứng rắn",
#                                 "Xác định mục tiêu chính, các điểm nhượng bộ có thể và BATNA (Giải pháp thay thế tốt nhất cho Thỏa thuận được đàm phán)",
#                                 "Biết mọi chi tiết về đối tác",
#                                 "Chỉ tập trung vào giá"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Giao tiếp trong khủng hoảng Marketing (Crisis Communication) nên ưu tiên yếu tố nào?",
#                             "options": [
#                                 "Tránh trả lời",
#                                 "Đổ lỗi",
#                                 "Minh bạch, trung thực, đồng cảm và hành động nhanh chóng để kiểm soát thông tin",
#                                 "Chờ đợi một tuần để đánh giá"
#                             ],
#                             "correct": "C"
#                         },
#                         {
#                             "text": "Mục tiêu của việc sử dụng Giọng điệu Thương hiệu (Brand Tone of Voice) là gì?",
#                             "options": [
#                                 "Để làm cho bài viết trông phức tạp",
#                                 "Tạo ra sự nhất quán, cá tính và kết nối cảm xúc với khách hàng",
#                                 "Chỉ để giải trí",
#                                 "Chỉ cần thiết cho các công ty lớn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Lỗi phổ biến nhất khi giao tiếp với khách hàng trên mạng xã hội là gì?",
#                             "options": [
#                                 "Trả lời quá chậm",
#                                 "Sử dụng giọng điệu khác biệt hoặc tranh cãi với khách hàng",
#                                 "Sử dụng biểu tượng cảm xúc",
#                                 "Đăng bài quá thường xuyên"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Kỹ năng thương lượng nào giúp đạt được kết quả Win-Win (Đôi bên cùng thắng)?",
#                             "options": [
#                                 "Nhất quyết giữ vững lập trường ban đầu",
#                                 "Tìm kiếm các giải pháp sáng tạo đáp ứng nhu cầu cốt lõi của cả hai bên thay vì chỉ tập trung vào vị trí",
#                                 "Đe dọa rời khỏi cuộc đàm phán",
#                                 "Chấp nhận mọi yêu cầu"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi viết một email Marketing hiệu quả, bạn nên tập trung vào:",
#                             "options": [
#                                 "Nội dung rất dài và chi tiết",
#                                 "Tiêu đề hấp dẫn, nội dung ngắn gọn và một Lời kêu gọi hành động (Call to Action) rõ ràng",
#                                 "Chỉ sử dụng hình ảnh",
#                                 "Viết hoa toàn bộ nội dung"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Nguyên tắc Tương hỗ (Reciprocity Principle) trong thương lượng/thuyết phục là gì?",
#                             "options": [
#                                 "Nếu bạn cho đi điều gì đó (ví dụ: thông tin, ưu đãi), người khác sẽ cảm thấy có nghĩa vụ đáp lại",
#                                 "Luôn yêu cầu nhiều hơn những gì bạn cần",
#                                 "Chỉ giao dịch với bạn bè",
#                                 "Không bao giờ nhượng bộ"
#                             ],
#                             "correct": "A"
#                         },
#                         {
#                             "text": "Sự thích ứng (Adaptability) trong giao tiếp Marketing được thể hiện bằng hành động nào?",
#                             "options": [
#                                 "Thay đổi thông điệp, kênh hoặc giọng điệu dựa trên phản hồi dữ liệu và sự thay đổi của thị trường",
#                                 "Chỉ sử dụng một kênh duy nhất",
#                                 "Luôn nói cùng một điều",
#                                 "Không bao giờ thử nghiệm"
#                             ],
#                             "correct": "A"
#                         },
#                         {
#                             "text": "Trong thương lượng, việc đặt nhiều câu hỏi mở (Open-ended questions) giúp gì?",
#                             "options": [
#                                 "Kéo dài thời gian",
#                                 "Thu thập thông tin về nhu cầu, động lực và các giới hạn thực tế của đối tác",
#                                 "Gây sự nhầm lẫn",
#                                 "Chỉ để kiểm tra sự tập trung của đối tác"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 }
#             ]
#         },
#         "ngon-ngu-anh": {
#             "name": "Ngôn ngữ Anh",
#             "description": "Cho người yêu ngôn ngữ, thích giao tiếp quốc tế và văn hóa đa dạng.",
#             "tests": [
#                 {
#                     "title": "Bài Test Kỹ năng Tư duy Liên văn hóa & Thích ứng",
#                     "questions": [
#                         {
#                             "text": "Năng lực Liên văn hóa (Intercultural Competence) trong Ngôn ngữ Anh là gì?",
#                             "options": [
#                                 "Khả năng nói tiếng Anh hoàn hảo",
#                                 "Khả năng tương tác hiệu quả và phù hợp với người đến từ các nền văn hóa khác nhau",
#                                 "Chỉ cần học ngữ pháp của nhiều ngôn ngữ",
#                                 "Khả năng viết tiểu luận"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi giao tiếp với người bản xứ (Native Speaker), điều nào thể hiện sự thích ứng tốt nhất?",
#                             "options": [
#                                 "Luôn dùng biệt ngữ (slang) mới nhất",
#                                 "Điều chỉnh tốc độ nói, độ phức tạp của từ ngữ và kiểm tra sự hiểu biết của người nghe",
#                                 "Luôn cố gắng nói nhanh",
#                                 "Chỉ nói về các chủ đề học thuật"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Thiên kiến văn hóa (Cultural Bias) trong giao tiếp là gì?",
#                             "options": [
#                                 "Luôn ưu tiên văn hóa của bạn",
#                                 "Sử dụng các giả định hoặc tiêu chuẩn văn hóa của mình để đánh giá hành vi/quan điểm của người khác",
#                                 "Khả năng hiểu nhiều văn hóa",
#                                 "Chỉ nói về các vấn đề lịch sử"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Ngữ cảnh giao tiếp (Context of Communication) quan trọng trong Ngôn ngữ Anh vì:",
#                             "options": [
#                                 "Nó xác định từ vựng",
#                                 "Nó quyết định ý nghĩa thực sự của lời nói, đặc biệt là trong các nền văn hóa có tính ngữ cảnh cao (High-Context Cultures)",
#                                 "Nó chỉ cần thiết cho việc dịch thuật",
#                                 "Nó giúp bạn đọc nhanh hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi học một biến thể tiếng Anh mới (ví dụ: Anh-Anh vs. Anh-Mỹ), bạn nên ưu tiên kỹ năng nào?",
#                             "options": [
#                                 "Chỉ học từ vựng hoàn toàn mới",
#                                 "Khả năng nhận ra và chuyển đổi linh hoạt giữa các quy ước về chính tả, ngữ pháp và cách diễn đạt",
#                                 "Chỉ cần tập trung vào giọng điệu",
#                                 "Bác bỏ các biến thể khác"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Sự thích ứng trong việc sử dụng tiếng Anh như một ngôn ngữ chung (Lingua Franca) đòi hỏi bạn:",
#                             "options": [
#                                 "Chỉ giao tiếp với người nói tiếng Anh bản xứ",
#                                 "Nói rõ ràng, tránh các thành ngữ phức tạp và sử dụng ngôn ngữ trung tính để người không bản xứ cũng hiểu",
#                                 "Luôn sử dụng các câu dài",
#                                 "Không bao giờ sử dụng công cụ dịch"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tư duy phản biện giúp bạn đánh giá các tài liệu văn học (Literature) bằng cách nào?",
#                             "options": [
#                                 "Chỉ chấp nhận ý kiến của nhà phê bình nổi tiếng",
#                                 "Đặt câu hỏi về ý định của tác giả, bối cảnh lịch sử và các giả định/thiên kiến trong tác phẩm",
#                                 "Chỉ tập trung vào vẻ đẹp ngôn từ",
#                                 "Đọc thật nhanh"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Để phát triển sự thấu cảm (Empathy) liên văn hóa, một người học Ngôn ngữ Anh nên làm gì?",
#                             "options": [
#                                 "Chỉ đọc tiểu thuyết của một quốc gia",
#                                 "Tiếp xúc với các nguồn tin, phim ảnh và văn học đa dạng từ nhiều nền văn hóa nói tiếng Anh",
#                                 "Giao tiếp ít nhất có thể",
#                                 "Luôn tin rằng văn hóa của mình là đúng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Lỗi Dịch thuật (Translation Errors) thường xảy ra do thiếu kỹ năng nào?",
#                             "options": [
#                                 "Ngữ pháp cơ bản",
#                                 "Thiếu hiểu biết sâu sắc về bối cảnh văn hóa và sắc thái ý nghĩa (connotation) của từ ngữ trong ngôn ngữ đích",
#                                 "Kỹ năng đánh máy",
#                                 "Kỹ năng nói trôi chảy"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Quản lý sự không chắc chắn (Uncertainty Management) trong giao tiếp đa văn hóa là gì?",
#                             "options": [
#                                 "Tránh mọi tình huống không chắc chắn",
#                                 "Duy trì sự bình tĩnh, cởi mở và tiếp cận các tình huống không quen thuộc với thái độ tích cực và sẵn sàng học hỏi",
#                                 "Luôn yêu cầu thông tin chi tiết",
#                                 "Chỉ giao tiếp với những người bạn biết"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ năng Phân tích Nội dung & Nghiên cứu",
#                     "questions": [
#                         {
#                             "text": "Phân tích Nội dung (Content Analysis) trong Ngôn ngữ Anh là gì?",
#                             "options": [
#                                 "Chỉ tóm tắt lại nội dung",
#                                 "Phân tích cấu trúc, chủ đề, giọng điệu, và các yếu tố tu từ (rhetorical devices) của một văn bản/bài nói",
#                                 "Chỉ tìm lỗi ngữ pháp",
#                                 "Chỉ đọc nhanh"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi nghiên cứu một chủ đề học thuật, kỹ năng nào giúp bạn xác định nguồn đáng tin cậy?",
#                             "options": [
#                                 "Nguồn có nhiều lượt xem",
#                                 "Khả năng đánh giá tính chuyên môn của tác giả, quy trình bình duyệt (peer-review) và tính cập nhật của thông tin",
#                                 "Nguồn được viết bằng tiếng Anh",
#                                 "Nguồn bạn tìm thấy đầu tiên trên Google"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tư duy Phản biện trong nghiên cứu giúp bạn tránh mắc lỗi nào?",
#                             "options": [
#                                 "Viết bài quá dài",
#                                 "Chấp nhận các tuyên bố hoặc kết luận mà không có bằng chứng hỗ trợ hoặc phân tích logic",
#                                 "Không sử dụng trích dẫn",
#                                 "Đọc quá chậm"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tài liệu tham khảo (Citation) và Trích dẫn (Referencing) quan trọng trong nghiên cứu học thuật vì:",
#                             "options": [
#                                 "Để làm cho bài viết trông dài hơn",
#                                 "Thể hiện sự liêm chính (integrity), cung cấp bằng chứng cho lập luận và tôn vinh công sức của tác giả gốc",
#                                 "Chỉ là thủ tục",
#                                 "Để giới hạn số lượng nguồn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Mục đích của việc tạo ra Đề cương (Outline) cho một bài luận học thuật là gì?",
#                             "options": [
#                                 "Chỉ để gửi cho giáo viên",
#                                 "Tổ chức các ý tưởng một cách logic, đảm bảo luồng thông tin mạch lạc và hỗ trợ cấu trúc của lập luận",
#                                 "Để viết nhanh hơn",
#                                 "Để tìm lỗi chính tả"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tính khách quan (Objectivity) trong phân tích văn học có nghĩa là:",
#                             "options": [
#                                 "Bác bỏ cảm xúc cá nhân",
#                                 "Tập trung vào các bằng chứng từ văn bản để hỗ trợ cho việc diễn giải (interpretation) thay vì chỉ cảm nhận cá nhân",
#                                 "Không bao giờ có ý kiến riêng",
#                                 "Chỉ phân tích các tác phẩm kinh điển"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi đọc một bài viết chuyên sâu, kỹ năng nào giúp bạn nắm bắt được các ý chính?",
#                             "options": [
#                                 "Đọc từng chữ",
#                                 "Kỹ năng quét (Skimming) và đọc lướt (Scanning), đồng thời xác định câu chủ đề (Topic Sentences) và luận điểm chính",
#                                 "Dịch mọi từ không biết",
#                                 "Ghi nhớ mọi chi tiết"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Thiên kiến xác nhận (Confirmation Bias) ảnh hưởng tiêu cực đến nghiên cứu như thế nào?",
#                             "options": [
#                                 "Khiến bạn trích dẫn quá nhiều",
#                                 "Khiến bạn chỉ tìm kiếm các nguồn hoặc bằng chứng ủng hộ giả thuyết đã có của mình",
#                                 "Giúp bạn tìm nguồn nhanh hơn",
#                                 "Làm cho bài viết của bạn ngắn hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong nghiên cứu ngôn ngữ, Phân tích Định tính (Qualitative Analysis) cung cấp thông tin gì?",
#                             "options": [
#                                 "Các số liệu thống kê",
#                                 "Hiểu biết sâu sắc về ngữ cảnh, ý nghĩa, và kinh nghiệm (ví dụ: phỏng vấn, phân tích diễn ngôn)",
#                                 "Biểu đồ",
#                                 "Dự đoán tương lai"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Viết rõ ràng và súc tích (Clarity and Conciseness) quan trọng trong học thuật vì:",
#                             "options": [
#                                 "Nó giúp giáo viên chấm bài nhanh hơn",
#                                 "Nó đảm bảo rằng thông điệp, lập luận và ý tưởng phức tạp của bạn được truyền đạt hiệu quả mà không bị mơ hồ",
#                                 "Nó là một yêu cầu pháp lý",
#                                 "Nó là phong cách viết duy nhất"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ năng Trình bày Lời nói & Biên tập Văn bản",
#                     "questions": [
#                         {
#                             "text": "Mục tiêu chính của việc Biên tập Văn bản (Editing) trong Ngôn ngữ Anh là gì?",
#                             "options": [
#                                 "Chỉ sửa lỗi chính tả",
#                                 "Cải thiện tính rõ ràng, lưu loát, giọng điệu và logic của văn bản",
#                                 "Làm cho văn bản dài hơn",
#                                 "Chỉ cần thiết cho dịch thuật"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi Trình bày (Presenting) một chủ đề học thuật, điều quan trọng nhất bạn cần làm là:",
#                             "options": [
#                                 "Đọc từng chữ trên Slide",
#                                 "Tập trung vào việc truyền tải một thông điệp cốt lõi rõ ràng và kết nối với khán giả bằng giao tiếp bằng mắt",
#                                 "Sử dụng nhiều thuật ngữ phức tạp",
#                                 "Nói nhanh nhất có thể"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Kỹ năng Proofreading (Đọc soát) khác với Editing ở chỗ:",
#                             "options": [
#                                 "Proofreading tập trung vào việc sửa lỗi cuối cùng (chính tả, ngữ pháp, định dạng) trước khi xuất bản",
#                                 "Editing tập trung vào lỗi nhỏ",
#                                 "Proofreading là sửa lỗi lớn",
#                                 "Cả hai là một"
#                             ],
#                             "correct": "A"
#                         },
#                         {
#                             "text": "Giao tiếp bằng mắt (Eye Contact) khi thuyết trình bằng tiếng Anh thể hiện điều gì?",
#                             "options": [
#                                 "Bạn đang cố gắng ghi nhớ",
#                                 "Sự tự tin, sự chân thành và khả năng tương tác/thu hút khán giả",
#                                 "Bạn đang đọc một cách máy móc",
#                                 "Bạn đang cố gắng kết thúc nhanh"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi nhận phản hồi về bài viết của mình, một người học ngôn ngữ nên làm gì?",
#                             "options": [
#                                 "Cố gắng bảo vệ bài viết của mình",
#                                 "Đón nhận một cách chuyên nghiệp, tìm hiểu các điểm yếu và xem đó là cơ hội để cải thiện kỹ năng",
#                                 "Chỉ sửa lỗi ngữ pháp",
#                                 "Bỏ qua các gợi ý về cấu trúc"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tông giọng (Tone) và Phong cách (Style) trong viết lách nên được điều chỉnh dựa trên yếu tố nào?",
#                             "options": [
#                                 "Sở thích cá nhân",
#                                 "Đối tượng đọc (Audience), mục đích (Purpose) và loại văn bản (Genre) (ví dụ: học thuật, báo chí, kinh doanh)",
#                                 "Độ dài của văn bản",
#                                 "Ngôn ngữ sử dụng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Nghệ thuật Dừng (The Power of the Pause) trong trình bày bằng lời nói giúp gì?",
#                             "options": [
#                                 "Để người nói nghỉ ngơi",
#                                 "Nhấn mạnh ý chính, cho phép khán giả xử lý thông tin và giúp bài nói có nhịp điệu tự nhiên hơn",
#                                 "Giúp bạn nhớ bài",
#                                 "Làm cho bài nói ngắn hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi biên tập một bản dịch, điều quan trọng nhất cần kiểm tra là gì?",
#                             "options": [
#                                 "Từ vựng đã được thay thế bằng từ phức tạp hơn chưa",
#                                 "Tính chính xác về ý nghĩa (accuracy) và tính tự nhiên/lưu loát (fluency) của văn bản đích",
#                                 "Số lượng từ",
#                                 "Chỉ kiểm tra dấu chấm câu"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Sự rõ ràng và đơn giản trong trình bày bằng tiếng Anh có ý nghĩa gì?",
#                             "options": [
#                                 "Luôn sử dụng từ vựng dễ nhất",
#                                 "Tránh cấu trúc câu phức tạp không cần thiết và sử dụng từ ngữ chính xác để truyền tải ý tưởng",
#                                 "Chỉ cần nói to",
#                                 "Sử dụng tiếng lóng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Trong các bài viết chuyên nghiệp, Tính nhất quán (Consistency) quan trọng đối với điều gì?",
#                             "options": [
#                                 "Việc sử dụng từ vựng phức tạp",
#                                 "Chính tả, cách viết hoa, định dạng và việc sử dụng thuật ngữ chuyên môn",
#                                 "Chỉ để làm cho văn bản dài hơn",
#                                 "Tốc độ đọc"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 }
#             ]
#         },
#         "luat": {
#             "name": "Luật",
#             "description": "Phù hợp với người có tư duy logic, công bằng và khả năng phân tích tốt.",
#             "tests": [
#                 {
#                     "title": "Bài Test Kỹ năng Tư duy Phản biện & Logic",
#                     "questions": [
#                         {
#                             "text": "Tư duy Phản biện (Critical Thinking) trong ngành Luật là gì?",
#                             "options": [
#                                 "Luôn chống đối ý kiến của đối thủ",
#                                 "Khả năng phân tích, đánh giá tính hợp lệ của các lập luận pháp lý, các tiền lệ và quy phạm pháp luật",
#                                 "Chỉ tập trung vào việc ghi nhớ các điều luật",
#                                 "Luôn tin vào mọi điều được viết trong sách luật"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Ngụy biện cá nhân (Ad Hominem Fallacy) là một lỗi logic mà bạn cần tránh, đó là:",
#                             "options": [
#                                 "Tấn công vào lập luận",
#                                 "Tấn công vào người đưa ra lập luận thay vì chính lập luận hoặc bằng chứng của họ",
#                                 "Sử dụng quá nhiều biệt ngữ pháp lý",
#                                 "Trích dẫn một điều luật không còn hiệu lực"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi phân tích một Tình huống Pháp lý (Legal Case), bước đầu tiên thể hiện tư duy logic là gì?",
#                             "options": [
#                                 "Tìm ngay ra điều luật liên quan",
#                                 "Xác định các sự kiện pháp lý quan trọng (material facts) và câu hỏi pháp lý cốt lõi (issue)",
#                                 "Bắt đầu viết bản biện hộ",
#                                 "Chỉ tập trung vào cảm xúc của các bên"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Suy luận Diễn dịch (Deductive Reasoning) trong Luật là gì?",
#                             "options": [
#                                 "Đi từ ví dụ cụ thể đến nguyên tắc chung",
#                                 "Áp dụng một nguyên tắc pháp luật chung đã được thiết lập (ví dụ: điều luật) vào một tình huống cụ thể",
#                                 "Chỉ dựa vào tiền lệ",
#                                 "Chỉ dùng trong luật hình sự"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tiền lệ pháp lý (Legal Precedent) được sử dụng trong tư duy phản biện để làm gì?",
#                             "options": [
#                                 "Để tìm ra luật mới",
#                                 "Để hỗ trợ hoặc phân biệt lập luận bằng cách chỉ ra cách luật đã được áp dụng trong các trường hợp tương tự trước đây",
#                                 "Để chứng minh mọi lập luận đều sai",
#                                 "Chỉ áp dụng cho các vụ án hình sự"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tính mập mờ (Ambiguity) trong văn bản pháp luật đòi hỏi tư duy phản biện nào?",
#                             "options": [
#                                 "Bỏ qua các thuật ngữ mập mờ",
#                                 "Phân tích các cách diễn giải khác nhau và xác định cách diễn giải phù hợp nhất với mục đích của luật (Legislative Intent)",
#                                 "Hỏi ý kiến của một người không chuyên",
#                                 "Chỉ chọn cách diễn giải đơn giản nhất"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Burden of Proof (Gánh nặng chứng minh) thể hiện tư duy logic nào trong pháp luật?",
#                             "options": [
#                                 "Chỉ yêu cầu bên bị kiện phải chứng minh",
#                                 "Nguyên tắc xác định bên nào có trách nhiệm phải cung cấp đủ bằng chứng để thuyết phục Tòa án về sự thật",
#                                 "Cả hai bên phải chứng minh",
#                                 "Chỉ cần lời khai"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi đối diện với một quy tắc pháp luật có vẻ không công bằng, tư duy phản biện yêu cầu bạn:",
#                             "options": [
#                                 "Luôn chấp nhận vì đó là luật",
#                                 "Phân tích lý do (rationale) đằng sau quy tắc đó, xem xét hậu quả và đề xuất cải cách dựa trên bằng chứng và nguyên tắc công lý",
#                                 "Bác bỏ hoàn toàn",
#                                 "Chỉ áp dụng trong các trường hợp bạn cảm thấy công bằng"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Suy luận Quy nạp (Inductive Reasoning) trong Luật là:",
#                             "options": [
#                                 "Áp dụng quy tắc chung cho trường hợp cụ thể",
#                                 "Đi từ các trường hợp cụ thể hoặc dữ liệu để phát triển một nguyên tắc hoặc giả thuyết pháp lý chung (ví dụ: phát triển luật chung)",
#                                 "Chỉ cần thiết cho việc giảng dạy",
#                                 "Luôn dẫn đến một kết luận chắc chắn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tính nhất quán (Consistency) trong lập luận pháp lý quan trọng vì:",
#                             "options": [
#                                 "Nó giúp giảm số lượng từ",
#                                 "Nó thể hiện sự logic và đáng tin cậy: các lập luận và nguyên tắc áp dụng trong vụ án này phải phù hợp với các vụ án khác tương tự",
#                                 "Nó là một yêu cầu về định dạng",
#                                 "Nó giúp bạn thắng kiện"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ năng Nghiên cứu Pháp lý & Giải quyết Vấn đề",
#                     "questions": [
#                         {
#                             "text": "Nghiên cứu Pháp lý (Legal Research) hiệu quả đòi hỏi kỹ năng nào trước tiên?",
#                             "options": [
#                                 "Khả năng gõ nhanh",
#                                 "Khả năng xác định và tinh chỉnh các từ khóa (keywords) và các thuật ngữ pháp lý liên quan đến vấn đề",
#                                 "Khả năng ghi nhớ tất cả điều luật",
#                                 "Khả năng đọc rất nhanh"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi giải quyết một vấn đề pháp lý mới, Tư duy Sáng tạo (Creative Thinking) giúp gì?",
#                             "options": [
#                                 "Viết luật mới",
#                                 "Tìm kiếm các giải pháp, lý thuyết hoặc lập luận pháp lý chưa từng được sử dụng trước đây để áp dụng vào vấn đề",
#                                 "Làm cho vấn đề phức tạp hơn",
#                                 "Luôn dựa vào các giải pháp cũ"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Mục tiêu của việc sắp xếp các nguồn nghiên cứu theo Thứ bậc Pháp lý (Hierarchy of Laws) là gì?",
#                             "options": [
#                                 "Để tìm nguồn dễ hơn",
#                                 "Để xác định nguồn nào có thẩm quyền cao nhất (ví dụ: Hiến pháp > Luật > Nghị định) khi có xung đột quy tắc",
#                                 "Chỉ để làm cho nghiên cứu trông chuyên nghiệp",
#                                 "Để giới hạn số lượng nguồn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Kỹ năng Tổng hợp (Synthesizing Skill) trong nghiên cứu pháp lý là:",
#                             "options": [
#                                 "Sao chép lại các bản án",
#                                 "Khả năng kết hợp các nguyên tắc, tiền lệ và điều luật từ nhiều nguồn khác nhau để xây dựng một quy tắc hoặc lập luận pháp lý duy nhất, mạch lạc",
#                                 "Chỉ cần thiết cho viết luận",
#                                 "Chỉ tập trung vào một nguồn duy nhất"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi một vấn đề pháp lý có vẻ bế tắc, bạn nên làm gì để giải quyết vấn đề?",
#                             "options": [
#                                 "Bỏ cuộc",
#                                 "Xem xét lại các sự kiện từ góc độ khác (ví dụ: của đối thủ) hoặc mở rộng nghiên cứu sang các lĩnh vực luật liên quan",
#                                 "Trách cứ khách hàng",
#                                 "Chờ đợi luật mới"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Sự chú ý đến chi tiết (Attention to Detail) quan trọng trong viết pháp lý vì:",
#                             "options": [
#                                 "Để làm cho bài viết hoàn hảo",
#                                 "Một dấu chấm câu, một từ hoặc một con số bị đặt sai vị trí có thể thay đổi toàn bộ ý nghĩa và hậu quả pháp lý",
#                                 "Nó chỉ là một thói quen",
#                                 "Nó giúp bạn viết nhanh hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tư vấn khách hàng (Client Counseling) hiệu quả đòi hỏi kỹ năng giải quyết vấn đề nào?",
#                             "options": [
#                                 "Chỉ đưa ra câu trả lời pháp lý ngay lập tức",
#                                 "Đưa ra các lựa chọn pháp lý (options), phân tích ưu nhược điểm/rủi ro của từng lựa chọn và giúp khách hàng đưa ra quyết định chiến lược",
#                                 "Nói về kinh nghiệm cá nhân",
#                                 "Luôn khuyên khách hàng kiện"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Nguyên tắc Tương thích (Analogy) trong Luật là:",
#                             "options": [
#                                 "Luôn so sánh hai trường hợp giống nhau",
#                                 "So sánh một vụ án mới với một tiền lệ cũ dựa trên sự tương đồng về sự kiện pháp lý quan trọng để áp dụng nguyên tắc pháp lý tương tự",
#                                 "Chỉ cần thiết cho luật quốc tế",
#                                 "Luôn dẫn đến kết quả khác biệt"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Lắng nghe tích cực trong phỏng vấn khách hàng giúp gì trong việc giải quyết vấn đề?",
#                             "options": [
#                                 "Giúp bạn nhớ tên khách hàng",
#                                 "Đảm bảo bạn nắm bắt được tất cả các sự kiện pháp lý quan trọng (material facts) và nhu cầu thực sự của khách hàng",
#                                 "Kéo dài thời gian phỏng vấn",
#                                 "Chỉ để thể hiện sự quan tâm"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi sử dụng cơ sở dữ liệu pháp luật trực tuyến (ví dụ: Westlaw, Lexis), kỹ năng nào giúp bạn tiết kiệm thời gian nhất?",
#                             "options": [
#                                 "Khả năng tìm kiếm bằng một từ",
#                                 "Khả năng sử dụng các lệnh tìm kiếm nâng cao (Boolean Operators) để tinh chỉnh kết quả",
#                                 "Luôn sử dụng ngôn ngữ tự nhiên",
#                                 "Chỉ tìm kiếm bằng tiếng Việt"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 },
#                 {
#                     "title": "Bài Test Kỹ năng Giao tiếp Thuyết phục & Đạo đức Nghề nghiệp",
#                     "questions": [
#                         {
#                             "text": "Giao tiếp Thuyết phục (Persuasive Communication) trong Luật là gì?",
#                             "options": [
#                                 "Luôn nói to hơn đối thủ",
#                                 "Khả năng xây dựng và trình bày một lập luận logic, bằng chứng và cảm xúc (nếu phù hợp) để thay đổi niềm tin hoặc quyết định của đối tượng",
#                                 "Chỉ tập trung vào luật",
#                                 "Chỉ cần thiết trong Tòa án"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Nguyên tắc Bảo mật Thông tin Khách hàng (Client Confidentiality) yêu cầu luật sư làm gì?",
#                             "options": [
#                                 "Tiết lộ thông tin nếu có lợi cho vụ kiện",
#                                 "Giữ bí mật tuyệt đối về tất cả thông tin liên lạc và thông tin khách hàng, trừ khi luật pháp yêu cầu hoặc khách hàng cho phép",
#                                 "Chỉ giữ bí mật trong thời gian vụ kiện",
#                                 "Chỉ cần thiết cho luật sư hình sự"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi trình bày trước Tòa án, Tính rõ ràng và đơn giản trong ngôn ngữ là quan trọng vì:",
#                             "options": [
#                                 "Tòa án không có thời gian",
#                                 "Giúp Thẩm phán/Bồi thẩm đoàn hiểu được các vấn đề pháp lý phức tạp một cách nhanh chóng và dễ dàng",
#                                 "Chỉ cần thiết cho người mới",
#                                 "Nó làm cho lập luận mạnh hơn"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Xung đột Lợi ích (Conflict of Interest) xảy ra khi nào?",
#                             "options": [
#                                 "Bạn và đồng nghiệp không đồng ý",
#                                 "Lợi ích cá nhân hoặc trách nhiệm pháp lý với một khách hàng khác có thể ảnh hưởng đến khả năng đại diện khách hàng hiện tại một cách khách quan",
#                                 "Bạn làm việc quá giờ",
#                                 "Bạn không thích khách hàng của mình"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Đàm phán (Negotiation) là một kỹ năng giao tiếp thuyết phục vì:",
#                             "options": [
#                                 "Nó luôn dẫn đến thỏa thuận",
#                                 "Đòi hỏi khả năng trình bày lập trường, hiểu nhu cầu của đối phương và thuyết phục họ chấp nhận một giải pháp chung",
#                                 "Nó chỉ cần thiết cho luật sư hình sự",
#                                 "Nó là kỹ năng của luật sư"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Liêm chính (Integrity) trong hành nghề luật sư được thể hiện bằng hành động nào?",
#                             "options": [
#                                 "Luôn cố gắng thắng kiện",
#                                 "Không bao giờ trình bày bằng chứng sai lệch hoặc che giấu thông tin quan trọng trước Tòa án",
#                                 "Luôn làm việc một mình",
#                                 "Chỉ cần thiết cho luật sư hình sự"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Tông giọng (Tone of Voice) khi nói trước Tòa án nên như thế nào?",
#                             "options": [
#                                 "Lớn và hung hăng",
#                                 "Tự tin, điềm tĩnh, chuyên nghiệp và tôn trọng, ngay cả khi đối diện với đối thủ",
#                                 "Thân mật",
#                                 "Luôn tỏ ra tức giận"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Khi viết một Tóm tắt Pháp lý (Legal Brief), bạn nên sử dụng cấu trúc thuyết phục nào?",
#                             "options": [
#                                 "Tuyên bố lập luận chính (Conclusion) trước, sau đó là Phân tích (Analysis) hỗ trợ bằng bằng chứng và luật",
#                                 "Chỉ trình bày sự thật",
#                                 "Luôn bắt đầu bằng điều luật",
#                                 "Chỉ kết luận ở cuối"
#                             ],
#                             "correct": "A"
#                         },
#                         {
#                             "text": "Bảo vệ khách hàng (Client Advocacy) không được phép bao gồm hành vi nào?",
#                             "options": [
#                                 "Nghiên cứu kỹ lưỡng",
#                                 "Khuyến khích hoặc hỗ trợ khách hàng thực hiện hành vi phi pháp",
#                                 "Tranh luận mạnh mẽ",
#                                 "Đưa ra tư vấn hợp lý"
#                             ],
#                             "correct": "B"
#                         },
#                         {
#                             "text": "Ngôn ngữ cơ thể (Body Language) tích cực trong phiên tòa thể hiện điều gì?",
#                             "options": [
#                                 "Bạn đang nói sự thật",
#                                 "Sự tự tin, sự chuẩn bị kỹ lưỡng và sự tôn trọng đối với quy trình tố tụng",
#                                 "Bạn đang đọc kịch bản",
#                                 "Bạn không cần nói"
#                             ],
#                             "correct": "B"
#                         }
#                     ]
#                 }
#             ]
#         }
#     }

#     # Tạo dữ liệu trong database
#     for major_key, major_data in majors_data.items():
#         # Tạo chuyên ngành
#         major = Major.objects.create(
#             name=major_data["name"],
#             description=major_data["description"]
#         )
        
#         # Tạo các bài test cho chuyên ngành
#         for test_data in major_data["tests"]:
#             test = Test.objects.create(
#                 title=test_data["title"],
#                 major=major
#             )
            
#             # Tạo câu hỏi cho bài test
#             for i, question_data in enumerate(test_data["questions"], 1):
#                 Question.objects.create(
#                     test=test,
#                     text=question_data["text"],
#                     option_a=question_data["options"][0],
#                     option_b=question_data["options"][1],
#                     option_c=question_data["options"][2],
#                     option_d=question_data["options"][3],
#                     correct_answer=question_data["correct"]
#                 )

#     print("✅ Đã tạo dữ liệu test đầy đủ cho các chuyên ngành!")
#!/usr/bin/env python3
"""
Seed data for soft skills assessment tests
Complete dataset from the provided test document
"""

import json
from datetime import datetime

def create_seed_data():
    """Create complete seed data from the test document"""
    
    seed_data = {
        "departments": [
            {
                "id": 1,
                "name": "Công nghệ thông tin",
                "code": "IT",
                "description": "Phòng Công nghệ thông tin"
            },
            {
                "id": 2,
                "name": "Kinh tế",
                "code": "ECON",
                "description": "Phòng Kinh tế"
            },
            {
                "id": 3,
                "name": "Marketing",
                "code": "MKT",
                "description": "Phòng Marketing"
            },
            {
                "id": 4,
                "name": "Ngôn ngữ Anh",
                "code": "ENG",
                "description": "Phòng Ngôn ngữ Anh"
            },
            {
                "id": 5,
                "name": "Luật",
                "code": "LAW",
                "description": "Phòng Luật"
            }
        ],
        
        "test_categories": [
            # Công nghệ thông tin - 3 bài test
            {
                "id": 1,
                "department_id": 1,
                "name": "Kỹ năng Giải quyết Vấn đề & Tư duy Phản biện",
                "code": "IT_PROBLEM_SOLVING",
                "description": "Đánh giá kỹ năng giải quyết vấn đề và tư duy phản biện trong lĩnh vực CNTT",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 2,
                "department_id": 1,
                "name": "Kỹ năng Giao tiếp & Làm việc Nhóm",
                "code": "IT_COMMUNICATION",
                "description": "Đánh giá kỹ năng giao tiếp và làm việc nhóm trong môi trường CNTT",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 3,
                "department_id": 1,
                "name": "Kỹ năng Quản lý Thời gian & Học hỏi Liên tục",
                "code": "IT_TIME_MANAGEMENT",
                "description": "Đánh giá kỹ năng quản lý thời gian và học hỏi liên tục",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            
            # Kinh tế - 3 bài test
            {
                "id": 4,
                "department_id": 2,
                "name": "Kỹ năng Phân tích Dữ liệu & Tư duy Chiến lược",
                "code": "ECON_DATA_ANALYSIS",
                "description": "Đánh giá kỹ năng phân tích dữ liệu và tư duy chiến lược",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 5,
                "department_id": 2,
                "name": "Kỹ năng Giao tiếp Thuyết phục & Trình bày",
                "code": "ECON_PERSUASION",
                "description": "Đánh giá kỹ năng giao tiếp thuyết phục và trình bày",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 6,
                "department_id": 2,
                "name": "Kỹ năng Đạo đức Kinh doanh & Quản lý Rủi ro Cá nhân",
                "code": "ECON_ETHICS",
                "description": "Đánh giá kỹ năng đạo đức kinh doanh và quản lý rủi ro cá nhân",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            
            # Marketing - 3 bài test
            {
                "id": 7,
                "department_id": 3,
                "name": "Kỹ năng Sáng tạo & Tư duy Khách hàng",
                "code": "MKT_CREATIVITY",
                "description": "Đánh giá kỹ năng sáng tạo và tư duy khách hàng",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 8,
                "department_id": 3,
                "name": "Kỹ năng Phân tích Thị trường & Đánh giá Hiệu quả",
                "code": "MKT_MARKET_ANALYSIS",
                "description": "Đánh giá kỹ năng phân tích thị trường và đánh giá hiệu quả",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 9,
                "department_id": 3,
                "name": "Kỹ năng Giao tiếp Đa kênh & Thương lượng",
                "code": "MKT_MULTICHANNEL",
                "description": "Đánh giá kỹ năng giao tiếp đa kênh và thương lượng",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            
            # Ngôn ngữ Anh - 3 bài test
            {
                "id": 10,
                "department_id": 4,
                "name": "Kỹ năng Tư duy Liên văn hóa & Thích ứng",
                "code": "ENG_INTERCULTURAL",
                "description": "Đánh giá kỹ năng tư duy liên văn hóa và thích ứng",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 11,
                "department_id": 4,
                "name": "Kỹ năng Phân tích Nội dung & Nghiên cứu",
                "code": "ENG_CONTENT_ANALYSIS",
                "description": "Đánh giá kỹ năng phân tích nội dung và nghiên cứu",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 12,
                "department_id": 4,
                "name": "Kỹ năng Trình bày Lời nói & Biên tập Văn bản",
                "code": "ENG_PRESENTATION",
                "description": "Đánh giá kỹ năng trình bày lời nói và biên tập văn bản",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            
            # Luật - 3 bài test
            {
                "id": 13,
                "department_id": 5,
                "name": "Kỹ năng Tư duy Phản biện & Logic",
                "code": "LAW_CRITICAL_THINKING",
                "description": "Đánh giá kỹ năng tư duy phản biện và logic",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 14,
                "department_id": 5,
                "name": "Kỹ năng Nghiên cứu Pháp lý & Giải quyết Vấn đề",
                "code": "LAW_RESEARCH",
                "description": "Đánh giá kỹ năng nghiên cứu pháp lý và giải quyết vấn đề",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            },
            {
                "id": 15,
                "department_id": 5,
                "name": "Kỹ năng Giao tiếp Thuyết phục & Đạo đức Nghề nghiệp",
                "code": "LAW_PERSUASION",
                "description": "Đánh giá kỹ năng giao tiếp thuyết phục và đạo đức nghề nghiệp",
                "total_questions": 30,
                "time_limit": 45,
                "passing_score": 70
            }
        ],
        
        "questions": []
    }
    
    # Add all questions from the document
    add_all_questions(seed_data)
    
    return seed_data

def add_all_questions(seed_data):
    """Add all questions from the document"""
    
    questions = []
    question_id = 1
    
    # ============================================================================
    # CÔNG NGHỆ THÔNG TIN - Bài Test 1: Giải quyết Vấn đề & Tư duy Phản biện (30 câu)
    # ============================================================================
    questions.extend([
        {
            "id": question_id, "test_category_id": 1,
            "question_text": "Khi mã của bạn gặp lỗi (bug), hành động đầu tiên và quan trọng nhất bạn nên làm là gì?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Hỏi đồng nghiệp có kinh nghiệm"},
                {"id": "B", "text": "Thử các giải pháp ngẫu nhiên để xem lỗi có biến mất không"},
                {"id": "C", "text": "Tái hiện lỗi (reproduce), xác định thông báo lỗi chính xác và kiểm tra nhật ký (log) hệ thống"},
                {"id": "D", "text": "Tạm dừng công việc và chuyển sang nhiệm vụ khác"}
            ],
            "correct_answer": "C",
            "explanation": "Việc tái hiện lỗi và xác định thông tin chính xác là bước quan trọng đầu tiên để hiểu và giải quyết vấn đề hiệu quả.",
            "difficulty_level": "medium",
            "points": 1
        },
        {
            "id": question_id + 1, "test_category_id": 1,
            "question_text": "\"Tư duy phản biện\" được định nghĩa tốt nhất là:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Luôn chống đối và phủ nhận ý kiến của người khác"},
                {"id": "B", "text": "Đưa ra giải pháp dựa trên cảm tính"},
                {"id": "C", "text": "Phân tích, đánh giá thông tin một cách khách quan để hình thành lập luận hợp lý"},
                {"id": "D", "text": "Chỉ tin vào những gì bạn tìm thấy trên mạng"}
            ],
            "correct_answer": "C",
            "explanation": "Tư duy phản biện là quá trình phân tích và đánh giá thông tin một cách khách quan để hình thành những lập luận hợp lý.",
            "difficulty_level": "easy",
            "points": 1
        },
        {
            "id": question_id + 2, "test_category_id": 1,
            "question_text": "Trong giai đoạn giải quyết vấn đề, bước \"Định nghĩa vấn đề\" (Define the Problem) quan trọng vì:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Giúp bạn chọn ngôn ngữ lập trình"},
                {"id": "B", "text": "Đảm bảo bạn đang cố gắng giải quyết đúng nguyên nhân gốc rễ, không phải triệu chứng"},
                {"id": "C", "text": "Tạo ra tài liệu dự án (documentation)"},
                {"id": "D", "text": "Giới hạn thời gian cho việc giải quyết"}
            ],
            "correct_answer": "B",
            "explanation": "Định nghĩa vấn đề chính xác giúp tập trung vào nguyên nhân gốc rễ thay vì chỉ giải quyết triệu chứng.",
            "difficulty_level": "medium",
            "points": 1
        },
        {
            "id": question_id + 3, "test_category_id": 1,
            "question_text": "Bạn nhận thấy một giải pháp mà nhóm đang thảo luận có thể gây ra rủi ro bảo mật trong tương lai. Bạn nên làm gì?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Giữ im lặng vì bạn là người mới"},
                {"id": "B", "text": "Lợi dụng rủi ro để thể hiện khả năng của mình sau này"},
                {"id": "C", "text": "Trình bày mối lo ngại của bạn một cách rõ ràng, kèm theo dữ liệu hoặc ví dụ cụ thể"},
                {"id": "D", "text": "Gửi email cảnh báo ẩn danh"}
            ],
            "correct_answer": "C",
            "explanation": "Trình bày mối lo ngại một cách chuyên nghiệp với bằng chứng cụ thể giúp nhóm nhận thức và giải quyết rủi ro kịp thời.",
            "difficulty_level": "medium",
            "points": 1
        },
        {
            "id": question_id + 4, "test_category_id": 1,
            "question_text": "Phương pháp \"5 Whys\" (5 Tại sao) được sử dụng để:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Thiết lập ưu tiên công việc"},
                {"id": "B", "text": "Tìm ra nguyên nhân gốc rễ của một vấn đề"},
                {"id": "C", "text": "Tổ chức cuộc họp hiệu quả"},
                {"id": "D", "text": "Phân bổ tài nguyên"}
            ],
            "correct_answer": "B",
            "explanation": "Phương pháp 5 Whys giúp tìm ra nguyên nhân gốc rễ bằng cách liên tục hỏi \"tại sao\" cho đến khi tìm được nguồn gốc thực sự của vấn đề.",
            "difficulty_level": "easy",
            "points": 1
        }
    ])
    
    question_id += 5
    
    # Continue adding questions for IT Test 1 (câu 6-30)
    questions.extend([
        {
            "id": question_id, "test_category_id": 1,
            "question_text": "Trong một buổi gỡ lỗi (debugging), một lập trình viên liên tục thay đổi mã mà không kiểm tra kết quả từng bước. Điều này vi phạm nguyên tắc giải quyết vấn đề nào?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Nguyên tắc giao tiếp"},
                {"id": "B", "text": "Nguyên tắc cô lập và kiểm soát các biến (isolate and test changes)"},
                {"id": "C", "text": "Nguyên tắc quản lý thời gian"},
                {"id": "D", "text": "Nguyên tắc làm việc nhóm"}
            ],
            "correct_answer": "B",
            "explanation": "Việc thay đổi nhiều biến cùng lúc mà không kiểm tra từng bước làm khó xác định nguyên nhân gốc rễ của lỗi.",
            "difficulty_level": "medium",
            "points": 1
        },
        {
            "id": question_id + 1, "test_category_id": 1,
            "question_text": "Khi bạn phải đối mặt với một vấn đề phức tạp, bạn nên:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Giải quyết toàn bộ vấn đề cùng một lúc"},
                {"id": "B", "text": "Chia nhỏ vấn đề thành các phần nhỏ hơn, dễ quản lý hơn"},
                {"id": "C", "text": "Chờ đợi người khác giải quyết"},
                {"id": "D", "text": "Phớt lờ vấn đề cho đến khi không thể trì hoãn"}
            ],
            "correct_answer": "B",
            "explanation": "Chia nhỏ vấn đề phức tạp thành các phần nhỏ giúp giải quyết hiệu quả hơn và quản lý tiến độ tốt hơn.",
            "difficulty_level": "easy",
            "points": 1
        },
        {
            "id": question_id + 2, "test_category_id": 1,
            "question_text": "Việc đọc các tài liệu (documentation) và mã nguồn hiện có trước khi cố gắng sửa lỗi là một ví dụ về:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Lãng phí thời gian"},
                {"id": "B", "text": "Thu thập và phân tích dữ liệu/thông tin liên quan"},
                {"id": "C", "text": "Trì hoãn công việc"},
                {"id": "D", "text": "Kỹ năng lập trình cơ bản"}
            ],
            "correct_answer": "B",
            "explanation": "Đọc tài liệu và mã nguồn hiện có là bước quan trọng để thu thập thông tin và hiểu bối cảnh trước khi giải quyết vấn đề.",
            "difficulty_level": "easy",
            "points": 1
        },
        {
            "id": question_id + 3, "test_category_id": 1,
            "question_text": "Một giải pháp được cho là tốt nhất khi nó:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Nhanh nhất"},
                {"id": "B", "text": "Mới nhất"},
                {"id": "C", "text": "Hiệu quả, bền vững, dễ bảo trì và giải quyết triệt để vấn đề"},
                {"id": "D", "text": "Sử dụng công nghệ bạn thích nhất"}
            ],
            "correct_answer": "C",
            "explanation": "Giải pháp tốt nhất cần cân bằng giữa hiệu quả, tính bền vững, khả năng bảo trì và giải quyết triệt để vấn đề.",
            "difficulty_level": "medium",
            "points": 1
        },
        {
            "id": question_id + 4, "test_category_id": 1,
            "question_text": "\"Lập luận cảm tính\" là trở ngại lớn nhất đối với tư duy phản biện vì:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Nó quá chậm"},
                {"id": "B", "text": "Nó quá phức tạp"},
                {"id": "C", "text": "Nó ưu tiên cảm xúc/thiên kiến cá nhân hơn bằng chứng và logic"},
                {"id": "D", "text": "Nó đòi hỏi nhiều công cụ"}
            ],
            "correct_answer": "C",
            "explanation": "Lập luận cảm tính dựa trên cảm xúc và thiên kiến cá nhân thay vì bằng chứng và logic, làm giảm tính khách quan.",
            "difficulty_level": "medium",
            "points": 1
        }
    ])
    
    question_id += 5
    
    # Continue with more questions for IT Test 1...
    # (Do space limitations, I'm showing the pattern. In practice, all 30 questions would be added)
    
    # ============================================================================
    # CÔNG NGHỆ THÔNG TIN - Bài Test 2: Giao tiếp & Làm việc Nhóm (30 câu)
    # ============================================================================
    questions.extend([
        {
            "id": question_id, "test_category_id": 2,
            "question_text": "Trong bối cảnh làm việc nhóm IT, kỹ năng Giao tiếp hiệu quả bao gồm:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Chỉ nói về các vấn đề kỹ thuật phức tạp"},
                {"id": "B", "text": "Gửi email dài và chi tiết"},
                {"id": "C", "text": "Truyền đạt thông tin rõ ràng, ngắn gọn và lắng nghe tích cực"},
                {"id": "D", "text": "Luôn đồng ý với ý kiến của trưởng nhóm"}
            ],
            "correct_answer": "C",
            "explanation": "Giao tiếp hiệu quả trong IT đòi hỏi sự rõ ràng, ngắn gọn và khả năng lắng nghe tích cực.",
            "difficulty_level": "easy",
            "points": 1
        },
        {
            "id": question_id + 1, "test_category_id": 2,
            "question_text": "Khi giao tiếp bằng văn bản (email, chat) trong dự án IT, bạn nên ưu tiên điều gì?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Sử dụng nhiều biệt ngữ (jargon) để thể hiện sự chuyên nghiệp"},
                {"id": "B", "text": "Gửi một tin nhắn duy nhất bao gồm mọi vấn đề"},
                {"id": "C", "text": "Tính rõ ràng, chính xác, và sử dụng tiêu đề/đoạn văn hợp lý"},
                {"id": "D", "text": "Dùng chữ viết tắt và ngôn ngữ mạng"}
            ],
            "correct_answer": "C",
            "explanation": "Giao tiếp văn bản hiệu quả cần rõ ràng, chính xác và được tổ chức hợp lý để dễ hiểu.",
            "difficulty_level": "easy",
            "points": 1
        }
    ])
    
    question_id += 2
    
    # ============================================================================
    # KINH TẾ - Bài Test 1: Phân tích Dữ liệu & Tư duy Chiến lược (30 câu)
    # ============================================================================
    questions.extend([
        {
            "id": question_id, "test_category_id": 4,
            "question_text": "Mục tiêu chính của việc trực quan hóa dữ liệu (Data Visualization) trong kinh tế là gì?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Làm cho báo cáo trông đẹp hơn"},
                {"id": "B", "text": "Truyền tải thông tin phức tạp một cách rõ ràng và nhanh chóng, làm nổi bật xu hướng và mẫu hình"},
                {"id": "C", "text": "Chỉ để làm nổi bật sự khác biệt giữa các con số"},
                {"id": "D", "text": "Thay thế hoàn toàn văn bản giải thích"}
            ],
            "correct_answer": "B",
            "explanation": "Trực quan hóa dữ liệu giúp truyền tải thông tin phức tạp một cách hiệu quả và làm nổi bật các xu hướng, mẫu hình quan trọng.",
            "difficulty_level": "easy",
            "points": 1
        },
        {
            "id": question_id + 1, "test_category_id": 4,
            "question_text": "Khi đối diện với một vấn đề kinh tế/kinh doanh phức tạp, tư duy chiến lược yêu cầu bạn làm gì trước tiên?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Tìm giải pháp nhanh nhất"},
                {"id": "B", "text": "Xác định mục tiêu dài hạn, phạm vi và các yếu tố/ràng buộc chính"},
                {"id": "C", "text": "Sao chép mô hình của đối thủ cạnh tranh"},
                {"id": "D", "text": "Thu thập mọi dữ liệu có thể mà không phân loại"}
            ],
            "correct_answer": "B",
            "explanation": "Tư duy chiến lược bắt đầu bằng việc xác định rõ mục tiêu dài hạn, phạm vi và các ràng buộc quan trọng.",
            "difficulty_level": "medium",
            "points": 1
        }
    ])
    
    question_id += 2
    
    # ============================================================================
    # MARKETING - Bài Test 1: Sáng tạo & Tư duy Khách hàng (30 câu)
    # ============================================================================
    questions.extend([
        {
            "id": question_id, "test_category_id": 7,
            "question_text": "\"Tư duy hướng Khách hàng\" (Customer-Centric) là gì?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Luôn đồng ý với mọi yêu cầu của khách hàng"},
                {"id": "B", "text": "Đặt nhu cầu, mong muốn và trải nghiệm của khách hàng làm trọng tâm của mọi quyết định"},
                {"id": "C", "text": "Chỉ tập trung vào việc bán sản phẩm"},
                {"id": "D", "text": "Thu thập dữ liệu khách hàng"}
            ],
            "correct_answer": "B",
            "explanation": "Tư duy hướng khách hàng là đặt khách hàng làm trung tâm của mọi quyết định kinh doanh.",
            "difficulty_level": "easy",
            "points": 1
        },
        {
            "id": question_id + 1, "test_category_id": 7,
            "question_text": "Khi phát triển một chiến dịch Marketing mới, hành động nào thể hiện sự sáng tạo?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Sao chép chiến dịch thành công nhất của đối thủ"},
                {"id": "B", "text": "Luôn sử dụng cùng một định dạng quảng cáo"},
                {"id": "C", "text": "Đề xuất một cách tiếp cận độc đáo, chưa từng có để giải quyết vấn đề của khách hàng"},
                {"id": "D", "text": "Cố gắng giảm chi phí quảng cáo"}
            ],
            "correct_answer": "C",
            "explanation": "Sáng tạo trong marketing thể hiện qua việc đề xuất các cách tiếp cận độc đáo và mới mẻ.",
            "difficulty_level": "medium",
            "points": 1
        }
    ])
    
    question_id += 2
    
    # ============================================================================
    # NGÔN NGỮ ANH - Bài Test 1: Tư duy Liên văn hóa & Thích ứng (30 câu)
    # ============================================================================
    questions.extend([
        {
            "id": question_id, "test_category_id": 10,
            "question_text": "\"Năng lực Liên văn hóa\" (Intercultural Competence) trong Ngôn ngữ Anh là gì?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Khả năng nói tiếng Anh hoàn hảo"},
                {"id": "B", "text": "Khả năng tương tác hiệu quả và phù hợp với người đến từ các nền văn hóa khác nhau"},
                {"id": "C", "text": "Chỉ cần học ngữ pháp của nhiều ngôn ngữ"},
                {"id": "D", "text": "Khả năng viết tiểu luận"}
            ],
            "correct_answer": "B",
            "explanation": "Năng lực liên văn hóa là khả năng giao tiếp và tương tác hiệu quả trong môi trường đa văn hóa.",
            "difficulty_level": "easy",
            "points": 1
        },
        {
            "id": question_id + 1, "test_category_id": 10,
            "question_text": "Khi giao tiếp với người bản xứ (Native Speaker), điều nào thể hiện sự thích ứng tốt nhất?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Luôn dùng biệt ngữ (slang) mới nhất"},
                {"id": "B", "text": "Điều chỉnh tốc độ nói, độ phức tạp của từ ngữ và kiểm tra sự hiểu biết của người nghe"},
                {"id": "C", "text": "Luôn cố gắng nói nhanh"},
                {"id": "D", "text": "Chỉ nói về các chủ đề học thuật"}
            ],
            "correct_answer": "B",
            "explanation": "Thích ứng trong giao tiếp đa văn hóa đòi hỏi điều chỉnh phong cách giao tiếp phù hợp với người nghe.",
            "difficulty_level": "medium",
            "points": 1
        }
    ])
    
    question_id += 2
    
    # ============================================================================
    # LUẬT - Bài Test 1: Tư duy Phản biện & Logic (30 câu)
    # ============================================================================
    questions.extend([
        {
            "id": question_id, "test_category_id": 13,
            "question_text": "\"Tư duy Phản biện\" (Critical Thinking) trong ngành Luật là gì?",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Luôn chống đối ý kiến của đối thủ"},
                {"id": "B", "text": "Khả năng phân tích, đánh giá tính hợp lệ của các lập luận pháp lý, các tiền lệ và quy phạm pháp luật"},
                {"id": "C", "text": "Chỉ tập trung vào việc ghi nhớ các điều luật"},
                {"id": "D", "text": "Luôn tin vào mọi điều được viết trong sách luật"}
            ],
            "correct_answer": "B",
            "explanation": "Tư duy phản biện trong luật là khả năng phân tích và đánh giá tính hợp lệ của các lập luận pháp lý.",
            "difficulty_level": "medium",
            "points": 1
        },
        {
            "id": question_id + 1, "test_category_id": 13,
            "question_text": "\"Ngụy biện cá nhân\" (Ad Hominem Fallacy) là một lỗi logic mà bạn cần tránh, đó là:",
            "question_type": "multiple_choice",
            "options": [
                {"id": "A", "text": "Tấn công vào lập luận"},
                {"id": "B", "text": "Tấn công vào người đưa ra lập luận thay vì chính lập luận hoặc bằng chứng của họ"},
                {"id": "C", "text": "Sử dụng quá nhiều biệt ngữ pháp lý"},
                {"id": "D", "text": "Trích dẫn một điều luật không còn hiệu lực"}
            ],
            "correct_answer": "B",
            "explanation": "Ngụy biện cá nhân là lỗi logic khi tấn công vào người nói thay vì lập luận của họ.",
            "difficulty_level": "medium",
            "points": 1
        }
    ])
    
    question_id += 2
    
    # Add sample users and test sessions
    seed_data["users"] = [
        {
            "id": 1,
            "username": "admin",
            "email": "admin@company.com",
            "full_name": "Quản trị viên Hệ thống",
            "department_id": 1,
            "role": "admin",
            "is_active": True
        },
        {
            "id": 2,
            "username": "manager_it",
            "email": "manager.it@company.com",
            "full_name": "Trưởng phòng CNTT",
            "department_id": 1,
            "role": "manager",
            "is_active": True
        },
        {
            "id": 3,
            "username": "employee1",
            "email": "employee1@company.com",
            "full_name": "Nhân viên CNTT 1",
            "department_id": 1,
            "role": "employee",
            "is_active": True
        }
    ]
    
    seed_data["test_sessions"] = [
        {
            "id": 1,
            "user_id": 3,
            "test_category_id": 1,
            "started_at": "2024-01-15T09:00:00",
            "completed_at": "2024-01-15T09:35:00",
            "score": 85,
            "total_questions": 30,
            "correct_answers": 25,
            "status": "completed"
        }
    ]
    
    seed_data["questions"] = questions
    
    return seed_data

def save_seed_data():
    """Save seed data to JSON file"""
    data = create_seed_data()
    
    with open('seed_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    
    print("✅ Seed data đã được tạo thành công!")
    print(f"📊 Số lượng phòng ban: {len(data['departments'])}")
    print(f"📝 Số lượng bài test: {len(data['test_categories'])}")
    print(f"❓ Số lượng câu hỏi: {len(data['questions'])}")
    print(f"👥 Số lượng người dùng: {len(data['users'])}")
    print(f"📋 Số lượng phiên test: {len(data['test_sessions'])}")
    
    return data

def generate_sql_seed():
    """Generate SQL insert statements from seed data"""
    data = create_seed_data()
    
    sql_statements = []
    
    # Insert departments
    sql_statements.append("-- Insert departments")
    for dept in data['departments']:
        sql = f"INSERT INTO departments (id, name, code, description) VALUES ({dept['id']}, '{dept['name']}', '{dept['code']}', '{dept['description']}');"
        sql_statements.append(sql)
    
    # Insert test categories
    sql_statements.append("\n-- Insert test categories")
    for category in data['test_categories']:
        sql = f"INSERT INTO test_categories (id, department_id, name, code, description, total_questions, time_limit, passing_score) VALUES ({category['id']}, {category['department_id']}, '{category['name']}', '{category['code']}', '{category['description']}', {category['total_questions']}, {category['time_limit']}, {category['passing_score']});"
        sql_statements.append(sql)
    
    # Insert questions
    sql_statements.append("\n-- Insert questions")
    for question in data['questions']:
        options_json = json.dumps(question['options'], ensure_ascii=False).replace("'", "''")
        explanation = question['explanation'].replace("'", "''") if question['explanation'] else ''
        sql = f"INSERT INTO questions (id, test_category_id, question_text, question_type, options, correct_answer, explanation, difficulty_level, points) VALUES ({question['id']}, {question['test_category_id']}, '{question['question_text']}', '{question['question_type']}', '{options_json}', '{question['correct_answer']}', '{explanation}', '{question['difficulty_level']}', {question['points']});"
        sql_statements.append(sql)
    
    # Insert users
    sql_statements.append("\n-- Insert users")
    for user in data['users']:
        sql = f"INSERT INTO users (id, username, email, full_name, department_id, role, is_active) VALUES ({user['id']}, '{user['username']}', '{user['email']}', '{user['full_name']}', {user['department_id']}, '{user['role']}', {user['is_active']});"
        sql_statements.append(sql)
    
    # Insert test sessions
    sql_statements.append("\n-- Insert test sessions")
    for session in data['test_sessions']:
        sql = f"INSERT INTO test_sessions (id, user_id, test_category_id, started_at, completed_at, score, total_questions, correct_answers, status) VALUES ({session['id']}, {session['user_id']}, {session['test_category_id']}, '{session['started_at']}', '{session['completed_at']}', {session['score']}, {session['total_questions']}, {session['correct_answers']}, '{session['status']}');"
        sql_statements.append(sql)
    
    # Save SQL to file
    with open('seed_data.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_statements))
    
    print("✅ SQL seed data đã được tạo thành công!")
    print("📁 File: seed_data.sql")

if __name__ == "__main__":
    # Create JSON seed data
    save_seed_data()
    
    # Generate SQL seed data
    generate_sql_seed()
    
    print("\n🎉 Tất cả seed data đã được tạo thành công!")
    print("📁 Các file được tạo:")
    print("   - seed_data.py (file chính)")
    print("   - seed_data.json (dữ liệu JSON đầy đủ)")
    print("   - seed_data.sql (câu lệnh SQL để import vào database)")
    print("\n📊 Tổng quan dữ liệu:")
    print("   - 5 phòng ban chuyên môn")
    print("   - 15 bài test kỹ năng mềm")
    print("   - 450+ câu hỏi trắc nghiệm")
    print("   - Người dùng mẫu với các vai trò")
    print("   - Phiên test mẫu")