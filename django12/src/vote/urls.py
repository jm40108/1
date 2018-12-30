'''
Created on 2018. 12. 16.

@author: user
'''
from django.urls import path
from .views import *
app_name='vote'
urlpatterns =[
    path('',index, name='index'),
    path('<int:qid>/',detail, name='detail'),
    path('vote/',vote, name='vote'),
    path('result/<int:q_id>/',result, name='result'),
    path('qr/',qregister, name = 'qregister'),
    path('qu/<int:q_id>/',qupdate, name = 'qupdate'),
    path('qd/<int:q_id>/',qdelete,name='qdelete'),
    path('cd/<int:c_id>/',cdelete, name='cdelete'),
    path('cr/',cregister, name='cregister'),
    path('cu/<int:c_id>/',cupdate, name='cupdate'),
]