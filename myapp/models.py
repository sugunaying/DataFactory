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

#官方工具步骤
class DB_GM_steps(models.Model):
    tool_id=models.CharField("所属工具id",max_length=10)
    filter_id=models.CharField("过滤id",max_length=100,default='',blank=True,null=True)#default为空不受任何影响，必执行，不为空为2就不执行步骤2
    methods=models.CharField('类型：r-请求，s-sql，l-linux',max_length=10,null=True,default='r')#
    name=models.CharField('步骤名字',max_length=10,null=True,default='')#
    delay_before=models.IntegerField('执行步骤前延迟*秒',default='0')#有些步骤慢
    delay_after=models.IntegerField('执行步骤后延迟*秒',default='0')#
    ifdo=models.BooleanField('是否执行',default='')#不想让某一步执行
    docounts=models.IntegerField('执行次数',default='1')#
    retry=models.IntegerField('重试次数',default='0')#
    timeout=models.IntegerField('最大等待时间',default='60')#
    order=models.IntegerField('执行顺序')#
    #sql
    sql_component=models.CharField('sql组件id',max_length=10,null=True,default='')#选sql组件
    sql_body=models.CharField('sql语句体',max_length=2000,null=True,default='')
    sql_assert_str=models.CharField('sql断言返回值字符串-表达式',max_length=200,null=True,blank=True,default='')
    sql_extract_index=models.CharField('sql提取-下标法',max_length=200,null=True,default='')

    #linux
    linux_component=models.CharField('linux组件id',max_length=10,null=True,default='')#选sql组件
    linux_body=models.CharField('linux语句体',max_length=2000,null=True,default='')
    linux_assert_str=models.CharField('linux断言返回值字符串-表达式',max_length=200,null=True,blank=True,default='')
    linux_extract_re=models.CharField('linux提取-正则',max_length=200,null=True,default='')

    #request
    request_method=models.CharField('请求方式',max_length=10,null=True,default='get')#选sql组件
    request_url=models.CharField('请求url',max_length=1000,null=True,default='https://')
    request_body=models.CharField('请求体',max_length=2000,null=True,default='')
    request_body_method=models.CharField('请求体类型',max_length=20,null=True,default='form-data')
    request_headers=models.CharField('请求头',max_length=1000,null=True,default='{}')
    request_sign=models.BooleanField('是否加密验签',default=False)
    request_cert=models.BooleanField('是否带证书',default=False)
    request_assert_str=models.CharField('request断言返回值字符串-表达式',max_length=300,null=True,blank=True,default='')
    request_assert_path=models.CharField('request断言返回值字符串-路径',max_length=300,null=True,blank=True,default='')
    request_extract_re=models.CharField('request提取-正则',max_length=200,null=True,default='')
    request_extract_path=models.CharField('request提取-路径',max_length=200,null=True,default='')
    request_proxy=models.BooleanField('是否使用代理',default=False)

#官方工具表
class DB_GM_tools(models.Model):
    name = models.CharField('工具名字',max_length=100,null=True,blank=True,default='')
    def __str__(self):
        return str(self.name)

# 环境变量
class DB_PAR(models.Model):
    name = models.CharField('名字',max_length=20,null=True,blank=True,default='')
    code = models.CharField('代码',max_length=2000,null=True,blank=True,default='')
    def __str__(self):
        return str(self.name)

#服务器组件
class DB_LINUX(models.Model):
    name = models.CharField('名字',max_length=200,null=True,blank=True,default='')
    host = models.CharField('服务器的地址ip',max_length=50,null=True,blank=True,default='')
    port = models.IntegerField('端口',default=0)
    username = models.CharField('用户名',max_length=50,null=True,blank=True,default='')
    password = models.CharField('密码',max_length=50,null=True,blank=True,default='')
    def __str__(self):
        return str(self.name)

#sql组件
class DB_SQL(models.Model):
    name = models.CharField('名字', max_length=200, null=True, blank=True, default='')
    host = models.CharField('数据的地址ip', max_length=50, null=True, blank=True, default='')
    port = models.IntegerField('端口', default=0)
    db_name = models.CharField('数据库',max_length=50, null=True, blank=True, default='')
    username = models.CharField('用户名', max_length=50, null=True, blank=True, default='')
    password = models.CharField('密码', max_length=50, null=True, blank=True, default='')
    def __str__(self):
        return str(self.name)