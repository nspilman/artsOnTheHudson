import csv
import os, shutil
from django.contrib.auth.models import User
from .models import Timelog
import datetime

def readcsv(file):
    newfile = open(file)
    readfile = csv.reader(newfile)
    datafile = list(readfile)
    return datafile

def write(list,filename):
    outputFile = open(str(filename)+".csv",'w',newline='')
    outputWriter = csv.writer(outputFile)
    for line in list:
        row = []
        if type(line) == str:
            outputWriter.writerow([line])
        else:
            for i in line:
                row.append(i)        
            outputWriter.writerow(row)

def timeload(file):
    rejects = []
    csv_to_list = readcsv(file)
    for line in csv_to_list:
        timelog = Timelog()
        try:
            firstname, lastname = line[0].split(' ')
            if firstname.lower() != 'alex':
                timelog.person = User.objects.get(first_name = firstname)
            else:
                timelog.person = User.objects.get(first_name = firstname, last_name = lastname)
        except:
            continue
        timelog.logdate = datetime.date.today()
        timelog.minutes = line[5]
        timelog.description =line[1] 
        workday_date = line[2]
        try:
            for_str = '%m/%dd/%Y'
            timelog.work_day = datetime.datetime.strptime(workday_date, for_str)
        except:
            for_str = '%m/%d/%Y'
            timelog.work_day = datetime.datetime.strptime(workday_date, for_str)
        timelog.save()





