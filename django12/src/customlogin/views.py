from django.shortcuts import render
from customlogin.forms import SigninForm, SignupForm
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


#회원가입
def signup(request):
    if request.method == "GET":
        return render(request, 'customlogin/signup.html', {'f':SignupForm()})
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            #User.objects.create_user(아이디, 이메일, 비밀번호)->비밀번호를 암호화한채로 회원생성, 데이터베이스에 저장 및 반환
            #form.cleaned_data['변수명'] -> 사용자가 입력한 데이터 추출
            if form.cleaned_data['password']==form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()
                return HttpResponseRedirect(reverse('vote:index'))
            else:
                return render(request, 'customlogin/signup.html',{'f':form,'error':"비밀번호와 비밀번호 확인이 다릅니다."})
        else:
            return render(request, 'customlogin/signup.html',{'f':form})
#로그인
def signin(request):
    if request.method == "GET":
        return render(request, 'customlogin/signin.html', {'f': SigninForm(), 'nexturl':request.GET.get('next','')})
    elif request.method == "POST":
        form = SigninForm(data=request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)
        if u:
            login(request, user=u)
            nexturl = request.POST.get('nexturl')
            if nexturl:
                return HttpResponseRedirect(nexturl)
            else:
                return HttpResponseRedirect(reverse('vote:index'))
        else:
            return render(request, 'customlogin/signin.html', {'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
    
#로그아웃
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('vote:index'))