from django.db import models
from django.conf import settings
from django.utils import timezone


class Post (models.Model):
	author= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='posts')
	title = models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def snipped(self):
		return self.body[0:50]+"..." 	



# Post (models.Model)-so Django will know that we should save in db

# charfie-limited Text-not limited
# models.ForeignKey – this is a link to another model.1

# ForeignKey-many to one relationship, settings.AUTH_USER_MODEL can have several post 

# on_delete=models.CASCADE is an SQL standard.
# CASCADE: When the referenced object is deleted, 
# also delete the objects that have references to it (When you remove 
# a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
