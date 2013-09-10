from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=100)

class Letter(models.Model):
    email = models.EmailField(max_length=75)
    subject = models.CharField(max_length=50)
    text = models.TextField()
    deliverdate = models.DateField()
    currentdate = models.DateField(auto_now_add =True)
    picture = models.FileField(upload_to='./picture',blank=True,null=True)
    user = models.ForeignKey(User)
