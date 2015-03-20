from django.db import models

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
	team = models.CharField(max_length=10, unique=True)
	search = models.IntegerField(default=0)
	critical = models.IntegerField(default=0)
	time = models.IntegerField(default=0)
	penalty = models.IntegerField(default=0)
	total = models.IntegerField(default=0)

	def __unicode__(self):
		return self.team

class SmartRatsTableEntry(models.Model):
	team = models.CharField(max_length=10, unique=True)
	search = models.IntegerField(default=0)
	critical = models.IntegerField(default=0)
	time = models.IntegerField(default=0)
	easter_egg = models.IntegerField(default=0)
	penalty = models.IntegerField(default=0)
	total = models.IntegerField(default=0)

	def __unicode__(self):
		return self.team