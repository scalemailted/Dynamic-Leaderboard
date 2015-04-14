from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from robotics_scoreboard.models import Team, Score
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
	fastRats = list(createFastRatsDict())
	#context_dict = {'fastRats': fastRats }
	return JsonResponse(data=fastRats, safe=False)

def getSmartRatsJson(request):
	#Get all of the records from the database
	# add cast the collection into a list
	smartRats = list(createSmartRatsDict())
	#context_dict = {'fastRats': fastRats }
	return JsonResponse(data=smartRats, safe=False)

def getTeamData(request):
	teamData = list(createTeamScoreDict())
	return JsonResponse(data=teamData, safe=False)

#helper methods
def createSmartRatsDict( ):
    #create cursor that will perform the query
    cursor = connection.cursor()
    
    #define the raw sql query that will create the composite entry data
    # that will be serialized as JSON for the view
    query = ('SELECT '
    't.Team AS team,'
    't.TeamNumber AS team_number,'
    't.Type AS rat_type,'
    't.TotalScore AS total_score, '
    't.InFinal AS in_final,'
    't.Disqualified AS disqualified, '
    's.SearchPath AS search_path,'
    's.SearchTime AS search_time,'
    's.CriticalPath AS critical_path,'
    's.CriticalTime AS critical_time,'
    's.EasterEgg AS easter_egg,'
    's.Penalty AS penalty,'
    's.RoundScore AS round_score,' 
    's.id '
    'FROM robotics_scoreboard_score AS s '
    'JOIN robotics_scoreboard_team AS t '
    'ON t.id=s.team_id '
    'WHERE rat_type = "S"'
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

def createFastRatsDict( ):
    #create cursor that will perform the query
    cursor = connection.cursor()
    
    #define the raw sql query that will create the composite entry data
    # that will be serialized as JSON for the view
    query = ('SELECT '
    't.Team AS team,'
    't.TeamNumber AS team_number,'
    't.Type AS rat_type,'
    't.TotalScore AS total_score, '
    't.InFinal AS in_final,'
    't.Disqualified AS disqualified, '
    's.SearchPath AS search_path,'
    's.SearchTime AS search_time,'
    's.CriticalPath AS critical_path,'
    's.CriticalTime AS critical_time,'
    's.EasterEgg AS easter_egg,'
    's.Penalty AS penalty,'
    's.RoundScore AS round_score,' 
    's.id '
    'FROM robotics_scoreboard_score AS s '
    'JOIN robotics_scoreboard_team AS t '
    'ON t.id=s.team_id '
    'WHERE rat_type = "F"'
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

def createTeamScoreDict( ):
    #create cursor that will perform the query
    cursor = connection.cursor()
    
    #define the raw sql query that will create the composite entry data
    # that will be serialized as JSON for the view
    query = ('SELECT '
    't.Team AS team,'
    't.TeamNumber AS team_number,'
    't.Type AS rat_type,'
    't.TotalScore AS total_score, '
    't.InFinal AS in_final,'
    't.Disqualified AS disqualified, '
    's.SearchPath AS search_path,'
    's.SearchTime AS search_time,'
    's.CriticalPath AS critical_path,'
    's.CriticalTime AS critical_time,'
    's.EasterEgg AS easter_egg,'
    's.Penalty AS penalty,'
    's.RoundScore AS round_score,' 
    's.id '
    'FROM robotics_scoreboard_score AS s '
    'JOIN robotics_scoreboard_team AS t '
    'ON t.id=s.team_id'
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
