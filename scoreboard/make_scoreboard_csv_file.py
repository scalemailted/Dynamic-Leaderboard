import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard.settings')

import django
django.setup()

from robotics_scoreboard.models import Team, Score

def main():

	with open("IEEERoundData.csv", "w") as outFile:
		print("Printing column headers")
		#Print column Headers
		outFile.write("Team, Round, Search Path, Search Time, Critical Path, Critical Time, Easter Egg, Search Penalty, Critical Penalty, Round Total, BTB % \n")
		print("Printing Score Record Data")
		#Retreive all score records from Database
		scores = Score.objects.all()
		for score in scores:
			outFile.write( printScoreDetails(score) )


#Given a score object, will return a string containing all of the score's data fields.
def printScoreDetails(score):
	return ( "{}, {}, {}, {}, {}, {}, {}, {} ,{}, {}, {}%\n".format(
																score.team,
																score.round, 
																score.search_path, 
																score.search_time, 
																score.critical_path,
																score.critical_time,
																score.easter_egg,
																score.search_penalty,
																score.critical_penalty,
																score.round_score,
																score.btb_percentage
															)
	)


if __name__ == "__main__":
	main()