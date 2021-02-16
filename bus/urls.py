from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('buslist',bus_list,name='buslist'),
    path('busdetail/<slug:slug_text>',bus_detail,name='busdetail'),
    path('data/<str:slug_lat>/<str:slug_lng>/<slug:slug_uid>',bus_track,name='bustrack'),
    path('register',user_registration,name='register'),
    path('login',user_login,name='user_login'),
    path('logout',user_logout,name='logout')

]
