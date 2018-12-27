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
    book=models.Book.objects.get(title='JAVA')
    book.authors.add(*[author_1,author_2])
    return HttpResponse("OK")

#一对一
def otodata_add(req):
    ### 方式一
    author_obj = models.Author.objects.get(name="nami")
    models.AuthorDetail.objects.create(sex=True,email='nami@flb.com',address='gl',birthday='2019-10-10',author=author_obj)
    return HttpResponse("author info add!")

def get_data(req):
    publisher = models.Publisher.objects.get(name="新华社")
    pub_id =  publisher.id
    book_set = models.Book.objects.filter(publisher_id=pub_id)
    print(book_set)
    return HttpResponse("GET BOOK INFO")


def del_data(req):
    book = models.Book.objects.filter(title='JAVA')[0]
    print(book)
    # book.authors.remove(2)  #remove方法要指定authorid
    book.authors.clear()    #clear方法删除所有author

    return HttpResponse("author info del")

def weijianPage(req):
    return render(req,"weijianPage.html")