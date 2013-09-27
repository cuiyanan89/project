#coding=utf-8
# Create your views here.
from django.contrib.syndication.views  import Feed
from django.shortcuts import render_to_response
from blog.models import Node,Post


def index(req):
    notices = Node.objects.filter(nodename="Notice")[0].post_set.all()
    nodes = Node.objects.order_by('-create_time')[:5]
    posts = Post.objects.order_by('-create_time')[:10]
    return render_to_response('index.html',{'notices':notices,'nodes':nodes,'posts':posts})

def post(req):
    nodes = Node.objects.all()
    posts = Post.objects.all()
    id = req.GET.get('id',None)
    if id:
        post = Post.objects.get(id=id)
        return render_to_response('posts.html',{'nodes':nodes,'posts':posts,'post':post})
    else:
        return render_to_response('postlists.html',{'nodes':nodes,'posts':posts})

def node(req):
    nodes = Node.objects.all()
    posts = Post.objects.all()
    id = req.GET.get('id',None)
    if id:
        node = Node.objects.get(id=id)
        return render_to_response('nodes.html',{'nodes':nodes,'posts':posts,'node':node})
    else:
        return render_to_response('nodelists.html',{'nodes':nodes,'posts':posts})

def replay(req):
    nodes = Node.objects.all()
    posts = Post.objects.all()
    return render_to_response('replay.html',{'nodes':nodes,'posts':posts})
