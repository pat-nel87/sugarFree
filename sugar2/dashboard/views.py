from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Glucose, Insulin, Macro

import itertools
import matplotlib
import matplotlib.pyplot as plt
from io import StringIO

import json
#import numpy as np


def dashview(request):
    user = request.user
    if user.user_reading is not None:
        context = {  
        'graph': return_graph(user),
        'piegraph': pieGraph(user)
        }
        return render(request, "expdash.html", context)
    else:
    
        return render(request, "dash.html")

def listview(request):
    user = request.user
    user_reading = user.user_reading.all()
    user_dose = user.user_dose.all()    
    user_macro = user.user_macro.all()
    context = {
        'user_reading': user_reading,
        'user_dose': user_dose,
        'user_macro': user_macro
        }
    return render(request, "list.html", context)
    
    
    
def insulin_entry(request):
    user = request.user
    dose = request.POST['dose']
    time = request.POST['time']
    new_insulin = Insulin.objects.create(dose=dose, time=time, uploaded_by=user)
    new_insulin.save()
    print(f"{new_insulin}")
    return redirect('dashview')

def macro_entry(request):
    user = request.user
    fat = request.POST['fat']
    carb = request.POST['carb']
    protein = request.POST['protein']
    time = request.POST['time']
    calories = 0#calCalc(fat, carb, protein)
    new_meal = Macro.objects.create(fat=fat, carb=carb, protein=protein, time=time, calories=calories, uploaded_by=user)
    new_meal.save()
    print(f"{new_meal}")
    return redirect('dashview')

def calCalc(fat,carb,protein):
    totCal = (fat*9) + (carb*4) + (protein*4)
    return totCal


def gluco_entry(request):
    user = request.user
    reading = request.POST['reading']
    time = request.POST['time']
    new_entry = Glucose.objects.create(reading=reading,time=time,uploaded_by=user)
    new_entry.save()
    print(f"{reading} {time}")
    jsonEntry = json.dumps([reading , time])
    print(jsonEntry)
    #return HttpResponse(f"{new_entry} {new_entry.uploaded_by}")
    return redirect('dashview')
       
def return_graph(user):
    user = user 
    val1 = list(user.user_reading.values_list('reading').order_by('time'))
    val2 = list(user.user_reading.values_list('time').order_by('time'))
    val3 = list(user.user_dose.values_list('dose').order_by('time'))
    val4 = list(user.user_dose.values_list('time').order_by('time'))
    print(val3)
    print(val4)
    y = val1
    x = matplotlib.dates.date2num(val2)
    b = matplotlib.dates.date2num(val4)
    fig = matplotlib.pyplot.figure()
    matplotlib.pyplot.plot_date(x, y, 'r', label='blood sugar')
    #matplotlib.pyplot.bar(val3,height=val3, width=0.8)
    matplotlib.pyplot.plot_date(b, val3)
    matplotlib.pyplot.title("Blood Glucose Levels")
    #plt.plot(x,y)
    
    # converts graph to svg image!
    # stringIO module
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def graphTest(request):
    user = request.user
    context = {  
        'graph': pieGraph(user), }
    
    return render(request, "graphtest.html", context)

def pieTotal(val1, val2, val3):
    val1 = list(itertools.chain(*val1))
    val2 = list(itertools.chain(*val2))
    val3 = list(itertools.chain(*val3))
    
    totfat = 0
    totcarb = 0
    totprot = 0
    
    for x in range(len(val1)):
        totfat = totfat + val1[x]
       
    for x in range(len(val2)):
        totcarb = totcarb + val2[x]
    
    for x in range(len(val3)):
        totprot = totprot + val3[x]
    pieVal = [totfat, totcarb, totprot]
    return pieVal



def pieGraph(user):
    user = user
    val1 = list(user.user_macro.values_list('fat').order_by('time'))
    val2 = list(user.user_macro.values_list('carb').order_by('time'))
    val3 = list(user.user_macro.values_list('protein').order_by('time'))
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Fats', 'Carbs', 'Proteins'
    sizes = pieTotal(val1, val2, val3)
    #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #plt.show()
    imgdata = StringIO()
    fig1.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
    
    
    