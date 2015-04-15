from django.conf.urls import patterns, url
from robotics_scoreboard import views

urlpatterns = patterns('',
	url(r'round1', views.round1, name='Round1'),
	url(r'round2', views.round2, name='Round2'),
	url(r'round3', views.round3, name='Round3'),
	url(r'final', views.final, name='Final'),
	url(r'fastRatsRound1', views.fastRatsRound1, name='getFastRatsTable'),
	url(r'teamData', views.getTeamData, name='getTeamData'),
	url(r'smartRatsRound1', views.smartRatsRound1, name='getSmartRatsTable'),
	url(r'fastRatsRound2', views.fastRatsRound2, name='getFastRatsRound2'),
	url(r'fastRatsRound3', views.fastRatsRound3, name='getFastRatsRound3'),
	url(r'smartRatsRound2', views.smartRatsRound2, name='getSmartRatsRound2'),
	url(r'smartRatsRound3', views.smartRatsRound3, name='getSmartRatsRound3')
	)