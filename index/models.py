from django.db import models

# Create your models here.
class Accountinfo(models.Model):
    username=models.CharField('用户名',max_length=30)
    password=models.CharField('登录密码',max_length=30)
    email=models.EmailField('登录邮箱',max_length=40)

class Basicinfo(models.Model):
    gender=models.CharField('性别',max_length=1)
    ageday=models.IntegerField('天',max_length=2)
    ageyear=models.IntegerField('年',max_length=4)
    agemonth=models.IntegerField('月',max_length=2)
    marrystat=models.CharField('婚姻状况',max_length=1)
    education=models.CharField('学历',max_length=1)
    height=models.IntegerField('身高',max_length=3)
    weight=models.IntegerField('体重',max_length=3)
    province=models.CharField('所在地区',max_length=2)


    lovesort=models.CharField('交友类型',max_length=1)

    qq=models.CharField('QQ号码',max_length=15)
    homepage=models.CharField('微博/博客',max_length=30)

    idnumber=models.CharField('身份证号码',max_length=18)


