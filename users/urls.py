from django.urls import path
from . import views

urlpatterns = [
    path('profile_follow/', views.ProfileListView.as_view(), name='profile-list-view'),
    path('profile_follow/follow/<str:user>/',views.follow, name='follow'),
    path('profile_follow/unfollow/<str:user>/',views.unfollow, name='unfollow')

]
