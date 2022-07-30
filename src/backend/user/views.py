from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
# import logging
import json
from .models import User


def index(request):
    pass
    return HttpResponse("index")


def login(request):
    if request.method == 'POST':
        # logging.debug(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('passwd', None)
        if username and password:
            username = username.strip()
            try:
                user = User.objects.filter(username=username)
                sendData = json.loads(serializers.serialize('json', user, ensure_ascii=False))
            except:
                return HttpResponse('connect db failed')
            if sendData[0]['fields']['passwd'] == password:
                # request.session["info"] = {'id': user.id, 'username': user.username}

                user = User.objects.get(username=username)
                # 设置session
                request.session['is_login'] = "1"
                request.session['username'] = username
                # request.session["info"] = {'id': user.id,'username': username}
                request.session['userid'] = user.id
                # session可以保存7天
                request.session.set_expiry(60 * 60 * 24 * 7)

                userid = request.session.get('userid')
                username = request.session.get('username')

                # if not request.session.session_key:
                #     # request.session.create()
                #     request.session.save()
                # session_ID = request.session.session_key

                return HttpResponse("userpass")
        return HttpResponse("NO!!!")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        email = request.POST.get('email')
        user = User(
            username=username,
            passwd=password,
            email=email
        )
        user.save()

    return HttpResponse("registersuccess")
