from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    category = models.IntegerField() # 1~11까지로 한식부터 카페까지 구분하기 위한 필드
    subject = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    callnum = models.CharField(max_length=200)
    timeinfo = models.CharField(max_length=200)
    urlinfo = models.CharField(max_length=200)
    menu = models.TextField()
    review = models.TextField()
    image = models.ImageField(blank=True, upload_to='media/')
    # 별점 필드 추가하여 넣을 것.
    voter = models.ManyToManyField(User)  # 추천인 추가

    def __str__(self):
        return self.subject

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 기존 모델을 속성으로 연결하려면 ForeignKey를 사용한다.
    # on_delete=models.CASCADE : 연결된 모델의 객체가 삭제될 경우 함께 삭제된다는 의미
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일시