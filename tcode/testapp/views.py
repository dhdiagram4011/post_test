from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django import forms
from .models import Post
from .models import Serverlist
from .models import Login
from .forms import RegForm
from .forms import ServerlistForm
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password , check_password
import urllib.request

#from .forms import SelecttestForm
#from .forms import RadiotestForm
#from .models import Radiotest
#from .models import Selecttest


#메인페이지  (/)
def main(request):
    email = request.session.get('email')
    return render(request, 'testapp/main.html', {})


#로그인 페이지 (/login)
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session["user"] = form.email
            return redirect("login_success")
    else:
        form = LoginForm()
    
    return render(request, 'testapp/login.html', {"form":form})


#로그인 성공창 출력
def login_success(request):
    logins = Login.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:1]
    return render(request, 'testapp/login_success.html', {'logins':logins})


#빈 페이지
def white(request):
    pass

#로그아웃 페이지
def logout(request):
    if request.session.get('email'):
        del(request.session['email'])
    return redirect('main')


# 회원가입
def join(request):
    if request.method == 'GET':
        form = RegForm(request.GET)
        return render(request, 'testapp/join.html' , {'form':form})
    elif request.method  == 'POST':
        form = RegForm(request.POST)
        post = form.save()
        email = request.POST.get('email', None)
        name = request.POST.get('name' , None)
        password = request.POST.get('password' , None)
        post.published_date = timezone.now()
    #return render(request, 'testapp/join_result.html')
    return redirect('join_result')


#회원가입 결과값 출력
def join_result(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:1]
    return render(request, 'testapp/join_result.html', {'posts':posts})




## 번역기
def translate(request):
    if request.method == 'POST':
        form = TransForm(request.POST)
        post = form.save()
        document = request.POST.get('document', None)
        language = request.POST.get('language' , None)
        language_result = request.POST.get('language_result', None)
        return redirect ('translate_result')
    elif request.method == 'GET':
        form = TransForm
        return render(request, 'testapp/translate.html', {'form':form})
  
          
#번역 결과값 출력
def translate_result(request):
    #object = Transpost.objects.get(pk=pk)
    #return render(request, "testapp/translate_result.html", {"object":object})
    transposts = Transpost.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'testapp/translate_result.html', {'transposts':transposts})


# @rpits 서버 리스트 취합 테스트 (Connect to MYSQL)
def serverlist(request):
    if request.method == 'GET':
        form = ServerlistForm(request.GET)
        return render(request, 'testapp/serverlist.html', {'form':form})
    elif request.method == 'POST':
        form = ServerlistForm(request.POST)
        posts = form.save()
        name = request.POST.get('name', None)
        server_count = request.POST.get('server_count',None)
        model_name = request.POST.get('model_name', None)
        code = request.POST.get('code', None)
        use_case = request.POST.get('use_case',None)
        created_date =  request.POST.get('created_date', None)
        published_date = request.POST.get('published_date' , None)
    return redirect ('serverlist_result')


# 서버 리스트 입력에 대한 결과값
def serverlist_result(request):
    serverlists = Serverlist.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    return render(request, 'testapp/serverlist_result.html', {'serverlists':serverlists})


# 라디오 버튼 테스트 (입력)
def radiotest(request):
    if request.method == 'GET':
        form = RadiotestForm(request.GET)
        return render(request, 'testapp/selecttest.html', {'form':form})
    elif request.method =='POST':
        form = RadiotestForm(request.POST)
        posts = form.save()
        choice_field = request.POST.get('choice_field', None)
    return redirect('selecttest_result')


# 라디오 버튼 결과값 테스트 (MYSQL 저장)
def radiotest_result(request):
    radiotests = Radiotest.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:1]
    return render(request, 'testapp/selecttest_result.html', {'radiotests':radiotests})
    






