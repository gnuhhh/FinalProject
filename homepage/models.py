from django.db import models
from django.utils import timezone
# Create your models here.
class Expert(models.Model):
    expert_first_name = models.CharField(max_length=50, verbose_name='Họ đệm')
    expert_last_name = models.CharField(max_length=50, verbose_name='Tên')
    expert_image = models.ImageField(upload_to='static/assets/img/experts', verbose_name='Hình ảnh')
    expert_description = models.CharField(max_length=200, verbose_name='Mô tả', null=True)
    expert_work_day = models.DateField(verbose_name='Ngày vào làm', default=timezone.now)
    
    def __str__(self):
        return self.expert_first_name + ' ' + self.expert_last_name