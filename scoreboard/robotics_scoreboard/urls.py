from django.conf.urls import patterns, url
from robotics_scoreboard import views

urlpatterns = patterns('',
	url(r'round1', views.round1, name='Round1'),
	url(r'round2', views.round2, name='Round2'),
	url(r'round3', views.round3, name='Round3'),
	url(r'final', views.final, name='Final'),
	url(r'fastRatsData', views.getFastRatsJson, name='getFastRatsTable'),
	url(r'teamData', views.getTeamData, name='getTeamData'),
	url(r'smartRatsData', views.getSmartRatsJson, name='getSmartRatsTable')
	)