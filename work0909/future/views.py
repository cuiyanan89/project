# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from future.models import User,Letter
import hashlib



def index(req):
    return render(req,'index.html',{'user':None})

def regist(req):
    if req.method=="POST":
        username = req.POST.get('username',None)
        email = req.POST.get('email',None)
        password = req.POST.get('password',None)
        confirm = req.POST.get('confirm',None)
        if password == confirm:
            password = hashlib.sha1(password).hexdigest()
            user = User.objects.create(username=username,email=email,password=password)
    HttpResponseRedirect('/index/')

def login_view(req):
    pass

def logout_view(req):
    pass
#def model(req):
#    return render(req,'modal.html',{})
