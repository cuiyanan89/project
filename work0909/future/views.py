# Create your views here.
from django.shortcuts import render,render_to_response




def index(req):
    return render(req,'index.html',{})
