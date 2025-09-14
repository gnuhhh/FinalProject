from django.shortcuts import render, redirect
from .models import Question
import joblib
import os
from django.conf import settings
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'question.html', {'quests':questions})


def prediction(answer):
    try:
        if len(answer) != 20:
            raise ValueError("Số lượng câu trả lời không đúng")

        model_path = os.path.join(settings.BASE_DIR, 'major_prediction.joblib')
        csv_path = os.path.join(settings.BASE_DIR, 'major_dataset.csv')

        rfc = None
        model_loaded = False

        if os.path.exists(model_path):
            try:
                rfc = joblib.load(model_path)
                if hasattr(rfc, 'n_features_in_'):
                    model_loaded = True
            except Exception as e:
                print(f"Lỗi khi load model: {str(e)}")
                model_loaded = False

        if not model_loaded:
            if not os.path.exists(csv_path):
                raise FileNotFoundError(f"Không tìm thấy file dataset: {csv_path}")

            df = pd.read_csv(csv_path)

            if 'Ngành học' not in df.columns:
                raise ValueError("Không tìm thấy cột 'Ngành học' trong dataset")

            X = df.drop(columns=['Ngành học'])
            y = df['Ngành học']

            if X.empty or y.empty:
                raise ValueError("Dữ liệu training rỗng")

            rfc = RandomForestClassifier(n_estimators=100, random_state=42)
            rfc.fit(X, y)
            joblib.dump(rfc, model_path)

        answer = [int(x) for x in answer]

        if hasattr(rfc, 'n_features_in_') and len(answer) != rfc.n_features_in_:
            raise ValueError(f"Số lượng features không khớp. Cần {rfc.n_features_in_}, nhận được {len(answer)}")

        pred_value = rfc.predict([answer])

        major_descriptions = {
            "Công nghệ thông tin": "Ngành học về phát triển phần mềm, xử lý dữ liệu và các hệ thống thông tin",
            "Kế toán": "Ngành học về quản lý tài chính, sổ sách và báo cáo tài chính",
            "Marketing": "Ngành học về chiến lược tiếp thị và quảng bá sản phẩm",
            "Quản trị kinh doanh": "Ngành học về quản lý doanh nghiệp và phát triển chiến lược kinh doanh",
            "Luật": "Ngành học về pháp luật và các quy định pháp lý",
        }

        return {
            'major': pred_value[0],
            'description': major_descriptions.get(pred_value[0], "Chưa có mô tả cho ngành học này")
        }

    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return {
            'major': "Có lỗi xảy ra",
            'description': str(e)
        }
def result(request):
    if request.method == 'POST':
        res = []
        try:
            for i in range(1, 21):
                answer = request.POST.get(f'question_{i}')
                if answer is None:
                    raise ValueError(f"Thiếu câu trả lời cho câu hỏi {i}")
                res.append(answer)
                
            prediction_result = prediction(res)
            return render(request, 'question_result.html', prediction_result)
            
        except Exception as e:
            print(f"Error in result view: {str(e)}")  # Thêm log để debug
            return render(request, 'question_result.html', {
                'major': "Có lỗi xảy ra",
                'description': str(e)
            })
    
    return redirect('question')