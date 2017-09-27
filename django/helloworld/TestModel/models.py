from django.db import models
class Test(models.Model):
	name = models.CharField(max_length=20)

class Contact(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField(default=0)
	email = models.EmailField()
	id = models.IntegerField(max_length=20,primary_key=True)
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	id = models.IntegerField(max_length=20,primary_key=True)
	def __unicode__(self):
		return self.name
