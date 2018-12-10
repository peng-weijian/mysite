from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.template import Template, Context
import re
# Create your views here.

def time(req):
    time = datetime.now()
    return render(req,'time.html',{"time":time})

    # t = Template("<h1>当前时间为：{{ time }}</h1>")
    # c = Context({"time":time})
    # html = t.render(c)
    # return HttpResponse(html)

####### 万能的句点号 "." #########
def person_info(req):
    personInfo={"name":"peng","age":"25"}
    t = Template("my name is {{ personInfo.name }}, i am {{ personInfo.age }} years old.")
    c = Context({"personInfo":personInfo})
    page = t.render(c)
    return HttpResponse(page)

def person_info_v2(req):
    class Person():
        def __init__(self,name,age):
            self.name=name
            self.age=age
    person = Person("shuyu","26")
    print(person.name,person.age)
    t = Template("my name is {{ person.name }}, i am {{ person.age }} years old.")
    c = Context({"person":person})
    page = t.render(c)
    return HttpResponse(page)

####### 万能的句点号 "." #########


####  {% for %} ####
def member(req):
    member_list=[{"name":"shuyu","age":"26"},{"name":"manni","age":"25"},{"name":"wanyao","age":"25"}]
    return render(req,"member.html",{"member_list":member_list})

####  {% for %}  ####


#######  {% if %} tags标签 #########

def judge(req):
    if req.method == "POST":
        if re.search('[^0-9]',req.POST.get("number")):  #正则匹配，如果存在非0-9的字符，则为true
             number = req.POST.get("number")            #如果post内容含有其他非0-9字符，进行int类型转换会报错，所以才有了上面那一步
        else:
            number = int(req.POST.get("number"))        #转换为int类型才能进行比较
        return render(req, "if_tags.html", {"number":number})
    return render(req, "if_tags.html")

#######  {% if %} tags标签 #########


####### {% block %}extends继承 #########
def weijianPage(req):
    return render(req,"weijianPage.html")

def shuyuPage(req):
    return render(req, "shuyuPage.html")


####### {% block %}extends继承 #########