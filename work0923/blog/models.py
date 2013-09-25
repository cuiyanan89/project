from django.db import models

# Create your models here.
class Node(models.Model):
    nodename = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nodename

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=5000)
#    content_html = models.TextField(max_length=10000)
    create_time = models.DateField(auto_now_add = True)
    node = models.ForeignKey(Node)

    def __unicode__(self):
        return self.title
