from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.contrib.auth.backends import ModelBackend
from users.models import UserProfile,News
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm
from django.http import HttpResponse
from users.models import Dynamic
import json,time,re
from datetime import date, datetime

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username)|Q(phone=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class LoginView1(View):
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username")
            pass_word = request.POST.get("password")
            users = authenticate(username=user_name, password=pass_word)
            return HttpResponse("{'status':'sucess'}",content_type='application/json' )
        else:
            return HttpResponse("{'status':'fail'}",content_type='application/json')
    def get(self,request):
        return render(request, "index.html", {})


class LoginView(View):
    def post(self, request):
        user_obj = json.loads(request.body.decode())
        user_name=user_obj['username']
        pass_word=user_obj['password']
        users = authenticate(username=user_name, password=pass_word)
        if users is not None:
            userID=UserProfile.objects.get(username=user_name).id
            nick_name=UserProfile.objects.get(username=user_name).nick_name
            return HttpResponse("{'status':'sucess','userID':%d,'nick_name':%s}"%(userID,nick_name), content_type='application/json')
        else:
            return HttpResponse("{'status':'fail'}",content_type='application/json')

    def get(self, request):
        return render(request, "course-comment.html", {})


class Dynamic_publishing(View):
    def post(self,request):
        images={}
        length=int(request.POST['length'])
        text=request.POST['text']
        address=request.POST['address']
        id=request.POST['id']
        if address=="地址":
            address=""
        dynamic=Dynamic()
        if length ==0:
            dynamic.text=text
            dynamic.address=address
            dynamic.publish_user_id=id
            dynamic.save()

        else:
            for i in range(0,length):
                Time=time.time()
                path = "media/" + str(Time) + ".jpg"
                image = request.FILES.get('file'+str(i))
                with open(path, 'wb')as f:
                    for chunk in image.chunks():
                        f.write(chunk)

            dynamic.picture = path
            dynamic.text = text
            dynamic.address = address
            dynamic.publish_user_id = id
            dynamic.save()
        return HttpResponse("{'status':%s}", content_type='application/json')

#0是一个图片的新闻，1是视频的新闻，2是3个图片的新闻
class NewsView(View):
    def get(self,request):
        newlist={

                 'length':2,
                 'datas':[
                     {
                         'id':1,
                         'type':0,
                         'name':"在这样一所“别人家的校园”读大学是怎样的体验？",
                         'commentCount': 0,
                         'FromName': 'lidexuan',
                         'url': 'http://192.168.31.159:8000/media/20180423201801.jpg',
                         'time':'2018.4.23  7:00'

                     },
                     {
                         'id':2,
                         'type':0,
                         'name': "云顶开始招募啦",
                         'commentCount': 0,
                         'FromName': 'lidexuan',
                         'url':  'http://192.168.31.159:8000/media/2018423.png',
                         'time': '2018.4.23  9:00'
                     },
                     {
                         'id': 1,
                         'type': 2,
                         'name': "快来一起参观云顶逸庐！",
                         'commentCount': 0,
                         'FromName': 'lidexuan',
                         'url_0': 'http://192.168.31.159:8000/media/1.jpg',
                         'url_1': 'http://192.168.31.159:8000/media/2.jpg',
                         'url_2': 'http://192.168.31.159:8000/media/3.jpg',
                         'time': '2018.4.24  13:00'

                     },
                     {
                         'id': 1,
                         'type': 2,
                         'name': "恭喜楼下超算团队在超算比赛中荣获一等奖",
                         'commentCount': 0,
                         'FromName': 'lidexuan',
                          'url_0': 'http://192.168.31.159:8000/media/4.jpg',
                         'url_1': 'http://192.168.31.159:8000/media/5.jpg',
                         'url_2': 'http://192.168.31.159:8000/media/6.jpg',
                         'time': '2018.4.23  7:00'

                     },
                     {
                         'id': 1,
                         'type': 1,
                         'name': "太原理工大学云顶空间宣传片来啦！！！",
                         'commentCount': 0,
                         'FromName': 'lidexuan',
                         'video_url': 'http://192.168.31.159:8000/media/video.mp4',
                          'url':'http://192.168.31.159:8000/media/video.png',
                         'time': '2018.4.20  19:00'

                     },
                     {
                         'id': 2,
                         'type': 0,
                         'name': "在这样一所“别人家的校园”读大学是怎样的体验？",
                         'commentCount': 0,
                         'FromName': 'lidexuan',
                         'url': 'http://192.168.31.159:8000/media/20180423201801.jpg',
                         'time': '2018.4.23  7:00'

                     },
                     {
                         'id': 2,
                         'type': 0,
                         'name': "在这样一所“别人家的校园”读大学是怎样的体验？",
                         'commentCount': 0,
                         'FromName': 'lidexuan',
                         'url': 'http://192.168.31.159:8000/media/20180423201801.jpg',
                         'time': '2018.4.23  7:00'

                     },
                 ]

                 }
        return HttpResponse(str(newlist),content_type='application/json')

class Mobile(View):
    def post(self,request):
        user_obj = json.loads(request.body.decode())
        type=user_obj['type']
        if type=='0':
           phone=user_obj['phone']
           phoneinfo=UserProfile.objects.filter(phone=phone)
           if phoneinfo:
               return HttpResponse("{'status':'fail'}", content_type='application/json')
           else:
               return HttpResponse("{'status':'sucess'}", content_type='application/json')
        if type=='1':
            password=user_obj['password']
            phone=user_obj['phone']
            nickname=user_obj['nickname']
            nameinfo=UserProfile.objects.filter(nick_name=nickname)
            if nameinfo:
                return HttpResponse("{'status':'fail'}", content_type='application/json')
            else:

               user=UserProfile()
               user.phone=phone
               user.username=phone
               user.nick_name=nickname
               user.password=password
               user.save()
               return HttpResponse("{'status':'sucess'}", content_type='application/json')

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

class MyEncoder(json.JSONEncoder):
  def default(self, obj):
      # if isinstance(obj, datetime.datetime):
      #     return int(mktime(obj.timetuple()))
      if isinstance(obj, datetime):
          return obj.strftime('%Y-%m-%d %H:%M:%S')
      elif isinstance(obj, date):
          return obj.strftime('%Y-%m-%d')
      else:
          return json.JSONEncoder.default(self, obj)


class Square(View):
    def get(self,request):
        newlist={}
        datas=[]
        dynamic=Dynamic.objects.order_by('-id')
        for i in dynamic:
            if i.picture:
             datas.append({
                'number':1,
                'text':i.text,
                'picture':i.picture,
                'nickname':UserProfile.objects.get(id=1).nick_name,
                'publish_time':json.dumps(i.publish_time, cls=MyEncoder).replace("\"", ""),
                'zan':i.zan,
                'comment':i.comment

            })
            else:
                datas.append({
                'number':2,
                'text':i.text,
                'picture':'http://192.168.31.159:8000/media/20180423201801.jpg',
                'nickname':UserProfile.objects.get(id=1).nick_name,
                'publish_time':json.dumps(i.publish_time, cls=MyEncoder).replace("\"", ""),
                'zan':i.zan,
                'comment':i.comment

            })

        newlist={
            'length':2,
            'datas':datas,

        }
        return HttpResponse(str(newlist),content_type='application/json')

class Newspage(View):
    def get(self,request):
        pass




