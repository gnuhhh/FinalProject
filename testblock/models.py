# testblock/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class TestBlock(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    num_questions = models.IntegerField(default=30, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    SUBJECT_CHOICES = [
        ('A_TOAN', 'Toán Khối A'),
        ('A_LY', 'Vật Lý Khối A'),
        ('A_HOA', 'Hóa Học Khối A'),
        ('B_TOAN', 'Toán Khối B'),
        ('B_HOA', 'Hóa Học Khối B'),
        ('B_SINH', 'Sinh Học Khối B'),
        ('C_VAN', 'Ngữ Văn Khối C'),
        ('C_SU', 'Lịch Sử Khối C'),
        ('C_DIA', 'Địa Lý Khối C'),
        ('D_TOAN', 'Toán Khối D'),
        ('D_VAN', 'Ngữ Văn Khối D'),
        ('D_TA', 'Tiếng Anh Khối D'),
        ('A01_TOAN', 'Toán Khối A01'),
        ('A01_LY', 'Vật Lý Khối A01'),
        ('A01_TA', 'Tiếng Anh Khối A01'),
        ('B01_TOAN', 'Toán Khối B01'),
        ('B01_HOA', 'Hóa Học Khối B01'),
        ('B01_TA', 'Tiếng Anh Khối B01'),
        ('D07_TOAN', 'Toán Khối D07'),
        ('D07_HOA', 'Hóa Học Khối D07'),
        ('D07_TA', 'Tiếng Anh Khối D07'),
        ('B02_TOAN', 'Toán Khối B02'),
        ('B02_SINH', 'Sinh Học Khối B02'),
        ('B02_DIA', 'Địa Lý Khối B02'),
        ('C01_VAN', 'Ngữ Văn Khối C01'),
        ('C01_TOAN', 'Toán Khối C01'),
        ('C01_LY', 'Vật Lý Khối C01'),
        ('D14_VAN', 'Ngữ Văn Khối D14'),
        ('D14_LS', 'Lịch Sử Khối D14'),
        ('D14_TA', 'Tiếng Anh Khối D14'),
        ('D15_VAN', 'Ngữ Văn Khối D15'),
        ('D15_DIA', 'Địa Lý Khối D15'),
        ('D15_TA', 'Tiếng Anh Khối D15')
    ]
    
    code = models.CharField(max_length=10, choices=SUBJECT_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    time_limit = models.IntegerField(default=90)
    total_questions = models.IntegerField(default=50)
    
    def __str__(self):
        return self.name

# 🟢 ĐỔI TÊN BlQuestion THÀNH BlockQuestion
class BlockQuestion(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    test_block = models.ForeignKey(TestBlock, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    
    def __str__(self):
        return f"{self.test_block.name} - {self.text[:50]}..."

class BlockTestResult(models.Model):
    test_block = models.ForeignKey(TestBlock, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, blank=True)
    score = models.IntegerField(validators=[MinValueValidator(0)])
    total_questions = models.IntegerField(validators=[MinValueValidator(1)])
    percentage = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    suggested_majors = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.test_block.name} - {self.score}/{self.total_questions}"

class SubjectTestResult(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, blank=True)
    score = models.IntegerField(validators=[MinValueValidator(0)])
    total_questions = models.IntegerField(validators=[MinValueValidator(1)])
    percentage = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    time_taken = models.IntegerField(default=0)
    question_details = models.TextField(blank=True)  # ✅ THÊM FIELD NÀY
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.subject.name} - {self.score}/{self.total_questions}"
# Thêm vào models.py
class University(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[
        ('public', 'Công lập'),
        ('private', 'Tư thục')
    ])
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class Major(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='majors')
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    block = models.CharField(max_length=10, choices=[
        ('A', 'Khối A'), ('A1', 'Khối A1'), 
        ('B', 'Khối B'), ('C', 'Khối C'),
        ('D', 'Khối D'), ('OTHER', 'Khối khác')
    ])
    subject_1 = models.CharField(max_length=50)  # Môn 1
    subject_2 = models.CharField(max_length=50)  # Môn 2  
    subject_3 = models.CharField(max_length=50)  # Môn 3
    benchmark_2024 = models.FloatField()  # Điểm chuẩn 2024
    admission_quota = models.IntegerField()  # Chỉ tiêu
    
    def __str__(self):
        return f"{self.name} - {self.university.name}"