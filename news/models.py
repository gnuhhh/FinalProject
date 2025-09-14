from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Danh mục")
    image = models.ImageField(upload_to='static/assets/img/news/', verbose_name="Hình ảnh", null=True)
    content = models.TextField(verbose_name="Nội dung")
    author = models.CharField(max_length=100, default="Admin", verbose_name="Tác giả")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    # view_count = models.PositiveIntegerField(default=0, verbose_name="Lượt xem")
    is_active = models.BooleanField(default=False, verbose_name="Hiển thị")

    class Meta:
        verbose_name = "Tin tức"
        verbose_name_plural = "Tin tức"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/news/{self.slug}/'

    # def increment_view_count(self):
    #     self.view_count += 1
    #     self.save(update_fields=['view_count'])
