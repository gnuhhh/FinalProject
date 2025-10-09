from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Test, Question
import random

def test_list(request):
    query = request.GET.get('q', '')
    tests = Test.objects.filter(title__icontains=query) if query else Test.objects.all()
    return render(request, "testapp/test_list.html", {"tests": tests, "query": query})

def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions_count = test.questions.count()
    
    return render(request, "testapp/test_detail.html", {
        "test": test, 
        "questions_count": questions_count
    })

def test_take(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = list(test.questions.all())
    
    # Kiểm tra nếu test không có câu hỏi
    if len(questions) == 0:
        messages.warning(request, "Bài test này chưa có câu hỏi.")
        return redirect('testapp:test_detail', test_id=test_id)
    
    # Giới hạn số câu hỏi theo num_questions của test
    if len(questions) > test.num_questions:
        questions = random.sample(questions, test.num_questions)
    else:
        random.shuffle(questions)
    
    # PHÂN TRANG - 5 câu mỗi trang
    paginator = Paginator(questions, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, "testapp/test_take.html", {
        "test": test, 
        "questions": page_obj,
        "page_obj": page_obj
    })

def submit_test(request, test_id):
    if request.method != 'POST':
        messages.error(request, "Không tìm thấy dữ liệu bài làm.")
        return redirect('testapp:test_detail', test_id=test_id)
    
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    score = 0
    total = min(len(questions), test.num_questions)
    
    # Tạo danh sách chi tiết kết quả
    result_details = []
    
    for question in questions:
        answer_key = f"question_{question.id}"
        user_answer = request.POST.get(answer_key)
        is_correct = False
        
        if user_answer and user_answer.upper() == question.correct_answer:
            score += 1
            is_correct = True
        
        # Thêm chi tiết cho mỗi câu hỏi
        result_details.append({
            'question': question.text,
            'chosen': user_answer if user_answer else "Không trả lời",
            'correct': question.correct_answer,
            'is_correct': is_correct
        })
    
    percentage = (score / total) * 100 if total > 0 else 0
    
    # Xác định thông báo kết quả
    if percentage >= 70:
        result_message = "🎉 Chúc mừng! Bạn có thể thử sức ở chuyên ngành này!"
    else:
        result_message = "📘 Bạn nên tìm hiểu thêm về chuyên ngành này."

    return render(request, "testapp/test_result.html", {
        "test": test,
        "score": int(percentage),
        "correct": score,
        "total": total,
        "percentage": percentage,
        "message": result_message,
        "details": result_details
    })