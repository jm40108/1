from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .forms import *
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
#제네릭뷰
#뷰 클래스 구현 시 제네릭뷰를 상속받아 변수/메소드를 수정해 사용

#게시물 목록(index)
class Index(ListView):
    template_name = 'blog/index.html' #HTML 파일의 경로를 저장하는 변수
    model = Post #목록으로 보여진 모델클래스를 지정하는 변수
    context_object_name = 'post_list'
    paginate_by = 5
#상세 페이지(detail)
class Detail(DetailView):
    template_name = 'blog/detail.html'
    model = Post
    context_object_name = 'obj'
#글 등록 페이지(postRegister)
class PostRegister(LoginRequiredMixin,FormView):
    template_name='blog/postregister.html'
    form_class=PostForm
    context_object_name = 'form'
    def form_valid(self, form):
        obj = form.save(commit=False)#obj =Post 객체
        obj.author = self.request.user
        obj.save()
        for f in self.request.FILES.getlist('images'):
            #f : 이미지 정보, f를 이용해 PostImage 객체를 생성, 데이터베이스에 저장
            image = PostImage(post = obj, image = f)
            image.save()
        for f in self.request.FILES.getlist('files'):
            file = PostFile(post = obj, file = f)
            file.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(obj.id,)))
#검색기능을 구현한 뷰클래스
class SearchP(FormView):
    template_name = 'blog/searchP.html'
    form_class = SearchForm
    context_object_name = 'form'
    # 유효성검사를 통과한 요청들을 처리하기 위해서 form_valid함수 오버라이딩
    def form_valid(self, form):
        #post 객채중에 사용자가 입력한 텍스트를 포함한 객체를 찾아  HTML결과로 보여주기
        #사용자가 입력한 텍스트 추출
        search_word = form.cleaned_data['search_word']
        #추출된 텍스트를 포함한 Post객체들을 추출
        post_list = Post.objects.filter(headline__contains=search_word)
        #추출된 결과를 HTML로 전달
        return render(self.request, self.template_name, {'form':form, 'search_word':search_word, 'postlist':post_list})