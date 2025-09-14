from django.shortcuts import render, get_object_or_404
from news.models import News
from .models import Expert
# Create your views here.
def index(request):
    news = News.objects.filter(is_active=True).exclude(id__in=[1, 2])
    new = get_object_or_404(News, id=1)
    new1 = get_object_or_404(News, id=2)
    experts = Expert.objects.all()
    return render(request, 'index.html', {"news":news, "new":new, "experts":experts, 'new1':new1})

def news_detail(request, slug):
    new = get_object_or_404(News, slug=slug)
    previous_news = News.objects.filter(created_at__lt=new.created_at).order_by('-created_at').first()
    next_news = News.objects.filter(created_at__gt=new.created_at).order_by('created_at').first()
    return render(request, 'news_detail.html', {"new":new, 'previous_news':previous_news, 'next_news':next_news})