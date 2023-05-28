from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('id<int:post_id>/', views.detail, name='detail'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('korean/', views.list1, name='list1'),
    path('japanese/', views.list2, name='list2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)