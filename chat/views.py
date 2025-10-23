from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required(login_url='login')
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='test-group')
    chat_messages = chat_group.message.all().order_by('created_at')
    return render(request, 'chat/chat.html', {'chat_messages': chat_messages})