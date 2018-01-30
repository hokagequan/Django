from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
	"""docstring for Board"""
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)

class Topic(models.Model):
	"""docstring for Topic"""
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board, related_name='topics', on_delete=True)
	starter = models.ForeignKey(User, related_name='topics', on_delete=False)

class Post(models.Model):
	"""docstring for Post"""
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, related_name='posts', on_delete=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts', on_delete=False)
	updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=False)
