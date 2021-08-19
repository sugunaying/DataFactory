from django.contrib import admin
#此模块即代表后台
# Register your models here.
from myapp.models import DB_href, DB_notice

admin.site.register(DB_href)
admin.site.register(DB_notice)
