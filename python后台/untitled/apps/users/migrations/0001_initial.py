# Generated by Django 2.0.3 on 2018-05-12 03:32

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('birday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=5)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
                ('signature', models.CharField(max_length=50, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tite', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(max_length=100, verbose_name='访问地址')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField(null=True)),
                ('picture', models.ImageField(default='', max_length=300, upload_to='')),
                ('video', models.ImageField(default='', upload_to='')),
                ('address', models.CharField(max_length=100, null=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('publish_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '动态',
                'verbose_name_plural': '动态',
            },
        ),
        migrations.CreateModel(
            name='EmailRecode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=10, verbose_name='验证码类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dynamic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Dynamic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '点赞',
                'verbose_name_plural': '点赞',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('picture', models.ImageField(default='', upload_to='')),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('click', models.IntegerField(default=0)),
                ('video', models.ImageField(default='', upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
        migrations.CreateModel(
            name='PrimaryRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='评论内容')),
                ('picture', models.ImageField(upload_to='primary_remark/%Y/%m', verbose_name='评论图片')),
                ('remark_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论发布时间')),
                ('remark_dynamic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Dynamic')),
                ('remark_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '一级评论',
                'verbose_name_plural': '一级评论',
            },
        ),
        migrations.CreateModel(
            name='SecondRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, null=True, verbose_name='文本')),
                ('picture', models.ImageField(max_length=600, null=True, upload_to='primary_remark/%Y/%m', verbose_name='评论图片')),
                ('remark_time', models.DateTimeField(verbose_name='评论时间')),
                ('primary_remark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.PrimaryRemark')),
                ('remark_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '二级评论',
                'verbose_name_plural': '二级评论',
            },
        ),
        migrations.AddField(
            model_name='collections',
            name='dynamic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Dynamic'),
        ),
        migrations.AddField(
            model_name='collections',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
