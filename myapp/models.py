from django.db import models

# Create your models here.
from django.utils import timezone


class DB_href(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,null=True,blank=True)
    url=models.CharField(max_length=1000,null=True,blank=True)#后台长度限制
    count=models.PositiveIntegerField(verbose_name="浏览量",default=0)#PositiveIntegerField为正整数

    def __str__(self):#作用：展示指定return数据，避免展示全部数据
        return str(self.name)

class DB_notice(models.Model):
    stime=models.DateTimeField('保存日期',default = timezone.now)
    ncontent=models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return str(self.ncontent)#注：此处最好用str包一下，