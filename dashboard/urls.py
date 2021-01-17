# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:16:35 2021

@author: Patrick
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.dashview, name="dashview"),
    ]