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
from django.forms.models import model_to_dict
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
class website_object(APIView):  
    def get(self,request, app,id = ''):
        db_object = apps.get_model('website',app)
        if id:
            output = db_object.objects.get(id=id).name
        else:
            output = db_object.objects.all()
            
            output = [json.dumps(model_to_dict(object,fields=['name','blurb','date']), cls=DjangoJSONEncoder)for object in output]
            # for item in output:
            #     output['date'] = str(output['date'])
        return Response(output)
