from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def testpage(request):

	#Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage' : "This is text defined in the view method."}

	# Return a rendered response to send to the client
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'robotics_scoreboard/index.html', context_dict)