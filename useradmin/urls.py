from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    # 장고의 django.contrib.auth기능을 이용하여 로그인과 로그아웃을 쉽게 구현가능하다.
    path('login/', auth_views.LoginView.as_view(template_name='useradmin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]