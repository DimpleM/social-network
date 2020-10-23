from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile

class Post(models.Model):
	title  = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='', blank=True)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.title