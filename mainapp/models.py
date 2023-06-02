from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    category = models.IntegerField() # 1~11까지로 한식부터 카페까지 구분하기 위한 필드
    subject = models.CharField(max_length=200) # 가게이름
    location = models.CharField(max_length=200) # 주소
    callnum = models.CharField(max_length=200) # 전화번호
    timeinfo = models.CharField(max_length=200) # 영업시간
    urlinfo = models.CharField(max_length=200) # URL
    menu = models.TextField() # 메뉴
    review = models.TextField() # 총평
    image = models.ImageField(blank=True, upload_to='media/') # 썸네일사진
    summary = models.CharField(max_length=200) # 썸네일텍스트
    voter = models.ManyToManyField(User, blank=True)  # 추천인

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