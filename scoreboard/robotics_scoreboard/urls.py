from django.conf.urls import patterns, url
from robotics_scoreboard import views

urlpatterns = patterns('',
	url(r'^$', views.scoreboard, name='scoreboard'),
	url(r'fastRatsData', views.getFastRatsJson, name='getFastRatsTable'),
	url(r'smartRatsData', views.getSmartRatsJson, name='getSmartRatsTable'))
