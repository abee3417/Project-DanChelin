from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('korean/', views.list1, name='list1'),
    path('japanese/', views.list2, name='list2'),
]