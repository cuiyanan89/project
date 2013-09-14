# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from future.models import User,Letter
from django.core.paginator import Paginator
import hashlib
from message import singleton,CheckAndSend



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
            req.session['user'] = user
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
        letters = user.letter_set.all()
        p = Paginator(letters,10)
        page = req.GET.get('page',1)
        contacts = p.page(page)
        re_text['contacts'] = contacts
    return render(req,'myaccount.html',re_text)

def letter(req):
    if req.method=="POST":
        email = req.POST.get('email',None)
        subject = req.POST.get('subject',None)
        text = req.POST.get('text',None)
        deliver = req.POST.get('deliver',None)
        public = req.POST.get('visible',None)
        picture = req.FILES.get('picture',None)
        if public == 't':
            public = True
        else:
            public = False
        if req.session.has_key('user'):
            user = req.session.get('user',None)
            user.letter_set.create(email=email,subject=subject,text=text,deliverdate=deliver,public=public,picture=picture)
    return HttpResponseRedirect('/index/')

def edit(req):
    if req.method == "POST":
        email = req.POST.get('email',None)
        username = req.POST.get('username',None)
        password = req.POST.get('password',None)
        user =req.session.get('user',None)
        if user.password == hashlib.sha1(password).hexdigest():
            user.email = email
            user.username = username
            user.save()
            req.session['user'] = user
        if req.POST.has_key('index'):
            return HttpResponseRedirect('/index/')
    return HttpResponseRedirect('/account/')


def change_view(req):
    if req.method == "POST":
        current = req.POST.get('current',None)
        new = req.POST.get('new',None)
        repeat = req.POST.get('repeat',None)
        if new == repeat:
            user = req.session.get('user',None)
            if user.password == hashlib.sha1(current).hexdigest():
                user.password = hashlib.sha1(new).hexdigest()
                user.save()
                req.session['user'] = user
    return HttpResponseRedirect('/account/')

def delete_view(req):
    user = req.session.get('user',None)
    user.delete()
    req.session.clear()
    return HttpResponseRedirect('/index/')

def showletter(req):
    re_text = {'user':None}
    if req.session.has_key('user'):
        user = req.session['user']
        re_text['user'] = user
    letters = Letter.objects.filter(public=True)
    p = Paginator(letters,4)
    page = req.GET.get('page',1)
    contacts = p.page(page)
    re_text['contacts'] = contacts
    return render(req,'showletter.html',re_text)

def edit_letter(req):
    if req.method == "POST":
        email = req.POST.get('email',None)
        public = req.POST.get('visible',None)
        print public
        if public == 't':
            public = True
        else:
            public = False
        id = req.POST.get('id',None)
        user = req.session.get('user',None)
        letter = user.letter_set.get(id=id)
        letter.email = email
        letter.public = public
        letter.save()
    return HttpResponseRedirect('/account/')

def del_letter(req):
    letter = Letter.objects.get(id=req.GET.get('id'))
    letter.delete()
    return HttpResponseRedirect('/account/')

def search_view(req):
    re_text = {'user':None}
    if req.session.has_key('user'):
        user = req.session['user']
        re_text['user'] = user
    search_letter = []
    letters = Letter.objects.filter(public=True)
    if req.method == "POST":
        search_text = req.POST.get('search_text',None)
        if search_text:
            for letter in letters:
                if search_text in letter.subject:
                    search_letter.append(letter)

    p = Paginator(search_letter,4)
    page = req.GET.get('page',1)
    contacts = p.page(page)
    re_text['contacts'] = contacts
    return render(req,'showletter.html',re_text)
