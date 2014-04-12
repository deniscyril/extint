from django.db import models

from django.contrib.auth.models import User
# On utilise le système d'authentification inclus avec django
# On stocke dedans le pseudo, le prénom, le nom, l'email, le mot de passe

from projects.models import Projects

class Profile(models.Model):
	user = models.ForeignKey(User)
	
	date_of_birth = models.DateField()
	country = models.CharField(max_length=255)
	phone1 = models.CharField(max_length=255)
	phone2 = models.CharField(max_length=255)
	phone3 = models.CharField(max_length=255)
	
	#Comment stocker les informations les plus sensibles ?
	#Le stockage des informations bancaires viendrons avec l'implémentation d'une communication avec un système bancaire (ex: Paypal)