from django.db import models
#from markdown import markdown

# Create your models here.

class Node(models.Model):
    nodename = models.CharField(max_length=30)
    create_time = models.DateField(auto_now_add = True)

    def __unicode__(self):
        return self.nodename

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=5000)
#    content_html = models.TextField(blank=True,null=True)
    create_time = models.DateField(auto_now_add = True)
    node = models.ForeignKey(Node)

    def __unicode__(self):
        return self.title

#    def save(self):
#        self.content_html = markdown(self.content,['codehilite'])
