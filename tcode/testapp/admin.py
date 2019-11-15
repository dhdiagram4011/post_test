from django.contrib import admin
from .models import Post
from .models import Serverlist
#from .models import Selecttest
#from .models import Radiotest
from .models import Transpost
from .models import Login
# Register your models here.

admin.site.register(Post)
#admin.site.register(Serverlist)
admin.site.register(Login)

class TranspostOption(admin.ModelAdmin):
    list_display  = ['id','document','language','language_result','created_date']


admin.site.register(Transpost, TranspostOption)


class ServerlistOPT(admin.ModelAdmin):
    list_display=['name','team','server_count','model_name','code','use_case','created_date','published_date']

admin.site.register(Serverlist,ServerlistOPT)

