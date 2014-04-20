from django.conf.urls import patterns, url

from members import views


urlpatterns = patterns('',
	url(r'^register', views.register, name='register'),
)