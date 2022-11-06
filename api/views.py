# PYTHON3.7
import os
import time
import threading
import requests
from django.views import View
from django.http import JsonResponse, HttpResponse
from duniapp import settings
from api.unit import gettoken as gt
from api.unit import logincl as ll
from api.unit import IdWorker
from duniapp.settings import APPID, SECRET
from api.models import FUSER, SCHOOL

lock = threading.Lock()


# 存储博客
class SETBLOG(View):

    def ultip(self, img):

        lock.acquire()
        self.filename = img.name
        dir_path = os.path.join(settings.BASE_DIR, 'media')
        print("=============")
        file_path = os.path.join(dir_path, self.filename)
        print(file_path)
        with open(file_path, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)

    def post(self, request):
        img = request.FILES.get('files', None)
        th = threading.Thread(target=self.ultip, args=(img,))
        th.run()
        json = {
            'code': 0,
            'msg': 'success'
        }
        if lock.release() is None:
            return JsonResponse(json)


# code交换openid
class GETOPPENID(View):

    def post(self, request):
        import json
        code = json.loads(request.body.decode().replace("'", "")).get('code')
        appid = APPID
        secret = SECRET
        url = f' https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'
        res = requests.get(url=url).json()
        openid = res.get('openid')
        session_key = res.get('session_key')
        res = ll(openid, session_key)

        json = {
            'openid': openid,
            'data': res
        }

        return JsonResponse(json)


class GETPHONE(View):

    def post(self, request):
        code = request.POST.get('code')
        res = gt()
        token = res.get('access_token')
        url = f'https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token={token}'
        json = {
            'code': code
        }
        res = requests.post(url=url, json=json)

        print(res)


class SETUSER(View):

    def post(self, request):

        openid = request.POST.get('openid')
        tx = request.POST.get('tx')
        agm = request.POST.get('agm')
        sid = request.POST.get('sid')
        unc = request.POST.get('unc')
        ph = request.POST.get('ph')
        getid = IdWorker(1)
        uid = getid.get_id()
        FUSER.objects.create(u_id=uid, open_id=openid, t_x=tx, u_nc=unc, a_g=agm, s_id=sid, u_p=ph)
        user = FUSER.objects.get(open_id=openid)
        if user:

            json = {
                'code': 0,
                'msg': 'success',
                'ret': 0,
                'uid': uid
            }

        else:

            json = {
                'code': 1,
                'msg': 'fail',
                'ret': 1
            }

        return JsonResponse(json)


class SETSCHOOL(View):

    def get(self, request):

        sn = request.GET.get('sn')

        if sn is None:
            res = list(SCHOOL.objects.values().all())

        else:
            res = list(SCHOOL.objects.values().filter(schoolname__contains=sn))

        return JsonResponse(res, safe=False)
