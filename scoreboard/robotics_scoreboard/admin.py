from django.contrib import admin
from robotics_scoreboard.models import  FastRatsTableEntry, Team, Score
#,SmartRatsTableEntry

# Register your models here.
#admin.site.register( Category )
#admin.site.register( Page )
admin.site.register( FastRatsTableEntry )
admin.site.register( Team )
admin.site.register( Score )
#admin.site.register( SmartRatsTableEntry )