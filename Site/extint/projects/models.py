from django.db import models

from django.contrib.auth.models import User

class Projects(models.Model):
	owner = models.ForeignKey(User)
	
	text = models.TextField()
	image = models.ImageField()
	date_of_publication = models.DataField(auto_now_add=True)
	end_of_funding = models.DataField()
	goal = models.IntegerField()
	current_state = models.IntegerField()
	investors = models.ManyToManyFields(User)