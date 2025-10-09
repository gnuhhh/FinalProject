from django.db import models

class Major(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    title = models.CharField(max_length=200)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    num_questions = models.IntegerField(default=30)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(
        max_length=1, 
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
        default='A'
    )

    def __str__(self):
        return self.text[:50]  # Hiển thị ngắn gọn

# Xóa hoặc comment class Choice vì không sử dụng
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
#     text = models.CharField(max_length=200)
#     is_correct = models.BooleanField(default=False)
#     
#     def __str__(self):
#         return f"{self.text} ({'Đúng' if self.is_correct else 'Sai'})"