from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from rest_framework.response import Response
import json
from rest_framework.views import APIView
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.apps import apps
from website.models import Events, Education, Media, Press

# Create your views here.
class Object(APIView):  
    def get(self,request, app,id = ''):
        db_object = apps.get_model('website',app)
        if id:
            output = db_object.objects.get(id=id).name
        else:
            output = db_object.objects.all()
            output = [object.name for object in output]
        return Response(output)
