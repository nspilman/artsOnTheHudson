from django.shortcuts import render
# from classes.models import Class
from website.models import Events, Education, Media
from django.contrib.auth.decorators import login_required

@login_required()
def dashboard(request):
    cssclass = 'aevents'
    title =   'Dashboard | Jersey City | Arts on the Hudson'
    
    #order_id = request.session.get('order_id')
    return render(request,'dashboard/dashboard.html')


