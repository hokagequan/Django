from django.db import models

# Create your models here.
class AppFile(object):
	def __init__(self, name, url):
	    self.name = name
	    self.url = url