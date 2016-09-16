from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	visited = models.BooleanField(default=0)
	thumbs_down_by_users = models.ManyToManyField(User)
	def __str__(self):
		return self.name

class Review(models.Model):
	text = models.TextField()
	date = models.DateTimeField('date posted')
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.text

class ReviewComment(models.Model):
	text = models.TextField()
	date = models.DateTimeField('date posted')
	parent_review = models.ForeignKey(Review, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.text
