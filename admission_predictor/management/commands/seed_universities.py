import os
import sys
import django
from django.core.management.base import BaseCommand

# Setup Django environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')
django.setup()

from admission_predictor.models import University, Major

class Command(BaseCommand):
    help = 'Seed database with sample universities and majors data for admission_predictor app'
    
    def handle(self, *args, **kwargs):
        self.stdout.write('🎓 Đang thêm dữ liệu mẫu các trường đại học...')
        
        universities_data = [
            {
                'name': 'Đại học Bách Khoa Hà Nội',
                'code': 'HUST',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://hust.edu.vn'
            },
            {
                'name': 'Đại học Kinh tế Quốc dân',
                'code': 'NEU',
                'location': 'Hà Nội', 
                'type': 'public',
                'website': 'https://neu.edu.vn'
            },
            {
                'name': 'Đại học Ngoại thương',
                'code': 'FTU',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://ftu.edu.vn'
            },
            {
                'name': 'Đại học Y Hà Nội',
                'code': 'HMU',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://hmu.edu.vn'
            },
            {
                'name': 'Đại học Sư phạm Hà Nội',
                'code': 'HNUE',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://hnue.edu.vn'
            },
            {
                'name': 'Đại học Công nghệ - ĐHQG Hà Nội',
                'code': 'UET',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://uet.vnu.edu.vn'
            },
            {
                'name': 'Đại học Khoa học Tự nhiên - ĐHQG Hà Nội',
                'code': 'HUS',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://hus.vnu.edu.vn'
            },
            {
                'name': 'Đại học Khoa học Xã hội & Nhân văn - ĐHQG Hà Nội',
                'code': 'USSH',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://ussh.vnu.edu.vn'
            },
            {
                'name': 'Học viện Báo chí và Tuyên truyền',
                'code': 'AJCC',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://ajc.edu.vn'
            },
            {
                'name': 'Đại học Thương mại',
                'code': 'TMU',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://tmu.edu.vn'
            },
            {
                'name': 'Đại học Giao thông Vận tải',
                'code': 'UTC',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://utc.edu.vn'
            },
            {
                'name': 'Đại học Xây dựng',
                'code': 'NUCE',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://nuce.edu.vn'
            },
            {
                'name': 'Đại học Bách Khoa TP.HCM',
                'code': 'HCMUT',
                'location': 'TP.HCM',
                'type': 'public',
                'website': 'https://hcmut.edu.vn'
            },
            {
                'name': 'Đại học Kinh tế TP.HCM',
                'code': 'UEH',
                'location': 'TP.HCM',
                'type': 'public',
                'website': 'https://ueh.edu.vn'
            },
            {
                'name': 'Đại học Y Dược TP.HCM',
                'code': 'UMP',
                'location': 'TP.HCM',
                'type': 'public',
                'website': 'https://ump.edu.vn'
            },
            {
                'name': 'Đại học Sư phạm TP.HCM',
                'code': 'HCMUE',
                'location': 'TP.HCM',
                'type': 'public',
                'website': 'https://hcmue.edu.vn'
            },
            {
                'name': 'Đại học Cần Thơ',
                'code': 'CTU',
                'location': 'Cần Thơ',
                'type': 'public',
                'website': 'https://ctu.edu.vn'
            },
            {
                'name': 'Đại học Đà Nẵng',
                'code': 'UD',
                'location': 'Đà Nẵng',
                'type': 'public',
                'website': 'https://udn.vn'
            },
            {
                'name': 'Đại học FPT',
                'code': 'FPTU',
                'location': 'Hà Nội',
                'type': 'private',
                'website': 'https://fpt.edu.vn'
            },
            {
                'name': 'Đại học RMIT Việt Nam',
                'code': 'RMIT',
                'location': 'TP.HCM',
                'type': 'private',
                'website': 'https://rmit.edu.vn'
            },
            # Thêm các trường mới từ bảng
            {
                'name': 'Đại học Dược Hà Nội',
                'code': 'HUP',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://hup.edu.vn'
            },
            {
                'name': 'Đại học Quốc gia Hà Nội',
                'code': 'VNU',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://vnu.edu.vn'
            },
            {
                'name': 'Học viện Ngân hàng',
                'code': 'BA',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://hvnh.edu.vn'
            },
            {
                'name': 'Đại học Luật Hà Nội',
                'code': 'HLU',
                'location': 'Hà Nội',
                'type': 'public',
                'website': 'https://hlu.edu.vn'
            },
            {
                'name': 'Đại học Quốc gia TP.HCM',
                'code': 'VNUHCM',
                'location': 'TP.HCM',
                'type': 'public',
                'website': 'https://vnuhcm.edu.vn'
            },
            {
                'name': 'Đại học Sư phạm Kỹ thuật TP.HCM',
                'code': 'HCMUTE',
                'location': 'TP.HCM',
                'type': 'public',
                'website': 'https://hcmute.edu.vn'
            },
            {
                'name': 'Đại học Tôn Đức Thắng',
                'code': 'TDTU',
                'location': 'TP.HCM',
                'type': 'public',
                'website': 'https://tdtu.edu.vn'
            }
        ]
        
        # Tạo các trường đại học
        universities = {}
        for uni_data in universities_data:
            uni, created = University.objects.get_or_create(
                code=uni_data['code'],
                defaults=uni_data
            )
            universities[uni_data['code']] = uni
            if created:
                self.stdout.write(f'✅ Đã tạo: {uni.name}')
            else:
                self.stdout.write(f'⚠️ Đã tồn tại: {uni.name}')
        
        # Dữ liệu ngành học - ĐÃ CẬP NHẬT SANG KHỐI MỚI
        majors_data = [
            # Khối A00 (Toán, Lý, Hóa)
            {'code': 'CNTT', 'name': 'Công nghệ Thông tin', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.5, 'admission_quota': 200, 'university': 'HUST'},
            {'code': 'KTDT', 'name': 'Kỹ thuật Điện tử - Viễn thông', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 25.0, 'admission_quota': 150, 'university': 'HUST'},
            {'code': 'CK', 'name': 'Cơ khí', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 23.5, 'admission_quota': 180, 'university': 'HUST'},
            {'code': 'XD', 'name': 'Xây dựng', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 22.0, 'admission_quota': 120, 'university': 'NUCE'},
            {'code': 'CNTT_HCM', 'name': 'Công nghệ Thông tin', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.0, 'admission_quota': 250, 'university': 'HCMUT'},
            
            # Khối A01 (Toán, Lý, Anh)
            {'code': 'CNTT_A1', 'name': 'Công nghệ Thông tin', 'block': 'A01', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Anh', 'benchmark_2024': 25.5, 'admission_quota': 150, 'university': 'HUST'},
            {'code': 'KTDT_A1', 'name': 'Kỹ thuật Điện tử - Viễn thông', 'block': 'A01', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Anh', 'benchmark_2024': 24.0, 'admission_quota': 100, 'university': 'HUST'},
            {'code': 'CNTT_A1_HCM', 'name': 'Công nghệ Thông tin', 'block': 'A01', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Anh', 'benchmark_2024': 25.0, 'admission_quota': 200, 'university': 'HCMUT'},
            
            # Khối B00 (Toán, Hóa, Sinh)
            {'code': 'YD', 'name': 'Y đa khoa', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 28.5, 'admission_quota': 300, 'university': 'HMU'},
            {'code': 'RHM', 'name': 'Răng Hàm Mặt', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 27.5, 'admission_quota': 80, 'university': 'HMU'},
            {'code': 'DUOC', 'name': 'Dược học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 27.0, 'admission_quota': 150, 'university': 'HMU'},
            {'code': 'CNSH', 'name': 'Công nghệ Sinh học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 24.5, 'admission_quota': 100, 'university': 'HUS'},
            {'code': 'YD_HCM', 'name': 'Y đa khoa', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 28.0, 'admission_quota': 250, 'university': 'UMP'},
            
            # Khối C00 (Văn, Sử, Địa)
            {'code': 'LUAT', 'name': 'Luật', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 25.0, 'admission_quota': 200, 'university': 'USSH'},
            {'code': 'BAOCHI', 'name': 'Báo chí', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 26.5, 'admission_quota': 120, 'university': 'AJCC'},
            {'code': 'SPVAN', 'name': 'Sư phạm Ngữ văn', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 23.0, 'admission_quota': 80, 'university': 'HNUE'},
            {'code': 'SPSU', 'name': 'Sư phạm Lịch sử', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 21.5, 'admission_quota': 60, 'university': 'HNUE'},
            {'code': 'QLVH', 'name': 'Quản lý Văn hóa', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 20.0, 'admission_quota': 70, 'university': 'USSH'},
            
            # Khối D01 (Toán, Văn, Anh)
            {'code': 'QTKD', 'name': 'Quản trị Kinh doanh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.0, 'admission_quota': 180, 'university': 'NEU'},
            {'code': 'KTQT', 'name': 'Kinh tế Quốc tế', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 27.0, 'admission_quota': 150, 'university': 'FTU'},
            {'code': 'TA', 'name': 'Ngôn ngữ Anh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 25.5, 'admission_quota': 120, 'university': 'USSH'},
            {'code': 'TNDN', 'name': 'Tài chính - Ngân hàng', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 25.0, 'admission_quota': 160, 'university': 'NEU'},
            {'code': 'KT_D', 'name': 'Kế toán', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 24.5, 'admission_quota': 140, 'university': 'TMU'},
            {'code': 'QTKD_HCM', 'name': 'Quản trị Kinh doanh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 25.5, 'admission_quota': 200, 'university': 'UEH'},
            {'code': 'MARKETING', 'name': 'Marketing', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 24.0, 'admission_quota': 100, 'university': 'TMU'},
            
            # Khối D07 (Toán, Hóa, Anh)
            {'code': 'DUOC_D07', 'name': 'Dược học', 'block': 'D07', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Anh', 'benchmark_2024': 25.51, 'admission_quota': 200, 'university': 'HUP'},
            {'code': 'CNHH_D07', 'name': 'Công nghệ Hóa học', 'block': 'D07', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Anh', 'benchmark_2024': 22.0, 'admission_quota': 80, 'university': 'HUS'},
            {'code': 'KTHH_D07', 'name': 'Kỹ thuật Hóa học', 'block': 'D07', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Anh', 'benchmark_2024': 23.5, 'admission_quota': 100, 'university': 'HCMUT'},
            
            # Các ngành khác
            {'code': 'CNTT_FPT', 'name': 'Công nghệ Thông tin', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 21.0, 'admission_quota': 300, 'university': 'FPTU'},
            {'code': 'QTKD_FPT', 'name': 'Quản trị Kinh doanh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 20.5, 'admission_quota': 200, 'university': 'FPTU'},
            {'code': 'KTRM', 'name': 'Kinh doanh Quốc tế', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 22.0, 'admission_quota': 150, 'university': 'RMIT'},

            # Thêm các ngành mới từ bảng - ĐÃ CẬP NHẬT SANG KHỐI MỚI
            # ĐH Bách khoa Hà Nội (HUST)
            {'code': 'KHMT_HUST', 'name': 'Khoa học Máy tính', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 28.53, 'admission_quota': 120, 'university': 'HUST'},
            {'code': 'KTDT_TDH', 'name': 'Kỹ thuật Điều khiển & Tự động hóa', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 27.97, 'admission_quota': 100, 'university': 'HUST'},
            {'code': 'KTMT_HUST', 'name': 'Kỹ thuật Máy tính', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 28.48, 'admission_quota': 80, 'university': 'HUST'},
            {'code': 'KHDL_HUST', 'name': 'Khoa học Dữ liệu', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 28.22, 'admission_quota': 70, 'university': 'HUST'},
            {'code': 'KTO_HUST', 'name': 'Kỹ thuật Ô tô', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 27.28, 'admission_quota': 90, 'university': 'HUST'},

            # ĐH Kinh tế Quốc dân (NEU)
            {'code': 'QHCC_NEU', 'name': 'Quan hệ Công chúng', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 28.18, 'admission_quota': 80, 'university': 'NEU'},
            {'code': 'TMDT_NEU', 'name': 'Thương mại Điện tử', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 28.02, 'admission_quota': 100, 'university': 'NEU'},
            {'code': 'LOGISTICS_NEU', 'name': 'Logistics & QL Chuỗi Cung ứng', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 27.87, 'admission_quota': 90, 'university': 'NEU'},
            {'code': 'MARKETING_NEU', 'name': 'Marketing', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 27.90, 'admission_quota': 120, 'university': 'NEU'},
            {'code': 'KTQT_NEU', 'name': 'Kinh tế Quốc tế', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 27.85, 'admission_quota': 110, 'university': 'NEU'},

            # ĐH Ngoại thương (FTU)
            {'code': 'KT_FTU', 'name': 'Kinh tế', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 28.50, 'admission_quota': 150, 'university': 'FTU'},
            {'code': 'NNTRUNG_FTU', 'name': 'Ngôn ngữ Trung', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Trung', 'benchmark_2024': 37.7, 'admission_quota': 80, 'university': 'FTU'},
            {'code': 'QTKD_FTU', 'name': 'Quản trị Kinh doanh', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 28.40, 'admission_quota': 130, 'university': 'FTU'},
            {'code': 'KTQT_FTU', 'name': 'Kinh tế Quốc tế', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 28.30, 'admission_quota': 120, 'university': 'FTU'},
            {'code': 'LOGISTICS_FTU', 'name': 'Logistics & QL Chuỗi Cung ứng', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 28.20, 'admission_quota': 100, 'university': 'FTU'},

            # ĐH Y Hà Nội
            {'code': 'YKHOACD', 'name': 'Y khoa', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 27.60, 'admission_quota': 300, 'university': 'HMU'},
            {'code': 'RHAMMAT', 'name': 'Răng Hàm Mặt', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 27.40, 'admission_quota': 80, 'university': 'HMU'},
            {'code': 'YHCT', 'name': 'Y học Cổ truyền', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 25.40, 'admission_quota': 60, 'university': 'HMU'},
            {'code': 'YHDP', 'name': 'Y học Dự phòng', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 24.50, 'admission_quota': 70, 'university': 'HMU'},
            {'code': 'DDUONG', 'name': 'Điều dưỡng', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 23.50, 'admission_quota': 150, 'university': 'HMU'},

            # ĐH Dược Hà Nội
            {'code': 'DUOCHOC', 'name': 'Dược học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 25.51, 'admission_quota': 200, 'university': 'HUP'},
            {'code': 'HOADUOC', 'name': 'Hóa Dược', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 24.26, 'admission_quota': 80, 'university': 'HUP'},
            {'code': 'CNSH_HUP', 'name': 'Công nghệ Sinh học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 23.00, 'admission_quota': 60, 'university': 'HUP'},
            {'code': 'HOAHOC', 'name': 'Hóa học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 23.01, 'admission_quota': 50, 'university': 'HUP'},
            {'code': 'DUOCCLC', 'name': 'Dược học (Chất lượng cao)', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 24.50, 'admission_quota': 100, 'university': 'HUP'},

            # ĐH KHTN (VNU)
            {'code': 'KHMT_HUS', 'name': 'Khoa học Máy tính & Thông tin', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.25, 'admission_quota': 120, 'university': 'HUS'},
            {'code': 'KHDL_HUS', 'name': 'Khoa học Dữ liệu', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.00, 'admission_quota': 80, 'university': 'HUS'},
            {'code': 'TOANHOC', 'name': 'Toán học', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 24.00, 'admission_quota': 70, 'university': 'HUS'},
            {'code': 'CNKTHH', 'name': 'Công nghệ Kỹ thuật Hóa học', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 23.00, 'admission_quota': 60, 'university': 'HUS'},
            {'code': 'SINHHOC', 'name': 'Sinh học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 22.00, 'admission_quota': 80, 'university': 'HUS'},

            # ĐH KHXH&NV (VNU)
            {'code': 'TRUNGQUOC', 'name': 'Trung Quốc học', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 29.10, 'admission_quota': 60, 'university': 'USSH'},
            {'code': 'BAOCHI_USSH', 'name': 'Báo chí', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.90, 'admission_quota': 80, 'university': 'USSH'},
            {'code': 'QHCC_USSH', 'name': 'Quan hệ Công chúng', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.85, 'admission_quota': 70, 'university': 'USSH'},
            {'code': 'TAMLY', 'name': 'Tâm lý học', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.80, 'admission_quota': 65, 'university': 'USSH'},
            {'code': 'DONGPHUONG', 'name': 'Đông Phương học', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.75, 'admission_quota': 55, 'university': 'USSH'},

            # Học viện Ngân hàng
            {'code': 'LUATKT', 'name': 'Luật Kinh tế', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.40, 'admission_quota': 90, 'university': 'BA'},
            {'code': 'KETOAN_BA', 'name': 'Kế toán', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.10, 'admission_quota': 110, 'university': 'BA'},
            {'code': 'TCNH_BA', 'name': 'Tài chính Ngân hàng', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 25.80, 'admission_quota': 120, 'university': 'BA'},
            {'code': 'QTKD_BA', 'name': 'Quản trị Kinh doanh', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 25.75, 'admission_quota': 100, 'university': 'BA'},
            {'code': 'HTTTQL', 'name': 'Hệ thống thông tin quản lý', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 25.50, 'admission_quota': 80, 'university': 'BA'},

            # ĐH Luật Hà Nội
            {'code': 'LUATKT_HLU', 'name': 'Luật Kinh tế', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.85, 'admission_quota': 150, 'university': 'HLU'},
            {'code': 'LUAT_HLU', 'name': 'Luật', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 27.35, 'admission_quota': 200, 'university': 'HLU'},
            {'code': 'LTMQT', 'name': 'Luật Thương mại Quốc tế', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.50, 'admission_quota': 80, 'university': 'HLU'},
            {'code': 'LUTCLC', 'name': 'Luật Chất lượng cao', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.00, 'admission_quota': 100, 'university': 'HLU'},
            {'code': 'NNA_HLU', 'name': 'Ngôn ngữ Anh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.85, 'admission_quota': 60, 'university': 'HLU'},

            # Học viện Báo chí & TT
            {'code': 'TTDPT', 'name': 'Truyền thông Đa phương tiện', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 28.68, 'admission_quota': 70, 'university': 'AJCC'},
            {'code': 'BAOCHI_AJCC', 'name': 'Báo chí', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.50, 'admission_quota': 90, 'university': 'AJCC'},
            {'code': 'QHCC_AJCC', 'name': 'Quan hệ công chúng', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 28.50, 'admission_quota': 80, 'university': 'AJCC'},
            {'code': 'TTQT', 'name': 'Truyền thông Quốc tế', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 27.80, 'admission_quota': 60, 'university': 'AJCC'},
            {'code': 'QLNN', 'name': 'Quản lý Nhà nước', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 27.50, 'admission_quota': 75, 'university': 'AJCC'},

            # ĐH Bách khoa (VNU-HCM)
            {'code': 'KHMT_HCMUT', 'name': 'Khoa học Máy tính', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 78.07, 'admission_quota': 150, 'university': 'HCMUT'},
            {'code': 'KTMT_HCMUT', 'name': 'Kỹ thuật Máy tính', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 76.5, 'admission_quota': 120, 'university': 'HCMUT'},
            {'code': 'LOGISTICS_HCMUT', 'name': 'Logistics & QL Chuỗi Cung ứng', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 72.8, 'admission_quota': 100, 'university': 'HCMUT'},
            {'code': 'KTO_HCMUT', 'name': 'Kỹ thuật Ô tô', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 69.5, 'admission_quota': 90, 'university': 'HCMUT'},
            {'code': 'KTCK_HCMUT', 'name': 'Kỹ thuật Cơ khí', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 68.9, 'admission_quota': 110, 'university': 'HCMUT'},

            # ĐH Kinh tế TP.HCM (UEH)
            {'code': 'KDQT_UEH', 'name': 'Kinh doanh Quốc tế', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 27.20, 'admission_quota': 130, 'university': 'UEH'},
            {'code': 'MARKETING_UEH', 'name': 'Marketing', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 27.15, 'admission_quota': 120, 'university': 'UEH'},
            {'code': 'TMDT_UEH', 'name': 'Thương mại Điện tử', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 27.00, 'admission_quota': 100, 'university': 'UEH'},
            {'code': 'LOGISTICS_UEH', 'name': 'Logistics & QL Chuỗi Cung ứng', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.80, 'admission_quota': 90, 'university': 'UEH'},
            {'code': 'TCNH_UEH', 'name': 'Tài chính Ngân hàng', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.50, 'admission_quota': 140, 'university': 'UEH'},

            # ĐH KHXH&NV (VNU-HCM)
            {'code': 'BAOCHI_HCM', 'name': 'Báo chí', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.80, 'admission_quota': 85, 'university': 'HCMUE'},
            {'code': 'QLDV_DL', 'name': 'QL Dịch vụ Du lịch & Lữ hành', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.33, 'admission_quota': 70, 'university': 'HCMUE'},
            {'code': 'NNA_HCMUE', 'name': 'Ngôn ngữ Anh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.00, 'admission_quota': 100, 'university': 'HCMUE'},
            {'code': 'TAMLY_HCMUE', 'name': 'Tâm lý học', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 27.30, 'admission_quota': 65, 'university': 'HCMUE'},
            {'code': 'QHQT_HCMUE', 'name': 'Quan hệ Quốc tế', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 27.00, 'admission_quota': 60, 'university': 'HCMUE'},

            # ĐH Y Dược TP.HCM
            {'code': 'YKHOA_HCM', 'name': 'Y khoa', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 27.15, 'admission_quota': 280, 'university': 'UMP'},
            {'code': 'RHAMMAT_HCM', 'name': 'Răng Hàm Mặt', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 27.05, 'admission_quota': 75, 'university': 'UMP'},
            {'code': 'DUOC_HCM', 'name': 'Dược học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 25.75, 'admission_quota': 180, 'university': 'UMP'},
            {'code': 'YHCT_HCM', 'name': 'Y học Cổ truyền', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 24.3, 'admission_quota': 55, 'university': 'UMP'},
            {'code': 'KTXN', 'name': 'Kỹ thuật Xét nghiệm Y học', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 24.5, 'admission_quota': 80, 'university': 'UMP'},

            # ĐH Sư phạm Kỹ thuật TP.HCM
            {'code': 'ROBOT_AI', 'name': 'Robot và Trí tuệ Nhân tạo', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.75, 'admission_quota': 70, 'university': 'HCMUTE'},
            {'code': 'LOGISTICS_HCMUTE', 'name': 'Logistics & QL Chuỗi Cung ứng', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.50, 'admission_quota': 85, 'university': 'HCMUTE'},
            {'code': 'CNTT_HCMUTE', 'name': 'Công nghệ thông tin', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.00, 'admission_quota': 120, 'university': 'HCMUTE'},
            {'code': 'KTCĐT', 'name': 'Kỹ thuật Cơ điện tử', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 25.80, 'admission_quota': 90, 'university': 'HCMUTE'},
            {'code': 'CNOTO', 'name': 'Công nghệ Kỹ thuật Ô tô', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 25.50, 'admission_quota': 95, 'university': 'HCMUTE'},

            # ĐH Tôn Đức Thắng
            {'code': 'MARKETING_TDT', 'name': 'Marketing', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 37.0, 'admission_quota': 110, 'university': 'TDTU'},
            {'code': 'NNA_TDT', 'name': 'Ngôn ngữ Anh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 34.0, 'admission_quota': 90, 'university': 'TDTU'},
            {'code': 'QTKD_TDT', 'name': 'Quản trị Kinh doanh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 35.5, 'admission_quota': 130, 'university': 'TDTU'},
            {'code': 'LOGISTICS_TDT', 'name': 'Logistics & QL Chuỗi Cung ứng', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 36.5, 'admission_quota': 80, 'university': 'TDTU'},
            {'code': 'KTPM', 'name': 'Kỹ thuật phần mềm', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 35.0, 'admission_quota': 100, 'university': 'TDTU'},

            # ĐH Sư phạm Hà Nội
            {'code': 'SPLS', 'name': 'Sư phạm Lịch sử', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 29.30, 'admission_quota': 50, 'university': 'HNUE'},
            {'code': 'SPNV', 'name': 'Sư phạm Ngữ văn', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 28.60, 'admission_quota': 60, 'university': 'HNUE'},
            {'code': 'SPDL', 'name': 'Sư phạm Địa lý', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 27.70, 'admission_quota': 45, 'university': 'HNUE'},
            {'code': 'SPTOAN', 'name': 'Sư phạm Toán học', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 26.70, 'admission_quota': 70, 'university': 'HNUE'},
            {'code': 'SPTA', 'name': 'Sư phạm Tiếng Anh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.50, 'admission_quota': 65, 'university': 'HNUE'},

            # ĐH Cần Thơ
            {'code': 'SPTA_CTU', 'name': 'Sư phạm Tiếng Anh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 26.75, 'admission_quota': 55, 'university': 'CTU'},
            {'code': 'YKHOA_CTU', 'name': 'Y khoa', 'block': 'B00', 'subject_1': 'Toán', 'subject_2': 'Hóa', 'subject_3': 'Sinh', 'benchmark_2024': 26.50, 'admission_quota': 120, 'university': 'CTU'},
            {'code': 'CNTT_CTU', 'name': 'Công nghệ thông tin', 'block': 'A00', 'subject_1': 'Toán', 'subject_2': 'Lý', 'subject_3': 'Hóa', 'benchmark_2024': 25.50, 'admission_quota': 100, 'university': 'CTU'},
            {'code': 'QTKD_CTU', 'name': 'Quản trị Kinh doanh', 'block': 'D01', 'subject_1': 'Toán', 'subject_2': 'Văn', 'subject_3': 'Anh', 'benchmark_2024': 25.00, 'admission_quota': 110, 'university': 'CTU'},
            {'code': 'LUAT_CTU', 'name': 'Luật', 'block': 'C00', 'subject_1': 'Văn', 'subject_2': 'Sử', 'subject_3': 'Địa', 'benchmark_2024': 25.25, 'admission_quota': 80, 'university': 'CTU'},
        ]
        
        # Tạo các ngành học
        for major_data in majors_data:
            university = universities[major_data['university']]
            major, created = Major.objects.get_or_create(
                code=major_data['code'],
                university=university,
                defaults={
                    'name': major_data['name'],
                    'block': major_data['block'],
                    'subject_1': major_data['subject_1'],
                    'subject_2': major_data['subject_2'],
                    'subject_3': major_data['subject_3'],
                    'benchmark_2024': major_data['benchmark_2024'],
                    'admission_quota': major_data['admission_quota']
                }
            )
            if created:
                self.stdout.write(f'✅ Đã tạo ngành: {major.name} - {university.name}')
            else:
                self.stdout.write(f'⚠️ Đã tồn tại ngành: {major.name} - {university.name}')
        
        self.stdout.write(self.style.SUCCESS('🎉 Hoàn thành seed dữ liệu!'))