from django.shortcuts import render
from django.contrib import auth
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required #登录验证
from django.contrib.auth.models import User#拿到user表
from myapp.models import DB_href, DB_notice

def house_get_address():
    #通过http请求获取

    #先构造一些假数据
    return [{"name":"北京"},{"name":"上海"}]

