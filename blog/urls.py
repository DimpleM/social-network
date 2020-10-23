from django.urls import path
from blog.views import *

urlpatterns = [
    path('', home, name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
   
]
