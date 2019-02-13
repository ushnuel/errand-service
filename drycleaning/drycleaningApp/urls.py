from django.conf.urls import url
from drycleaningApp import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
    url(r'^message$', views.my_messages, name='my_messages'),
]
