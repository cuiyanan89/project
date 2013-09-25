from django.contrib.syndication.views import Feed
from markdown import markdown
from blog.models import Post

class RSSFeed(Feed):
    title = u"cuiyanan's blog"
    link = 'feeds'
    description = 'about yanan'
    def items(self):
#        return Post.objects.all()
        return Post.objects.order_by('-create_time')[:5]
    def item_title(self,item):
        return item.title
    def item_description(self,item):
        return markdown(item.content,['codehilite'])

    def item_link(self,item):
        return "127.0.0.1:8000/post/"+str(item.id)+"/"
