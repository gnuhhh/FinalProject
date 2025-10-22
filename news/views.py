from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import News

def news_list(request):
    """Hiển thị danh sách tin tức với phân trang và tìm kiếm"""
    # Lấy tất cả tin tức đang hoạt động
    news_queryset = News.objects.filter(is_active=True).order_by('-created_at')
    
    # Xử lý tìm kiếm
    search_query = request.GET.get('search', '')
    if search_query:
        news_queryset = news_queryset.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # Phân trang
    paginator = Paginator(news_queryset, 6)  # 6 bài viết mỗi trang
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)
    
    # Lấy tin tức gần đây cho sidebar
    recent_news_list = News.objects.filter(is_active=True).order_by('-created_at')[:5]
    
    context = {
        'news_list': news_list,
        'recent_news_list': recent_news_list,
        'search_query': search_query,
    }
    
    return render(request, 'news.html', context)

def news_detail(request, slug):
    """Hiển thị chi tiết bài viết"""
    news = get_object_or_404(News, slug=slug, is_active=True)
    
    # Lấy tin tức liên quan
    related_news = News.objects.filter(is_active=True).exclude(id=news.id).order_by('-created_at')[:3]
    
    context = {
        'news': news,
        'related_news': related_news,
    }
    
    return render(request, 'news/detail.html', context)
