import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard.settings')

import django
django.setup()

from robotics_scoreboard.models import Team, Score


teams = Team.objects.all()

#For each team entry
for team in teams:
	if(team.in_final is True):
		scores  = team.Scores.filter(round='F')
		if(scores.count() < 1):
		    team.Scores.create(
		        round = 'F'
		    )