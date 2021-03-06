from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'work0909.views.home', name='home'),
    # url(r'^work0909/', include('work0909.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','future.views.index'),
    url(r'^index/$','future.views.index'),
    url(r'^regist','future.views.regist'),
    url(r'^login/$','future.views.login_view'),
    url(r'^logout/$','future.views.logout_view'),
    url(r'^account/$','future.views.account'),
    url(r'^letter/$','future.views.letter'),
    url(r'^edit/$','future.views.edit'),
    url(r'^change/$','future.views.change_view'),
    url(r'^delete/$','future.views.delete_view'),
    url(r'^showletter/$','future.views.showletter'),
    url(r'^edit_letter/$','future.views.edit_letter'),
    url(r'^del_letter/$','future.views.del_letter'),
    url(r'^search/$','future.views.search_view'),
    url(r'^help/$','future.views.help'),
    url(r'^aboutus/$','future.views.aboutus'),
#    url(r'^model/$','future.views.model'),
)
