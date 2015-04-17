from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from robotics_scoreboard.models import Team, Score
from django.db import connection

# Create your views here.
def round1(request):

	#Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	#context_dict = {'boldmessage' : "This is text defined in the view method."}

	# Return a rendered response to send to the client
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	
	#return render(request, 'robotics_scoreboard/index.html', context_dict)
	return render( request, 'robotics_scoreboard/leaderboardQ1.html')

def round2(request):

    #Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage' : "This is text defined in the view method."}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    
    #return render(request, 'robotics_scoreboard/index.html', context_dict)
    return render( request, 'robotics_scoreboard/leaderboardQ2.html')

def round3(request):

    #Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage' : "This is text defined in the view method."}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    
    #return render(request, 'robotics_scoreboard/index.html', context_dict)
    return render( request, 'robotics_scoreboard/leaderboardQ3.html')

def final(request):
    #Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage' : "This is text defined in the view method."}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    
    #return render(request, 'robotics_scoreboard/index.html', context_dict)
    return render( request, 'robotics_scoreboard/leaderboardF.html')

def fastRatsRound1(request):
	#Get all of the records from the database
    # add cast the collection into a list
    round_number = 1
    fastRats = list(createFastRatsDict(round_number))
	#context_dict = {'fastRats': fastRats }    
    return JsonResponse(data=fastRats, safe=False)

def fastRatsRound2(request):
    #Get all of the records from the database
    # add cast the collection into a list
    round_number = 2
    fastRats = list(createFastRatsDict(round_number))
    #context_dict = {'fastRats': fastRats }
    return JsonResponse(data=fastRats, safe=False)

def fastRatsRound3(request):
    #Get all of the records from the database
    # add cast the collection into a list
    round_number = 3
    fastRats = list(createFastRatsDict(round_number))
    #context_dict = {'fastRats': fastRats }
    return JsonResponse(data=fastRats, safe=False)

def smartRatsRound1(request):
	#Get all of the records from the database
	# add cast the collection into a list
    round_number = 1
    smartRats = list(createSmartRatsDict(round_number))
	#context_dict = {'fastRats': fastRats }
    return JsonResponse(data=smartRats, safe=False)

def smartRatsRound2(request):
    #Get all of the records from the database
    # add cast the collection into a list
    round_number = 2
    smartRats = list(createSmartRatsDict(round_number))
    #context_dict = {'fastRats': fastRats }
    return JsonResponse(data=smartRats, safe=False)

def smartRatsRound3(request):
    #Get all of the records from the database
    # add cast the collection into a list
    round_number = 3
    smartRats = list(createSmartRatsDict(round_number))
    #context_dict = {'fastRats': fastRats }
    return JsonResponse(data=smartRats, safe=False)

def getTeamData(request):
	teamData = list(createTeamScoreDict())
	return JsonResponse(data=teamData, safe=False)

#helper methods
def createSmartRatsDict( roundNum=1):
    #create cursor that will perform the query
    cursor = connection.cursor()
    
    roundVal = str(roundNum)
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
    's.Round AS round_number,'
    's.RoundScore AS round_score,' 
    's.id '
    'FROM robotics_scoreboard_score AS s '
    'JOIN robotics_scoreboard_team AS t '
    'ON t.id=s.team_id '
    'WHERE rat_type = "S" '
    'AND round_number = ' + roundVal
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

def createFastRatsDict( roundNum=1):
    #create cursor that will perform the query
    cursor = connection.cursor()

    roundVal = str(roundNum)
    
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
    's.Round AS round_number,'
    's.id '
    'FROM robotics_scoreboard_score AS s '
    'JOIN robotics_scoreboard_team AS t '
    'ON t.id=s.team_id '
    'WHERE rat_type = "F"'
    #'AND round_number = '
    )

    query = query + ' AND round_number = ' + roundVal
    #execute query to populate the cursor's description collection
    cursor.execute(query )

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
    't.Disqualified AS disqualified, '
    's.SearchPath AS search_path,'
    's.SearchTime AS search_time,'
    's.CriticalPath AS critical_path,'
    's.CriticalTime AS critical_time,'
    's.EasterEgg AS easter_egg,'
    's.Penalty AS penalty,'
    's.Round AS round_number, '
    's.RoundScore AS round_score,'
    's.BTB AS btb_percentage,' 
    's.id '
    'FROM robotics_scoreboard_score AS s '
    'JOIN robotics_scoreboard_team AS t '
    'ON t.id=s.team_id AND round_number="F"'
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
