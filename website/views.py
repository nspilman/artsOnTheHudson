from django.shortcuts import render, redirect, get_object_or_404
from .models import Education, Events, Staff, Media, Contacts, Incomingmessages, Bulletin, Event_signup, Press
from people.models import Person
from django.core.mail import send_mail
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.sitemaps import Sitemap
import datetime
import markdown
from django.conf import settings
from django.http import Http404

from django.urls import reverse
from django.shortcuts import render
# from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    title = 'Arts Nonprofit | Jersey City | Arts on the Hudson'
    try:
        post = Bulletin.objects.all().last()
    except:
        post = ''
    if request.method == 'POST':
        if request.method == 'POST' and request.POST['_replyto']:
            submission = request.POST['_replyto'].lower()
            try:
                exists = Contacts.objects.get(email = submission)
                form_message = 'The email address you submitted is already on our mailing list'
                return render(request,'website/index.html', {'title':title, 'form_message':form_message, 'post':post}) 
            except: 
                form_message = 'Thanks for signing up!'
                send_mail('Welcome to the Arts on the Hudson mailing list', 'Thank you so much for signing up for our Mailing List!', 'The Arts on the Hudson team',
                           [submission], fail_silently=True)
                Contacts.objects.create(email = submission)
                return render(request,'website/index.html', {'title':title, 'form_message':form_message, 'post':post})  
    else:    
        return render(request,'website/index.html', {'title':title, 'post':post})

def staff(request):
    staff = Staff.objects.all()
    cssclass = 'astaff'
    title = 'Staff | Jersey City | Arts on the Hudson'
    variables = {'staff':staff, 'title':title, 'cssclass':cssclass}
    return render(request,'website/staff.html',variables)

def mission(request):
    return render(request,'website/mission.html')

def press(request):
    press = Press.objects.all()
    cssclass = 'apress'
    title = 'Press | Jersey City | Arts on the Hudson'
    variables = {'press':press, 'title':title, 'cssclass':cssclass}
    return render(request,'website/press.html',variables)

def events(request, events):
    upcoming = Events.objects.order_by('date').filter(date__gte=datetime.date.today())
    cssclass = 'aevents'
    past = Events.objects.order_by('-date').filter(date__lt=datetime.date.today())
    if events in ['events','pastevents']:
        if events == 'events':
            title = 'Events | Jersey City | Arts on the Hudson'
        else:
            title = 'Past Events | Jersey City | Arts on the Hudson'
        variables = {'upcoming':upcoming, 'past':past, 
                        'events':events, 'cssclass':cssclass, 'title':title}
        return render(request,'website/events.html', variables)
    else:
        raise Http404

def eventpage(request, eventurl):
    event = Events.objects.get(url__iexact = eventurl)
    if event.date < datetime.date.today():
        event.past = True
    else:
        event.past = False
    
    event.save()
    title = event.name  +' |Events | Arts on the Hudson'
    cssclass = 'aevents'
    event_signup = Event_signup.objects.filter(parent_event = event)
    if event_signup == []:
        variables = {'event':event, 'title':title, 'cssclass':cssclass}
    else:
        variables = {'event':event, 'title':title, 'cssclass':cssclass, 'event_signup':event_signup}

    return render(request,'website/eventpage.html', variables)
    
def education(request):
    return redirect('/education/Headstart/')

def program(request,programurl):
    program = Education.objects.get(url = programurl)
    cssclass = 'aeducation'
    title = program.name + ' | Education | Arts on the Hudson'
    variables = {'title':title, 'cssclass':cssclass, 'program':program}
    return render(request,'website/program.html', variables)

def media(request):
    cssclass = 'amedia'
    title = 'Promotional Media | Jersey City | Arts on the Hudson'
    videos = Media.objects.all()
    variables = {'title':title, 'cssclass':cssclass, 'videos':videos}
    return render(request,'website/media.html', variables)

def video(request,videourl):
    cssclass = 'amedia'
    title = 'Promotional Media | Jersey City | Arts on the Hudson'
    video= Media.objects.get(url=videourl)
    variables = {'title':title, 'cssclass':cssclass, 'promo':video}
    return render(request,'website/video.html', variables)

def contact(request):
    cssclass = 'acontact'
    title = 'Contact | Jersey City | Arts on the Hudson'
    variables = {'title':title, 'cssclass':cssclass,}
    return render(request,'website/contact.html', variables)

def give(request):
    cssclass = 'agive'
    title = 'Donate | Jersey City | Arts on the Hudson'
    variables = {'title':title, 'cssclass':cssclass,}
    return render(request,'website/give.html', variables)

def founder(request):
    cssclass = 'agive'
    storyfile = 'AOTHsite/static/website/md/founder.md'
    story = open(storyfile,  mode="r", encoding="utf-8").read()  
    html = markdown.markdown(story)  
    title = 'Grigory Gurevich | Jersey City | Arts on the Hudson'
    variables = {'title':title, 'cssclass':cssclass,'story':html}
    return render(request,'website/founder.html', variables)

