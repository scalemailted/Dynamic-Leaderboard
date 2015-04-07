from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from robotics_scoreboard.models import FastRatsTableEntry
#, SmartRatsTableEntry

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
