#coding=utf-8
# Create your views here.
from django.contrib.syndication.views  import Feed
from django.shortcuts import render_to_response
from blog.models import Node,Post


def base(req):
    return render_to_response('base.html',{'n':[1,2,3]})

def index(req):
    return render_to_response('index.html',{'n':[1,2,3]})

def post(req):
    posts = Post.objects.get(id=1)
    return render_to_response('posts.html',{'n':[1,2,3],'posts':posts})

def node(req):
    nodes = Node.objects.all()
    return render_to_response('nodes.html',{'n':[1,2,3],'nodes':nodes})

def replay(req):
    return render_to_response('replay.html',{'n':[1,2,3]})

