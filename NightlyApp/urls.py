from django.conf.urls import url
from NightlyApp import views

urlpatterns = [
    url(r'^index$', views.view_index, name='index'),
    url(r'^input$', views.view_input, name='input')
]
