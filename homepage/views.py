from django.shortcuts import render, get_object_or_404
from news.models import News
from .models import Expert, ChatHistory
from school.models import SchoolMajor
import openai, os
from django.http import JsonResponse   
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
# Create your views here.

def get_admission_context():
    records = (
        SchoolMajor.objects
        .select_related("school", "major")
        .all()
    )
    context = ""
    for r in records:
        context += f"""
                    - Trường: {r.school.schoolName}
                    + Loại: {r.school.type}
                    + Khu vực: {r.school.location}
                    + Năm thành lập: {r.school.establishyear}
                    - Ngành: {r.major.major_name}
                    - Điểm chuẩn: {r.point}
                    - Tổ hợp xét tuyển: {r.admission_combination}
                    - Chỉ tiêu: {r.admission_targets}
                    - Năm tuyển sinh: {r.admission_year}
                    - Chương trình: {"Chất lượng cao" if r.is_high_quality else "Đại trà"}
                    """
    return context

def asking_ai(message):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    admission_context = get_admission_context()
    system_prompt = f"""
                    Bạn là chuyên gia tư vấn tuyển sinh đại học với 10 năm kinh nghiệm.

                    Hệ thống dữ liệu có các bảng:
                    - School (thông tin trường)
                    - Major (ngành học)
                    - SchoolMajor (điểm chuẩn, tổ hợp, chỉ tiêu, năm tuyển sinh)

                    Dữ liệu tuyển sinh hiện tại:
                    {admission_context}
                    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print(f"Lỗi OpenAI API: {e}")
        raise e

def index(request):
    news = News.objects.filter(is_active=True).exclude(id__in=[1, 2])
    new = get_object_or_404(News, id=1)
    new1 = get_object_or_404(News, id=2)
    experts = Expert.objects.all()
    
    # Lấy lịch sử chat của user nếu đã đăng nhập
    chat_history = []
    if request.user.is_authenticated:
        chat_history = ChatHistory.objects.filter(user=request.user).order_by('-created_at')[:10]
    
    get_token(request)
    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        if not message:
            return JsonResponse({'error': 'Thiếu nội dung tin nhắn.'})
        try:
            response = asking_ai(message)
            if not response:
                response = 'Xin lỗi, hiện tôi chưa có câu trả lời phù hợp. Bạn có thể diễn đạt lại câu hỏi?'
            chat_history = ChatHistory.objects.create(
                user=request.user,
                message=message,
                response=response
            )
            chat_history.save()
            return JsonResponse({'response': response, 'message': message})
        except Exception as exc:
            print(f"Lỗi OpenAI API: {exc}")
            fallback = 'Hệ thống đang bận hoặc gặp sự cố. Vui lòng thử lại sau ít phút.'
            return JsonResponse({'response': fallback, 'message': message})
    return render(request, 'index.html', {'news': news, 'new': new, 'experts': experts, 'new1': new1,'chat_history': chat_history})

@login_required
def get_chat_history(request):
    if request.method == 'GET':
        chat_history = ChatHistory.objects.filter(user=request.user).order_by('created_at')[:10]
        history_data = []
        for chat in chat_history:
            history_data.append({
                'message': chat.message,
                'response': chat.response,
                'created_at': chat.created_at.strftime('%d/%m/%Y %H:%M')
            })
        return JsonResponse({'chat_history': history_data})
    return JsonResponse({'error': 'Method not allowed'})

def news_detail(request, slug):
    new = get_object_or_404(News, slug=slug)
    previous_news = News.objects.filter(created_at__lt=new.created_at).order_by('-created_at').first()
    next_news = News.objects.filter(created_at__gt=new.created_at).order_by('created_at').first()
    return render(request, 'news_detail.html', {"new":new, 'previous_news':previous_news, 'next_news':next_news})


