from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    city = models.CharField('城市', max_length=60)
    state_province = models.CharField(max_length=30)
    website = models.URLField()

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男'), (1, '女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE,)
    #在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错：
    #TypeError: __init__() missing 1 required positional argument: 'on_delete'


class Book(models.Model):
    title = models.CharField(max_length=10)
    authors = models.ManyToManyField(Author)    #多对多，多个作者对应多本书，自动创建第三张表
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,)    #一对多，一个出版社对应多本书。在book表创建外键
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)

    def __str__(self):
        return self.title