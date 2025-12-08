from django.urls import path
from . import views
from . import search_views  # THÊM DÒNG NÀY - IMPORT QUAN TRỌNG

urlpatterns = [
    # Basic voice endpoints
    path('command/', views.voice_command, name='voice_command'),
    path('listen/', views.listen_microphone, name='listen_microphone'),
    path('speak/', views.speak_text, name='speak_text'),
    
    # Advanced voice search endpoints (CHUYỂN HƯỚNG ĐẾN TRANG TRƯỜNG HỌC)
    path('api/voice-search/start/', views.voice_search_start, name='voice_search_start'),
    path('api/voice-search/stop/', views.voice_search_stop, name='voice_search_stop'),
    path('api/voice-search/get-result/', views.voice_search_get_result, name='voice_search_get_result'),
    path('api/voice-search/check-availability/', views.check_voice_availability, name='check_voice_availability'),
    path('api/voice-search/test/', views.voice_search_test, name='voice_search_test'),  # Test endpoint
    
    # === THÊM ENDPOINT MỚI VÀO ĐÂY ===
    path('api/voice-search/', search_views.handle_voice_search, name='voice_search_handler'),
    
    # Demo pages
    path('demo/', views.voice_search_demo, name='voice_search_demo'),
    
    # Other endpoints
    path('search/', views.search, name='voice_search'),
    path('profile/', views.profile, name='voice_profile'),
    path('', views.voice_home, name='voice_home'),
]