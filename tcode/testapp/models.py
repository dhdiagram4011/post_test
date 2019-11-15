from django.db import models
from django.utils import timezone
from django import forms
from google.cloud import translate


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



# 구글 번역 API
class Transpost(models.Model):
    document = models.TextField(max_length=5000, verbose_name="번역할 문장")
    language = models.CharField(max_length=500, verbose_name="번역할 언어")
    language_result = models.TextField(blank=True, null=True, verbose_name="번역결과")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="번역완료시간")
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        #return f"{self.document} 의 번역할 언어는 {self.language} 입니다"
        return f"{self.document} 의 번역할 언어는 {self.language_result} 입니다"

        class Meta:
            ordering = ['-created_date','-published_date']

        ## 번역결과
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        ## 번역하는 방법 (google translate api) -- save의 오버라이드
        translate_client = translate.Client()
        self.language_result = translate_client.translate(self.document,target_language=self.language)
        return super().save(force_insert,force_update,using,update_fields)
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.language_result


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







    









    


    
    




