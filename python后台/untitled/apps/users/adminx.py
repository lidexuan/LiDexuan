import xadmin
from .models import *
from xadmin import views

class BaseSetting(object):
    enable_themes=True
    use_bootwatch=True


class GlobalSeettings(object):
    site_title="云顶后台管理"
    site_footer="云顶在线网"
    menu_style="accordion" #将菜单收起来

class EmailRecodeAdmin(object):
    list_display=['code','email','send_type','send_time']
    search_fields=['code','email','send_type']
    list_filter=['code','email','send_type','send_time']

class Newsadmin():
    list_display = ['id','title','text','picture','video','author','publish_time','click']
    search_fields = ['title','author','publish_time']
    list_filter = ['title','author','publish_time','click']


class Dynamicadmin():
    list_display = ['id','publish_user','text','picture','video','publish_time']
    search_fields = ['publish_user','publish_time']
    list_filter = ['publish_user','publish_time']

class CollectionsAdmin(object):
    list_display = ['dynamic','user']
    search_fields = ['dynamic','user']
    list_filter = ['dynamic','user']

class LikeAdmin(object):
    list_display = ['dynamic','user']
    search_fields = ['dynamic','user']
    list_filter = ['dynamic','user']

class Primary_remarkAdmin(object):
    list_display =['text','picture','remark_user','remark_dynamic','remark_time']
    search_fields = ['text','remark_user','remark_dynamic']
    list_filter = ['text','remark_user','remark_dynamic','remark_time']

class SecondRemarkAdmin(object):
    list_display = ['text','remark_user','primary_remark']
    search_fields =['text','remark_user','primary_remark']
    list_filter = ['text','remark_user','primary_remark']


xadmin.site.register(EmailRecode,EmailRecodeAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSeettings)
xadmin.site.register(Collections,CollectionsAdmin)
xadmin.site.register(PrimaryRemark,Primary_remarkAdmin)
xadmin.site.register(Like,LikeAdmin)
xadmin.site.register(SecondRemark,SecondRemarkAdmin)
xadmin.site.register(News,Newsadmin)
xadmin.site.register(Dynamic,Dynamicadmin)