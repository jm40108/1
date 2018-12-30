from django.db import models


# Create your models here.
# 질문
# 질문제목 생성일
class Question(models.Model):
    name = models.CharField('설문조사 제목', max_length=100)
    date = models.DateTimeField()
    def __str__(self):
        return self.name

    
# 답변
# 어떤질문에연결되있는지 답변내용 투표수
class Choice(models.Model):
    name = models.CharField('답변항목', max_length=50)
    votes = models.IntegerField('투표수', default=0)
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='답변항목'
        ordering = ['q']
