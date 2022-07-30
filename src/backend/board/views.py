from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from user.models import UserBoardPost
from .models import Post


# import logging

def index(request):
    # logging.debug("index success")
    tmp_data = Post.objects.all().order_by('-created_time')
    post_list = serializers.serialize('json', tmp_data, ensure_ascii=False)
    response = HttpResponse()
    response["Access-Control-Allow-Origin"] = 'http://localhost:8080'
    response.content = post_list
    # return HttpResponse(post_list)
    return response


def addMessage(request):
    # logging.debug("add mess request success")
    username = request.POST.get('username')
    body = request.POST.get('content')
    created_time = request.POST.get('created_time')
    tag = request.POST.get('tag')
    user = Post(
        author=username,
        created_time=created_time,
        body=body,
        tag=tag
    )
    user.save()

    return HttpResponse("messagesuccess")


def addVote(request):
    # logging.debug("add vote request success")
    author = request.POST.get('author')
    good = request.POST.get('good')
    created_time = request.POST.get('created_time')

    post = Post.objects.get(author=author, created_time=created_time)

    boardpostid = post.id

    # 查看之前是否踩赞过
    # if not request.session.session_key:
    #     request.session.create()
    # session_ID = request.session.session_key
    # if not request.session.session_key:
    #     # request.session.create()
    #     request.session.save()
    # session_ID = request.session.session_key

    keys = request.session.keys()
    values = request.session.values()
    items = request.session.items()

    if "username" in request.session:
        result = request.session["username"]
    else:
        result = False

    # userid = request.session["info"]["id"]
    userid = request.session.get('userid')
    username = request.session.get('username')
    # userid = request.session['userid']
    # username = request.session['username']

    current_user = request.user
    userid = current_user.id
    try:
        user_userboardpost = UserBoardPost.objects.get(userid=userid, boardpostid=boardpostid, good=1)
        return HttpResponse("您已赞过")

    except UserBoardPost.DoesNotExist:

        # 增加记录
        user_userboardpost = UserBoardPost(
            userid=userid,
            boardpostid=boardpostid,
            good=1,
        )
        user_userboardpost.save()

        post.good = good
        post.save()
        return HttpResponse("赞成功")


def addRefuse(request):
    # logging.debug("add refuse request success")
    author = request.POST.get('author')
    bad = request.POST.get('bad')
    created_time = request.POST.get('created_time')
    post = Post.objects.get(author=author, created_time=created_time)
    post.bad = bad
    post.save()

    return HttpResponse("refusesuccess")
