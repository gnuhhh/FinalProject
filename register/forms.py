from django import forms    
from django.core.exceptions import ValidationError
import re

class RegisterForm(forms.Form):
    firstname = forms.CharField(
        required=True,
        max_length=50,
        error_messages={"required": "Họ đệm không được để trống"}
    )
    
    lastname = forms.CharField(
        required=True,
        max_length=50,
        error_messages={"required": "Tên không được để trống"}
    )

    username = forms.CharField(
        required=True,
        max_length=30,
        error_messages={"required": "Username không được để trống"}
    )

    email = forms.EmailField(
        required=True,
        error_messages={
            "invalid": "Email không đúng định dạng",
            "required": "Email không được để trống"
        }
    )

    password = forms.CharField(
        required=True,
        max_length=8,
        widget=forms.PasswordInput,
        error_messages={"required": "Mật khẩu không được để trống"}
    )
    
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        error_messages={"required": "Vui lòng nhập lại mật khẩu"}
    )
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if " " in username:
            raise ValidationError("Username không được chứa khoảng trắng")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if len(password) < 8:
            raise ValidationError("Mật khẩu phải ít nhất 8 ký tự")

        if not re.search(r"\d", password):
            raise ValidationError("Mật khẩu phải có ít nhất 1 chữ số")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt")
        return password

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise ValidationError("Mật khẩu xác nhận không khớp")
        return cleaned_data