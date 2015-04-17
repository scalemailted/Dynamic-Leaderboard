import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard.settings')

import django
django.setup()

from robotics_scoreboard.models import Team, Score


teams = Team.objects.all()

for team in teams:
		scores  = team.Scores.filter(round='')
		if(scores.count() < 1):
		    team.Scores.create(
		        round = ''
		    )