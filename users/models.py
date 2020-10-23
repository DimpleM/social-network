from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	following = models.ManyToManyField(User, related_name='following', blank=True)
	bio = models.TextField(default='no field')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def profile_posts(self):
		return self.post_set.all()

	def __str__(self):
		return str(self.user.username)

	class Meta:
		ordering = ('-created',)