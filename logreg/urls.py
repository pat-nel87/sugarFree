# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:03:20 2021

@author: Patrick
"""

from django.urls import path, include
from . import views


urlpatterns = [    
     path('', views.index, name= 'index'),
     path('register', views.register, name = 'register'),
     path('log_on', views.log_on, name ='log_on'),
     path('dashview', include("dashboard.urls"), name='dashview')
     ]