# testblock/urls.py
from django.urls import path
from . import views

app_name = 'testblock'

urlpatterns = [
    # URL GỐC: http://127.0.0.1:8000/test-khoi/
    path('', views.test_block_list, name='test_block_list'),
    
    # URL cho danh sách môn học theo khối
    path('<str:block_code>/mon-hoc/', views.subject_test_list, name='subject_test_list'),
    
    # URL cho bài test môn học
    path('<str:block_code>/test/<str:subject_code>/', views.start_subject_test, name='start_subject_test'),
    path('<str:block_code>/test/<str:subject_code>/submit/', views.submit_subject_test, name='submit_subject_test'),
    
    # URL CHO KẾT QUẢ - THÊM DÒNG NÀY
    path('ket-qua/<int:result_id>/', views.subject_test_result, name='subject_test_result'),
    
    # Các URLs khác
    path('block/<int:block_id>/', views.test_block_detail, name='test_block_detail'),
    path('ket-qua/<int:result_id>/', views.test_block_result, name='test_block_result'),
    path('ket-qua/<int:result_id>/chi-tiet/', views.test_block_result_detail, name='test_block_result_detail'),
    # XÓA DÒNG NÀY: path('ket-qua-mon-hoc/<int:result_id>/', views.subject_test_result, name='subject_test_result_old'),
    
]