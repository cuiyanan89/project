# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from future.models import User,Letter
import hashlib



def index(req):
    re_text = {'user':None}
    if req.session.has_key('user'):
        user = req.session['user']
        re_text['user'] = user
    return render(req,'index.html',re_text)

def regist(req):
    if req.method=="POST":
        username = req.POST.get('username',None)
        email = req.POST.get('email',None)
        password = req.POST.get('password',None)
        confirm = req.POST.get('confirm',None)
        if password == confirm and password != '':
            password = hashlib.sha1(password).hexdigest()
            user = User.objects.create(username=username,email=email,password=password)
    return HttpResponseRedirect('/index/')

def login_view(req):
    if req.method=="POST":
        email = req.POST.get('email',None)
        password = req.POST.get('password',None)
        print "email-->",email,"password-->",password
        try:
            user = User.objects.get(email=email,password=hashlib.sha1(password).hexdigest())
            req.session['user'] = user
        except:
            pass
    return HttpResponseRedirect('/index/')
        

def logout_view(req):
    req.session.clear()
    return HttpResponseRedirect('/index/')

def account(req):
    re_text = {'user':None}
    if req.session.has_key('user'):
        user = req.session['user']
        re_text['user'] = user
    return render(req,'myaccount.html',re_text)
#def model(req):
#    return render(req,'modal.html',{})
