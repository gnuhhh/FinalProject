from django.db import models

# Create your models here.
class School(models.Model):
    schoolId = models.CharField(max_length=10)
    schoolName = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to='static/assets/img/schools/', verbose_name='Hình ảnh')
    type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    content = models.TextField(max_length=1000000, default="tuyen sinh", null=True)
    description = models.CharField(max_length=1000000, default='Là một trong những cơ sở giáo dục hàng đầu tại Việt Nam, chuyên cung cấp chương trình đào tạo chất lượng cao, gắn liền với thực tiễn và hội nhập quốc tế. Với sứ mệnh đào tạo nguồn nhân lực có trình độ chuyên môn vững vàng, tư duy sáng tạo và đạo đức nghề nghiệp, trường luôn không ngừng đổi mới trong công tác giảng dạy, nghiên cứu khoa học và chuyển giao công nghệ. Trường hiện có nhiều khoa chuyên ngành đa dạng như Công nghệ thông tin, Kinh tế, Ngoại ngữ, Kỹ thuật, và Quản trị kinh doanh, đáp ứng nhu cầu phát triển của xã hội hiện đại. Cơ sở vật chất khang trang, đội ngũ giảng viên giàu kinh nghiệm cùng môi trường học tập thân thiện, năng động là những yếu tố giúp sinh viên phát triển toàn diện về kiến thức, kỹ năng và nhân cách.', null=True)
    establishyear = models.IntegerField(default=2000, null=True)
    scale = models.CharField(max_length=10, default='36000+', null=True)
    numberOfMajor = models.IntegerField(default=50, null=True)
    phoneNumber = models.CharField(max_length=20, default='028.3722.5724', null=True)
    email = models.CharField(max_length=50, default='tuyensinh@edu.vn', null=True)
    
    def __str__(self):
        return self.schoolName
    
class Major(models.Model):
    major_name = models.CharField(max_length=100, verbose_name='Tên ngành')
    schools = models.ManyToManyField(School, through='SchoolMajor')

    def __str__(self):
        return self.major_name

class SchoolMajor(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    point = models.FloatField(null=True, verbose_name='Điểm chuẩn')
    admission_targets = models.IntegerField(null=True, verbose_name='Chỉ tiêu')