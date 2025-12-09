from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from advise.models import Appointment
from .models import *
# Create your views here.
@login_required(login_url='login')
def chat_view(request, id):
    chat_group = get_object_or_404(ChatGroup, appointment__id=id)
    chat_messages = chat_group.message.all().order_by('created_at')
    chat_messages_sender = GroupMessage.objects.exclude(sender=request.user).first()
    appointment = Appointment.objects.get(id=id)
    # chat_messages_sender = appointment.work_schedule.expert
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            group_message = GroupMessage.objects.create(group=chat_group, sender=request.user, message=message_content)
            group_message.save()
        # if request.htmx:
        #     return render(request, 'chat/partials/chat_message_p.html', {'message': group_message, 'user': request.user})
    else:    
        return render(request, 'chat/chat.html', {'chat_messages': chat_messages, 'chat_messages_sender': chat_messages_sender, 'appointment': appointment, 'chat_group': chat_group})