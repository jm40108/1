from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from vote.forms import QuestionForm, ChoiceForm
from _datetime import datetime
from django.contrib.auth.decorators import login_required



# index
def index(request):
    a = Question.objects.all()
    return render(request, "vote/index.html", {'a':a})


# detail
def detail(request, qid):
    # get_object_or_404(모델클래스, 조건):해당하는 모델클래스에서 조건에 맞는 객체 한개를 추출
    # 조건에 맞는 객체가 한개도 없는 경우, 사용자가 잘못 요청한 것으로 처리해 404에러를 띄우는 처리를 해줌
    b = get_object_or_404(Question, id=qid)
    return render(request, 'vote/detail.html', {'q':b})


# vote
def vote(request):
    if request.method == "POST":
        c_id = request.POST.get('a')
        c = get_object_or_404(Choice, id=c_id)
        c.votes += 1
        c.save()
        return HttpResponseRedirect(reverse('vote:result', args=(c.q.id,)))


# result
def result(request, q_id):
    return render(request, 'vote/result.html', {'q':get_object_or_404(Question, id=q_id)})

@login_required
def qregister(request):
    if request.method == "GET":
        form = QuestionForm()
        return render(request, 'vote/qregister.html', {'f':form})
    elif request.method == "POST":
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            print('생성된 question 객체',q)
            q.date = datetime.now()
            q.save()
            return HttpResponseRedirect(reverse('vote:index'))

@login_required
def cregister(request):
    if request.method == "GET":
        return render(request, 'vote/cregister.html', {'f': ChoiceForm()})
    elif request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            c = form.save()
            print(c)
            return HttpResponseRedirect(reverse('vote:detail', args=(c.q.id,)))
        else:
            return render(request, 'vote/cregister.html',{'f':form,'error':'유효하지 않는 값입니다.'})

@login_required
def qupdate(request, q_id):
    obj = get_object_or_404(Question, id=q_id)
    if request.method == "GET":
        form = QuestionForm(instance = obj)
        return render(request, "vote/qupdate.html",{'f':form})
    elif request.method == "POST":
        form = QuestionForm(data = request.POST, instance = obj)
        if form.is_valid():
            q = form.save()
            print("obj : ",obj)
            print('q : ',q)
            return HttpResponseRedirect(reverse('vote:index'))

@login_required
def cupdate(request, c_id):
    c = get_object_or_404(Choice, id=c_id)
    if request.method == "GET":
        form = ChoiceForm(instance = c)
        return render(request, 'vote/cupdate.html', {'f':form})
    elif request.method == "POST":
        form = ChoiceForm(data = request.POST, instance = c)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vote:detail',args=(c.q.id,)))
        else:
            pass

@login_required
def qdelete(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    q.delete()
    return HttpResponseRedirect(reverse('vote:index'))

@login_required
def cdelete(request, c_id):
    c = get_object_or_404(Choice, id=c_id)
    c.delete();
    return HttpResponseRedirect(reverse('vote:detail',args=(c.q.id,)))

