from django.conf.urls import patterns, include, url

from django.contrib import admin
from members import urls
from projects import urls, views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'extint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^members/', include("members.urls")),
    url(r'^projects/', include("projects.urls")),
    url(r'^$', views.home, name='home'),
)
