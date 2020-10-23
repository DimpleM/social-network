from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Profile
# Create your views here.
from django.contrib.auth.models import User


class ProfileListView(ListView):
	model = Profile
	template_name = "users/main.html"
	context_object_name = "profiles"

	def get_queryset(self):
		profiles = Profile.objects.all().exclude(user= self.request.user)
		my_profile = Profile.objects.get(user=self.request.user)
		result = []
	
		for profile in 	profiles:
			if profile.user in  my_profile.following.all():
				result.append({"profile": profile,"follow":True,"url":"unfollow/{}".format(profile.user)})
			else:
				result.append({"profile": profile,"follow":False,"url":"follow/{}".format(profile.user)})
		return result

def follow(request,user):
	profile = User.objects.get(username=user)
	my_profile = Profile.objects.get(user=request.user)
	my_profile.following.add(profile)
	return redirect('profile-list-view')

def unfollow(request,user):
	profile = User.objects.get(username=user)
	my_profile = Profile.objects.get(user=request.user)
	my_profile.following.remove(profile)
	return redirect('profile-list-view')

