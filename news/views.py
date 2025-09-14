# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import News
# from .forms import NewsForm

# @login_required
# def news(request):
#     news_list = News.objects.all()
#     return render(request, 'admin/news/view.html', {'news_list':news_list})

# @login_required
# def news_create(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = form.save(commit=False)
#             news.author = request.user
#             news.save()
#             return redirect('news_list')
#     else:
#         form = NewsForm()
#     return render(request, 'news/create.html', {'form': form})

# @login_required
# def news_edit(request, pk):
#     news = get_object_or_404(News, pk=pk)
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES, instance=news)
#         if form.is_valid():
#             form.save()
#             return redirect('news_list')
#     else:
#         form = NewsForm(instance=news)
#     return render(request, 'news/edit.html', {'form': form, 'news': news})

# @login_required
# def news_delete(request, pk):
#     news = get_object_or_404(News, pk=pk)
#     if request.method == 'POST':
#         news.delete()
#         return redirect('news_list')
#     return render(request, 'news/delete.html', {'news': news})
