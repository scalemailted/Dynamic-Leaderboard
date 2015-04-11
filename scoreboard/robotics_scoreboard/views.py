from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from robotics_scoreboard.models import FastRatsTableEntry, Team, Score
from django.db import connection

# Create your views here.
def scoreboard(request):

	#Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	#context_dict = {'boldmessage' : "This is text defined in the view method."}

	# Return a rendered response to send to the client
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	
	#return render(request, 'robotics_scoreboard/index.html', context_dict)
	return render( request, 'robotics_scoreboard/leaderboard.html')

def getFastRatsJson(request):
	#Get all of the records from the database
	# add cast the collection into a list
	fastRats = list(FastRatsTableEntry.objects.all().values())
	#context_dict = {'fastRats': fastRats }
	return JsonResponse(data=fastRats, safe=False)

def getSmartRatsJson(request):
	#Get all of the records from the database
	# add cast the collection into a list
	smartRats = list(FastRatsTableEntry.objects.filter(rat_type='S').values())
	#context_dict = {'fastRats': fastRats }
	return JsonResponse(data=smartRats, safe=False)

def getTeamData(request):
	teamData = list(createTeamScoreDict())
	return JsonResponse(data=teamData, safe=False)

#helper methods

def createTeamScoreDict( ):
    #create cursor that will perform the query
    cursor = connection.cursor()
    
    #define the raw sql query that will create the composite entry data
    # that will be serialized as JSON for the view
    query = ('SELECT '
    'robotics_scoreboard_team.Team AS team,'
    'robotics_scoreboard_team.TeamNumber AS team_number,'
    'robotics_scoreboard_team.Type AS rat_type,'
    'robotics_scoreboard_team.TotalScore AS total_score, '
    'robotics_scoreboard_team.InFinal AS in_final,'
    'robotics_scoreboard_team.Disqualified AS disqualified, '
    'robotics_scoreboard_score.SearchPath AS search_path,'
    'robotics_scoreboard_score.SearchTime AS search_time,'
    'robotics_scoreboard_score.CriticalPath AS critical_path,'
    'robotics_scoreboard_score.CriticalTime AS critical_time,'
    'robotics_scoreboard_score.EasterEgg AS easter_egg,'
    'robotics_scoreboard_score.Penalty AS penalty,'
    'robotics_scoreboard_score.RoundScore AS round_score,' 
    'robotics_scoreboard_score.id '
    'FROM robotics_scoreboard_score '
    'JOIN robotics_scoreboard_team '
    'ON robotics_scoreboard_team.id=robotics_scoreboard_score.team_id'
    )
    #execute query to populate the cursor's description collection
    cursor.execute(query)

    #get a tuple of the field/column names
    desc = cursor.description
    #print(desc)

    #construct and return a dictionary with the alias names as the keys and the field values
    return [dict(zip([col[0] for col in desc ], row ))
    for row in cursor.fetchall()
    ]
