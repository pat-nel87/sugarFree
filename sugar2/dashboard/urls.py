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
    path('/gluco_entry', views.gluco_entry, name="gluco_entry"),
    path('/insulin_entry', views.insulin_entry, name="macro_entry"),
    path('/macro_entry', views.macro_entry, name="macro_entry"),
    path('/listview', views.listview, name="listview"),
    path('/graph_test', views.graphTest, name = "graphTest"),
    ]