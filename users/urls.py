"""URL patterns for app: users"""

from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
   url(r'^login/$', LoginView.as_view(), {'template_name': 'users/login.html'}, name='login'),   # login page
   url(r'^logout/$', views.logout_view, name='logout'),
]
