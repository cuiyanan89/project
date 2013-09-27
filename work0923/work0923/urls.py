from django.conf.urls import patterns, include, url
from blog.feeds import RSSFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'work0923.views.home', name='home'),
    # url(r'^work0923/', include('work0923.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/',include('grappelli.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.index'),
    url(r'^index/$','blog.views.index'),
    url(r'^post/$','blog.views.post'),
    url(r'^node/$','blog.views.node'),
    url(r'^replay/$','blog.views.replay'),
)

urlpatterns += patterns('',
    url('^feeds/$',RSSFeed(),name='blog_feed'),
)
