from django import forms

class TestBlockForm(forms.Form):
    user_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nhập tên của bạn (tùy chọn)'
        })
    )

class BlockQuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[
                    ('A', f"A. {question.option_a}"),
                    ('B', f"B. {question.option_b}"),
                    ('C', f"C. {question.option_c}"),
                    ('D', f"D. {question.option_d}"),
                ],
                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                label=question.text,
                required=True
            )