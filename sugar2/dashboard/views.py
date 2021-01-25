from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Glucose, Insulin
import matplotlib
import matplotlib.pyplot as plt 
from io import StringIO
import numpy as np


def dashview(request):
    user = request.user
    if user.user_reading is not None:
        context = {  
        'graph': return_graph(user), }
        return render(request, "dashgraphed.html", context)
    else:
    
        return render(request, "dash.html")

def insulin_entry(request):
    user = request.user
    dose = request.POST['dose']
    time = request.POST['time']
    new_insulin = Insulin.objects.create(dose=dose, time=time, uploaded_by=user)
    new_insulin.save()
    print(f"{new_insulin}")
    return redirect('dashview')


def gluco_entry(request):
    user = request.user
    reading = request.POST['reading']
    time = request.POST['time']
    new_entry = Glucose.objects.create(reading=reading,time=time,uploaded_by=user)
    new_entry.save()
    print(f"{reading} {time}")
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
    matplotlib.pyplot.plot_date(x, y, 'r')
    matplotlib.pyplot.plot_date(b, val3, 'b')
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
        'graph': return_graph(user), }
    
    return render(request, "graphtest.html", context)
    
    
    
    