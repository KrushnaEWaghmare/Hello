
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.myindex, name='myindex'),
    path('about/', views.myabout, name='myabout'),
    path('contact/', views.mycontact, name='mycontact'),
    path('features/', views.myfeatures, name='myfeatures'),
    path('projects/', views.myprojects, name='myprojects'),
]
