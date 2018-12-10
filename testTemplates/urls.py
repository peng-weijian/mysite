#coding utf-8
#author: pengweijian
#date: 2018/12/8

from django.contrib import admin
from django.urls import path
from testTemplates import views

urlpatterns = [
    # 根据app对路由规则进行分类
    # path('userInfo/', views.user_info),
    # path('login/', views.login),
    # path('home/', views.home),
    path('time/', views.time),
    path('personInfo/', views.person_info),
    path('personInfo_v2/', views.person_info_v2),
    path('member/', views.member),
    path('if/', views.judge),
    path('weijianPage/', views.weijianPage),
    path('shuyuPage/', views.shuyuPage),

]