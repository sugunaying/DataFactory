from django.shortcuts import render
from django.contrib import auth
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required #登录验证
from django.contrib.auth.models import User#拿到user表
#request包含用户请求的一切信息都在里边，包括，用户名（固定写法request.user.username）、cookie....
from myapp.models import DB_href, DB_notice


@login_required#强制在homepage页面引入登录态检查
def homepage(request):
    res={}
    res["username"]=request.user.username
    # res["hrefs"]=DB_href.objects.all()#拿到所有QuerySet格式的数据，这个数据没办法再DOM层去用
    res["hrefs"]=list(DB_href.objects.all().values())
    res["notices"]=DB_notice.objects.all()[::-1]#从后端网前端传的时候就按照降序排序，通过列表翻转实现
    # return render(request, "home.html",{"username":request.user.username})
    return render(request, "home.html",res)

def url_read(request):
    id=request.GET["id"]
    url=DB_href.objects.all().get(id=id)
    url.count+=1
    url.save(update_fields=['count'])
    return HttpResponse("success")

def add_url(request):
    url_content=request.GET["url"]
    url_name=request.GET["url_name"]
    DB_href.objects.create(url=url_content,name=url_name)
    return HttpResponse("success")

def loginpage(request):
    return render(request, "login.html", )

def login_action(request):
    # print("login start!!!")
    #获取用户名密码
    username=request.POST.get("username",None)#没有名字，默认为none
    password=request.POST.get("password",None)#将前端input输如框中的值拿到，form表单通过将值写入属性的name中，通过name进行传输
    # print(username,password)
    #去用户表里查询用户名和密码，能找到的用户，auth去查
    user = auth.authenticate(username=username,password=password)
    # print(user)#queryset类型
    #判断是否找到用户
    if user is not None:#登录成功,登录失败user=None
        auth.login(request,user)
        request.session['user']=username
        #方法一： return render(request, "home.html",{"username":request.user.username})
        #方法二：为了防止跳转的页面输入的内容过多
        # return homepage(request)
        #方法三：重定向
        return HttpResponseRedirect('/home/')
    else: #登录失败
        print("login fail!!!!")
        # 方法一：return render(request, "login.html", {})
        #方法二:
        # return loginpage(request)
        # 方法三：重定向:
        return HttpResponseRedirect('/accounts/login/')

def logout(request):
    auth.logout(request)#把请求request的清除cookie、...
    return HttpResponseRedirect('/accounts/login/')

def register(request):
    Uname= request.POST.get('username',None)
    Pwd=request.POST.get('password',None)
    #注册
    try:
        user = User.objects.create_user(username=Uname,password=Pwd)
        user.save()
        #注册成功后进行登录
        auth.login(request,user)
        request.session['user']=Uname
        #跳转到home页面
        return HttpResponseRedirect('/home/')
    except:
        return HttpResponse("注册失败，用户名已经存在")

# python 操作数据库
