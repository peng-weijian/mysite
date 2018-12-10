from django.shortcuts import render
from blog import models
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.
user_list = []
def user_info(req):
    if req.method == 'POST':
        # print("req.POST:",req.POST)
        username = req.POST.get("username",None)
        gender = req.POST.get("gender",None)
        age = req.POST.get("age",None)
        # user = {"username":username,"gender":gender,"age":age}
        # user_list.append(user)
        # print(user)
        models.userinfo.objects.create(
            username=username,
            gender=gender,
            age=age
        )

        user_list = models.userinfo.objects.all()
        print(user_list)
        return render(req,'userInfo.html',{"user_list":user_list})
    return render(req,'userInfo.html')

def login(req):
    if req.method == "POST":
        name = req.POST.get("username")
        # return render(req,"home.html",{"name":name})
        if 1:   #省略数据库校验，代表校验成功
            return redirect("/home")
    return render(req,"login.html")

def home(req):
    name='彭伟剑'
    return render(req,'home.html',{"name":name})

def get_time(req):
    time = datetime.now()
    return render(req,'getTime.html',{"time":time})