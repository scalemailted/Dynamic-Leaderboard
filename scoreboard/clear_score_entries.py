import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard.settings')

import django
django.setup()

from robotics_scoreboard.models import Team, Score

#Get queryset that will return all score entries
scores = Score.objects.all()

for score in scores:
	zeroOutScore(score)


def zeroOutScore( score ):
	score.search_path = 0
	score.search_time = 0.00
	score.critical_path = 0
	score.critical_time = 0.00
	score.easter_egg = 0
	score.penalty = 0
	score.round_score = 0
	score.save()
	return score