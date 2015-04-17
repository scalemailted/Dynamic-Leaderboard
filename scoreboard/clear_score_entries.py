import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard.settings')

import django
django.setup()

from robotics_scoreboard.models import Team, Score

def main():
	#Get queryset that will return all score entries
	scores = Score.objects.all()

	print ("Clearing {} scores".format(scores.count()))
		
	for score in scores:
		zeroOutScore(score)

	teams = Team.objects.all()

	print ("Clearing {} Team entries".format(teams.count()))

	for team in teams:
		clearTeamStatus(team)

def clearTeamStatus(team):
    team.in_final=False
    team.disqualified=False
    team.total_score=0
    team.perfect_score_payout=False
    team.save()
    return team

def zeroOutScore( score ):
	score.search_path = 0
	score.search_time = 0.00
	score.critical_path = 0
	score.critical_time = 0.00
	score.easter_egg = 0
	score.critical_penalty = 0
	score.search_penalty = 0
	score.round_score = 0
	score.btb_percentage = 0
	score.save()
	return score

if __name__ == '__main__':
	main()