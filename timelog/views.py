from django.shortcuts import render
from .models import Timelog
from django.contrib.auth.models import User
import timelog.legacy_timeloader as timelog
import os
from rest_framework.response import Response
from django.db.models import Avg, Count, Sum
from django.contrib.auth.decorators import login_required


def load_time(request):
    directory = os.fsencode('timelog/timeload/')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            timelog.timeload('timelog/timeload/' + filename)
        else:
            continue
    return render(request,'classes/classpage.html')
    
@login_required()
def reporting_home(request):
    users_time = []
    users = User.objects.all()
    timelogs = Timelog.objects.all()
    all_time = Timelog.objects.all().aggregate(Sum('minutes'))['minutes__sum']

    for user in users:
        usertime = Timelog.objects.filter(person = user).aggregate(Sum('minutes'))['minutes__sum']
        user_time= []
        user_time.append(user.first_name + ' ' + user.last_name) 
        user_time.append(usertime)
        users_time.append(user_time)
    return render(request,'timelog/timereport.html', {'users_time':users_time})
    
# # def reporting_timelog(request):



# Create your views here.
