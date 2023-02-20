from django.urls import path
from .views import *

urlpatterns = [
    path('',signup_page,name='signup_page'),
    path('signin_page',signin_page,name='signin_page'),
    path('index_page',index_page,name='index_page'),
    path('aotp_page',aotp_page,name='aotp_page'),
    path('cotp_page',cotp_page,name='cotp_page'),
    path('Signup',Signup,name='Signup'),
    path('Signin',Signin,name='Signin'),
    path('cotp',cotp,name='cotp'),
    path('aotp',aotp,name='aotp'),
]
