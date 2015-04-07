from django.db import models
from datetime import timedelta

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class FastRatsTableEntry(models.Model):
	RAT_TYPE_CHOICES = [ 
	('F', 'Fast Rat'),
	('S', 'Smart Rat')
	]
	team = models.CharField(max_length=10, unique=True, db_column='Team')
	search_path = models.IntegerField(default=0,db_column='Search Path')
	search_time = models.CharField(max_length=10,default='0', db_column='Search Time')
	critical_path = models.IntegerField(default=0, db_column='Critical Path')
	critical_time = models.CharField(max_length=10, default='0', db_column='Critical Time')
	easter_egg = models.IntegerField(default=0, db_column='Easter Egg')
	penalty = models.IntegerField(default=0, db_column='Penalty')
	round_score = models.IntegerField(default=0, db_column='Round')
	total_score = models.IntegerField(default=0, db_column='Total')
	rat_type = models.CharField(max_length=12, db_column='Type', choices=RAT_TYPE_CHOICES, default='F')

	def __unicode__(self):
		return self.team
'''
class SmartRatsTableEntry(models.Model):
	team = models.CharField(max_length=10, unique=True, db_column='Team')
	search_path = models.IntegerField(default=0, db_column='Search Path')
	search_time = models.DurartionField(default=timedelta(), db_column='Search Time')
	critical = models.IntegerField(default=0)
	time = models.IntegerField(default=0)
	penalty = models.IntegerField(default=0)
	total = models.IntegerField(default=0)

	def __unicode__(self):
		return self.team
'''