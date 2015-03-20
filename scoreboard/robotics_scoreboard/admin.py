from django.contrib import admin
from robotics_scoreboard.models import Category, Page, FastRatsTableEntry,SmartRatsTableEntry

# Register your models here.
admin.site.register( Category )
admin.site.register( Page )
admin.site.register( FastRatsTableEntry )
admin.site.register( SmartRatsTableEntry )