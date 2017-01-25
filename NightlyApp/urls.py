from django.conf.urls import url
from NightlyApp import views

urlpatterns = [
    url(r'^$', views.view_index, name='index')
]
