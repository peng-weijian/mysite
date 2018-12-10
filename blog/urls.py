#coding utf-8
#author: pengweijian
#date: 2018/12/8

from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # 根据app对路由规则进行分类
    path('userInfo/', views.user_info),
    path('login/', views.login),
    path('home/', views.home),
    path('get_time/', views.get_time),
]