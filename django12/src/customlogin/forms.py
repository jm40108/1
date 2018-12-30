'''
Created on 2018. 12. 23.

@author: user
'''
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

#회원가입에 사용할 모델 폼 클래스
class SignupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password_check'].label = '패스워드 확인'
    #폼 클래스에서 추가적인 <input>을 만들경우 forms.XXXField 객체를 변수에 저장
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order = ['username','password','password_check','last_name','first_name','email']
    class Meta:
        model = User
        widgets={
            'password':forms.PasswordInput()
            }
        fields=['username','password','last_name','first_name','email']
#로그인에 사용할 모델 폼 클래스
class SigninForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'password':forms.PasswordInput()
            }
        fields=['username','password']