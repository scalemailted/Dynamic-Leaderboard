import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard.settings')

import django
django.setup()

from robotics_scoreboard.models import Team, Score

teams = Team.objects.all()

#For each team entry
for team in teams:
	team.Scores.create(
		round = '3'
		)
#create a score entry with its round set to 3
#associate the score with the team