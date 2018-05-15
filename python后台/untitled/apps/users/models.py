from datetime import  datetime

from django.db import models
from  django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name='昵称',default='')#看官方文档 verbose_name是什么鬼
    birday=models.DateField(verbose_name='生日',null=True,blank=True)
    gender=models.CharField(max_length=5,choices=(("male","男"),("female","女"))) #看官方文档 choices怎么用
    address=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100)#看官方文档
    signature = models.CharField(max_length=50, null=True)
    is_admin = models.BooleanField(default=False)


    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username


class EmailRecode(models.Model):
    code=models.CharField(max_length=20,verbose_name="验证码")
    email=models.EmailField(max_length=50,verbose_name="邮箱")
    send_type=models.CharField(choices=(("register","注册"),("forget","找回密码")),max_length=10,verbose_name="验证码类型")
    send_time=models.DateTimeField(default=datetime.now,verbose_name="发送时间")

    class Meta:
        verbose_name="邮箱验证码"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.email


class Banner(models.Model):
    tite=models.CharField(max_length=100,verbose_name="标题")
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name='轮播图')
    url=models.URLField(max_length=100,verbose_name='访问地址')
    index=models.IntegerField(default=100,verbose_name='顺序')
    add_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name='轮播图'
        verbose_name_plural=verbose_name


class News(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    picture = models.ImageField(default='')
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now_add=True)
    click = models.IntegerField(default=0)
    video = models.ImageField(default='')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.title)


class Dynamic(models.Model):
    publish_user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    text = models.TextField(null=True)
    picture = models.CharField(default='',max_length=500)
    video = models.ImageField(default='')
    address = models.CharField(max_length=100,null=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    zan=models.IntegerField(default=0)
    comment=models.IntegerField(default=0)

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.publish_user)


class Collections(models.Model):
    dynamic = models.ForeignKey(Dynamic, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.dynamic

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name


class Like(models.Model):
    dynamic = models.ForeignKey(Dynamic, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.dynamic

    class Meta:
        verbose_name = "点赞"
        verbose_name_plural = verbose_name


class PrimaryRemark(models.Model):
    text = models.TextField(verbose_name='评论内容')
    picture = models.ImageField(upload_to="primary_remark/%Y/%m", verbose_name=u'评论图片', max_length=100)
    remark_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    remark_dynamic = models.ForeignKey(Dynamic, on_delete=models.CASCADE)
    remark_time = models.DateTimeField(default=datetime.now, verbose_name='评论发布时间')

    def __str__(self):
        return '%s %s' % (self.text, self.picture)

    class Meta:
        verbose_name = '一级评论'
        verbose_name_plural = verbose_name


class SecondRemark(models.Model):
    text = models.CharField(max_length=100, null=True, verbose_name="文本")
    picture = models.ImageField(upload_to="primary_remark/%Y/%m", max_length=600,null=True, verbose_name="评论图片")
    remark_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    primary_remark = models.ForeignKey(PrimaryRemark, on_delete=models.CASCADE)
    remark_time = models.DateTimeField(verbose_name="评论时间")

    def __str__(self):
        return self.text, self.picture, self.remark_time

    class Meta:
        verbose_name = "二级评论"
        verbose_name_plural = verbose_name
