""""URL addresses for learning_logs """

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # main page
    url(r'^topics/$', views.topics, name='topics'),  # topics page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),  # detailed page of topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),    # create topic by user page
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),    # Create entry by user page
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
