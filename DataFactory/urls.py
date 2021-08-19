"""DataFactory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#路由与视图函数（views.py）
from myapp.views import homepage, login_action, loginpage, logout,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage),#进入主页
    path('accounts/login/', loginpage),#进入登录页面
    path('login_action/', login_action),#点击登录
    path('logout/', logout),#点击登录
    path('register/', register),#点击登录
]
