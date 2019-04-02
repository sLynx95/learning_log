"""URL patterns for app: users"""

from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views

# from . import views

urlpatterns = [
   url(r'^login/$', views.LoginView.as_view(), {'template_name': 'users/login.html'}, name='login'),   # login page
]
