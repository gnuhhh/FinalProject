from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('<int:test_id>/', views.test_detail, name='test_detail'),
    path('<int:test_id>/take/', views.test_take, name='test_take'),  # Thêm dòng này
    path('<int:test_id>/submit/', views.submit_test, name='test_submit'),  # Đổi tên cho khớp
]