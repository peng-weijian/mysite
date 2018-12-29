from django.shortcuts import render,HttpResponse
from testModels import models

# Create your views here.

#一对多
def otmdata_add(req):
    ### 方式一
    book = models.Book.objects.create(title="PHP",publisher_id="1",price='25')
    book.save()
    return HttpResponse("book info add!")


#多对多
def mtmdata_add(req):
    ### 方式一
    # author_obj = models.Author.objects.get(name="nami")
    # book_set = models.Book.objects.filter(publisher_id="2")
    # author_obj.book_set.add(*book_set)

    ### 方式二

    author_1 = models.Author.objects.get(name='shuyu')
    author_2 = models.Author.objects.get(name='nami')
    book=models.Book.objects.get(title='PHP')
    book.authors.add(*[author_1,author_2])
    return HttpResponse("OK")

#一对一
def otodata_add(req):
    ### 方式一
    author_obj = models.Author.objects.get(name="shuyu")
    models.AuthorDetail.objects.create(sex=False,email='shuyu@flb.com',address='sz',birthday='2019-10-24',author=author_obj)
    return HttpResponse("author info add!")

def get_data(req):
    publisher = models.Publisher.objects.get(name="新华社")
    pub_id =  publisher.id
    book_set = models.Book.objects.filter(publisher_id=pub_id)
    print("book_set:" , book_set)
    print("book_set[0]:" , book_set[0])
    print("book_set.all():",book_set.all())
    print("book_set.all().values('title'):" ,book_set.all().values("title"))

    return HttpResponse("GET BOOK INFO")


def del_data(req):
    book = models.Book.objects.filter(title='JAVA')[0]
    print(book)
    # book.authors.remove(2)  #remove方法要指定authorid
    book.authors.clear()    #clear方法删除所有author

    return HttpResponse("author info del")

def dataselect(req):
    if req.method == "POST":
        print(req.POST)
        author_name = req.POST.get("author_name",None)
        author=models.Author.objects.filter(name=author_name).first()
        # query_set.first()  """Return the first object of a query or None if no match is found."""
        # author=models.Author.objects.filter(name=author_name)[0]  #如果query_set为空，会报错：list index out of range
        print(author)
        return render(req,"select.html",{"author":author})
    return render(req,"select.html")


def submit_book_info(req):
    author_list = []
    if req.method == "POST":
        print(req.POST)
        book_title = req.POST.get("title",None)
        book_publisher_name = req.POST.get("publisher", None)
        book_publisher_obj = models.Publisher.objects.get(name=book_publisher_name)
        book_price = req.POST.get("price", None)
        book = models.Book.objects.create(title=book_title, publisher=book_publisher_obj, price=book_price)  # 一对多创建对象
        author_1_name = req.POST.get("author_1",None)
        author_2_name = req.POST.get("author_2",None)   #拿到作者姓名
        if author_1_name:   #如果提交不为空
            author_obj_1 = models.Author.objects.filter(name=author_1_name).first()
            if not author_obj_1:  # 已有作者表中不存在这个作者
                author_obj_1 = models.Author.objects.create(name=author_1_name)
                author_list.append(author_obj_1)
        if author_2_name:
            author_obj_2 = models.Author.objects.filter(name=author_2_name).first()
            if not author_obj_2:  # 已有作者表中不存在这个作者
                author_obj_2 = models.Author.objects.create(name=author_2_name)
                author_list.append(author_obj_2)

        book.authors.add(*author_list)  #多对多插入对象信息
        success_info = "书籍信息提交成功!"
        return render(req,"submit_book_info.html",{"success_info":success_info})
    return render(req,"submit_book_info.html")


def data_filter(req):
    book_set_1 = models.Book.objects.filter(publisher_id__gte=2,title__icontains="P").values("title")   #逗号 ，是 并 的关系
    book_set_2 = models.Book.objects.filter(publisher_id__gte=2,title__startswith="P").values("title")
    print(book_set_1)
    print(book_set_2)
    return HttpResponse("GET BOOKSET")

def weijianPage(req):
    return render(req,"weijianPage.html")