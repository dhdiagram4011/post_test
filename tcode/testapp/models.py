from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.


# login page
class Login(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


# 회원가입 후 회원가입 완료 및 결과값 출력 페이지
class Post(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.email




### 서버실 테스트 서버 관리대장(RP)
class Serverlist(models.Model): 
    name = models.CharField(max_length=500) #소유자명
    team = models.CharField(max_length=500) #소속팀
    server_count = models.CharField(max_length=500) #보유댓수
    model_name = models.CharField(max_length=500) #서버 모델명
    code = models.CharField(max_length=500) #분류코드
    use_case = models.TextField(max_length=5000) #사용용도
    created_date = models.DateTimeField(default=timezone.now) #입력일시
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)  #등록일시

    def publish (self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name







    









    


    
    




