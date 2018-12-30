"""django12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import path, include
from bookmark.views import index, booklist, bookdetail
from django.conf import settings
from django.conf.urls.static import static


#include : 하위 URLconf 파일을 추가할때 사용하는 함수
#urlpatterns : URL과 뷰함수를 등록 및 관리하는 변수
#URL 등록 시 path함수를 이용해 urlpatterns의 요소를 추가
#path( URL주소(문자열) , 호출할 뷰함수/클래스 이름) 

#웹서버 기본주소 : 127.0.0.1:8000/ 
urlpatterns = [
    #기본주소 + admin 주소로 클라이언트가 요청한 경우, admin폴더/site.py/urls 함수가 실행
    path('a1/', admin.site.urls),
    path('', index), #127.0.0.1:8000 으로 클라이언트가 요청했을 때, index함수가 호출
    path('list/', booklist),
    path('detail/<int:bookid>/',bookdetail),
    path('vote/',include('vote.urls')),
    path('cl/', include('customlogin.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('blog/', include('blog.urls')),
]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




