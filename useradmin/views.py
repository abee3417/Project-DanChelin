from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from useradmin.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # 만들어진 회원으로부터 아이디, 비번 가져와서 자동로그인 하게해준다.
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('main:index')
    else:
        form = UserForm()
    return render(request, 'useradmin/signup.html', {'form': form})