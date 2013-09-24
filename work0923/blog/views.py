# Create your views here.
from django.shortcuts import render_to_response



def base(req):
    return render_to_response('base.html',{})
