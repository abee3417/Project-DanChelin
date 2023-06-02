from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    # UserCreationForm을 상속받고, 이메일 속성을 추가
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@dankook.ac.kr'):
            raise forms.ValidationError("오직 단국대학교 학생들만 가입할 수 있습니다.")
        return email
    