from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tên trường")
    code = models.CharField(max_length=20, unique=True, verbose_name="Mã trường")
    location = models.CharField(max_length=100, verbose_name="Địa điểm")
    type = models.CharField(max_length=50, choices=[
        ('public', 'Công lập'),
        ('private', 'Tư thục')
    ], verbose_name="Loại hình")
    website = models.URLField(blank=True, verbose_name="Website")
    
    class Meta:
        verbose_name = "Trường đại học"
        verbose_name_plural = "Các trường đại học"
    
    def __str__(self):
        return self.name

class Major(models.Model):
    # Các khối thi chính với tổ hợp môn phổ biến
    BLOCK_CHOICES = [
        ('A00', 'Khối A00 (Toán, Lý, Hóa)'),
        ('A01', 'Khối A01 (Toán, Lý, Anh)'),
        ('B00', 'Khối B00 (Toán, Hóa, Sinh)'),
        ('C00', 'Khối C00 (Văn, Sử, Địa)'),
        ('D01', 'Khối D01 (Toán, Văn, Anh)'),
        ('D07', 'Khối D07 (Toán, Hóa, Anh)'),
        ('OTHER', 'Khối khác')
    ]
    
    # Các môn học phổ biến
    SUBJECT_CHOICES = [
        ('Toán', 'Toán'),
        ('Lý', 'Vật lý'),
        ('Hóa', 'Hóa học'),
        ('Sinh', 'Sinh học'),
        ('Văn', 'Ngữ văn'),
        ('Sử', 'Lịch sử'),
        ('Địa', 'Địa lý'),
        ('Anh', 'Tiếng Anh'),
        ('Trung', 'Tiếng Trung'),
        ('Pháp', 'Tiếng Pháp'),
        ('Nga', 'Tiếng Nga'),
        ('Nhật', 'Tiếng Nhật'),
        ('Đức', 'Tiếng Đức'),
        ('Hàn', 'Tiếng Hàn'),
    ]
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='majors', verbose_name="Trường đại học")
    name = models.CharField(max_length=200, verbose_name="Tên ngành")
    code = models.CharField(max_length=20, verbose_name="Mã ngành")
    block = models.CharField(max_length=10, choices=BLOCK_CHOICES, verbose_name="Khối thi")
    subject_1 = models.CharField(max_length=50, choices=SUBJECT_CHOICES, verbose_name="Môn 1")
    subject_2 = models.CharField(max_length=50, choices=SUBJECT_CHOICES, verbose_name="Môn 2")  
    subject_3 = models.CharField(max_length=50, choices=SUBJECT_CHOICES, verbose_name="Môn 3")
    benchmark_2024 = models.FloatField(verbose_name="Điểm chuẩn 2024")
    admission_quota = models.IntegerField(verbose_name="Chỉ tiêu")
    description = models.TextField(blank=True, verbose_name="Mô tả ngành")
    
    class Meta:
        verbose_name = "Ngành học"
        verbose_name_plural = "Các ngành học"
        unique_together = ['code', 'university']
    
    def __str__(self):
        return f"{self.name} - {self.university.name}"
    
    def get_subject_combination(self):
        """Trả về tổ hợp môn thi dạng chuỗi"""
        return f"{self.subject_1} - {self.subject_2} - {self.subject_3}"

class AdmissionData(models.Model):
    """Model để lưu dữ liệu tuyển sinh các năm (có thể mở rộng cho nhiều năm)"""
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='admission_data', verbose_name="Ngành học")
    year = models.IntegerField(verbose_name="Năm tuyển sinh")
    benchmark = models.FloatField(verbose_name="Điểm chuẩn")
    admission_quota = models.IntegerField(verbose_name="Chỉ tiêu")
    actual_admitted = models.IntegerField(blank=True, null=True, verbose_name="Số lượng trúng tuyển thực tế")
    
    class Meta:
        verbose_name = "Dữ liệu tuyển sinh"
        verbose_name_plural = "Dữ liệu tuyển sinh"
        unique_together = ['major', 'year']
    
    def __str__(self):
        return f"{self.major.name} - {self.year}"

class PredictorModel(models.Model):
    """Model để lưu các mô hình dự đoán (nếu cần triển khai AI/ML)"""
    name = models.CharField(max_length=100, verbose_name="Tên mô hình")
    version = models.CharField(max_length=20, verbose_name="Phiên bản")
    accuracy = models.FloatField(blank=True, null=True, verbose_name="Độ chính xác")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    is_active = models.BooleanField(default=True, verbose_name="Đang hoạt động")
    
    class Meta:
        verbose_name = "Mô hình dự đoán"
        verbose_name_plural = "Các mô hình dự đoán"
    
    def __str__(self):
        return f"{self.name} v{self.version}"