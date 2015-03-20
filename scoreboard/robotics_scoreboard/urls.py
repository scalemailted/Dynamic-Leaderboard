from django.conf.urls import patterns, url
from robotics_scoreboard import views

urlpatterns = patterns('',
	url(r'^$', views.testpage, name='testpage'))
