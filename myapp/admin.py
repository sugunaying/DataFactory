from django.contrib import admin
#此模块即代表后台
# Register your models here.
from myapp.models import *

admin.site.register(DB_href)
admin.site.register(DB_notice)
admin.site.register(DB_SQL)
admin.site.register(DB_LINUX)
admin.site.register(DB_GM_steps)
admin.site.register(DB_PAR)
admin.site.register(DB_GM_tools)
