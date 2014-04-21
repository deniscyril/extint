from django.conf.urls import patterns, url

from members import views


urlpatterns = patterns('',
	url(r'^register', views.register_view, name='register'),
	url(r'^login', views.login_view, name='login'),
)