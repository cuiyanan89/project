# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect




def index(req):
    return render(req,'index.html',{'user':None})

def regist(req):
    pass

def login_view(req):
    pass

def logout_view(req):
    pass
#def model(req):
#    return render(req,'modal.html',{})
