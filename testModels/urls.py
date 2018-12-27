#coding utf-8
#author: pengweijian
#date: 2018/12/8

from django.contrib import admin
from django.urls import path
from testModels import views
urlpatterns = [
    # 根据app对路由规则进行分类
    # path('userInfo/', views.user_info),
    # path('login/', views.login),
    # path('home/', views.home),
    path('datamtmadd/', views.mtmdata_add),
    path('dataotoadd/', views.otodata_add),
    path('dataotmadd/', views.otmdata_add),
    path('getdata/', views.get_data),
    path('deldata/', views.del_data),
    path('weijianPage/', views.weijianPage),
]