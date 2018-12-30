'''
Created on 2018. 12. 22.

@author: user
'''
# Class 클래스명(ModelForm 또는 Form):
# ModelForm : 모델클래스를 기반으로 입력양식을 자동 생성할 때 상속받는 클래스
# Form : 커스텀 입력양식을 생성할 때 상속받는 클래스
from django.forms.models import ModelForm
from .models import Question, Choice


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['name']

        
class ChoiceForm(ModelForm):
    #Q 변수의 <label>태그의 값을 변경
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)
        self.fields['q'].label = '질문지'
        
    class Meta:
        model = Choice
        fields = ['q','name']
