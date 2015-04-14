from django.db import models
from datetime import timedelta
from django.db.models import Sum

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

class Team(models.Model):
	RAT_TYPE_CHOICES = [ 
	('F', 'Fast Rat'),
	('S', 'Smart Rat')
	]
	team_name = models.CharField(max_length=10, unique=True, db_column='Team')
	team_number = models.IntegerField(default=0, db_column='TeamNumber')
	rat_type = models.CharField(max_length=12, db_column='Type', choices=RAT_TYPE_CHOICES, default='F')
	in_final = models.BooleanField(default=False, db_column='InFinal')
	disqualified = models.BooleanField(default=False, db_column='Disqualified')
	total_score = models.IntegerField(default=0, db_column='TotalScore')

	def __unicode__(self):
		return self.team_name

	def save(self):
		self.updateTotalScore()
		super(Team, self).save()

	def updateTotalScore(self):
		self.total_score = self.Scores.aggregate(Sum('round_score'))['round_score__sum']


class Score(models.Model):
	ROUND_OPTIONS = [
	('1', 'One'), 
	('2', 'Two'), 
	('3', 'Three'),
	('F', 'Final')
	]

	team = models.ForeignKey(Team, related_name='Scores', related_query_name="score")
	round = models.CharField(max_length=5, db_column="Round", choices=ROUND_OPTIONS, default=1)
	search_path = models.IntegerField(default=0,db_column='SearchPath')
	search_time = models.DecimalField(max_digits=10, decimal_places=1, default=0.0, db_column='SearchTime')
	critical_path = models.IntegerField(default=0, db_column='CriticalPath')
	critical_time = models.DecimalField(max_digits=10, decimal_places=1,default=0.0, db_column='CriticalTime')
	easter_egg = models.IntegerField(default=0, db_column='EasterEgg')
	penalty = models.IntegerField(default=0, db_column='Penalty')
	round_score = models.IntegerField(default=0, db_column='RoundScore', editable=False)

	def __unicode__(self):
		return '{} - Round {}'.format(Team.objects.get(pk=self.team_id).team_name, self.round)

	def save(self, *args, **kwargs):
		self.updateRoundScore()
		self.updateTeamTotal()
		super(Score, self).save(*args, **kwargs)

	def delete(self):
		#self.team.total_score = self.team.total_score - self.round_score
		super(Score, self).delete()
		self.team.save()
	
	def updateTeamTotal(self):
		self.team.total_score = self.team.Scores.aggregate(Sum('round_score'))['round_score__sum']
		self.team.save()

	def updateRoundScore(self):
		self.round_score = self.search_path + self.critical_path + self.penalty
		if(self.team.rat_type is 'S'):
			self.round_score = self.round_score + self.easter_egg


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
	round_score = models.IntegerField(default=0, db_column='Round', editable=False)
	total_score = models.IntegerField(default=0, db_column='Total', editable=False)
	rat_type = models.CharField(max_length=12, db_column='Type', choices=RAT_TYPE_CHOICES, default='F')

	def save(self):
		# update total score to be the sum of search_path, critical_path, easter_egg, and penalty.
		self.round_score = self.search_path + self.critical_path + self.penalty
		if( self.rat_type is 'S'):
			self.round_score = self.round_score + self.easter_egg
		self.total_score = self.round_score
		super(FastRatsTableEntry, self).save()

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