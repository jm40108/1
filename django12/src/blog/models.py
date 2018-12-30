from django.db import models
from django.conf import settings


# 카테고리
class PostType(models.Model):
    name = models.CharField('카테고리', max_length=20)

    def __str__(self):
        return self.name


# 글(제목, 글쓴이-왜래키, 글내용, 작성일, 카테고리-왜래키)
class Post(models.Model):
    # models.PROTECT : 연결된 객체가 삭제되는 것을 막아주는 기능
    # models.SET_NULL : 연결된 객체가 삭제되면 null값을 저장
    # models.SET_DEFAULT : 연결된 객체가 삭제되면 기본 설정된 객체와 연결
    # models.SET_() : 연결된 객체가 삭제되면 매개변수로 지정된 객체가 연결
    # models.CASCADE : 연결된 객체가 삭제되면 같이 삭제됨
    type = models.ForeignKey(PostType, on_delete=models.PROTECT)
    headline = models.CharField('제목', max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField('내용' , null=True, blank=True)
    pub_date = models.DateTimeField('작성일',auto_now_add = True)
    class Meta:
        ordering=['-id']
    
# 이미지(글-왜래키, 이미지파일)
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField('이미지파일', upload_to='images/%Y/%m/%d')
    #ImageField : 이미지가 저장된 경로를 저장하는 공간
    #upload_to : 실제 이미지를 저장할 때 사용할 경로
    #%Y : 해당 서버의 현재 년도, %m: 해당 서버의 현재 월 , %d: 해당 서버의 현재 일
    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)

# 파일(글-왜래키, 파일)
class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField('첨부파일', upload_to='files/%Y/%m/%d')
    
    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)