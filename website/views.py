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
    past = Events.objects.filter(date__lt=datetime.date.today())
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
    
    if request.method == 'POST':
        firstname = request.POST['firstname'] 
        lastname = request.POST['lastname']
        email = request.POST['email'].lower()
        try:
            session = request.POST['session']
        except:
            session = ''

        new_order = Order()
        new_order.name = event.name
        if session == "":
            session_record = event_signup.get(parent_event = event)
            session = session_record.name
        else:
            session_record = event_signup.get(name = session)
        new_order.subname = session
        new_order.price = session_record.price
        last_order = Order.objects.all().order_by('order_id').last()
        if not last_order:
            new_order.order_id = '100000001'
        else:
            last_order_id = last_order.order_id
            last_order_int = int(last_order_id)
            new_order_id = last_order_int + 1
            new_order.order_id = str(new_order_id)

        new_order.email = email
        new_order.order_type = 'events'
        new_order.status = 'new'
        try:
            person = Person.objects.get(email = new_order.email)
        except:
            person = Person(first_name = firstname, last_name = lastname, email = email)
            person.save()

        new_order.save()

        return redirect('/orders/confirmation/' + str(new_order.order_id))

    return render(request,'website/neweventpage.html', variables)
    
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

def promo(request,promourl):
    cssclass = 'amedia'
    promo = Media.objects.get(url = promourl)
    title = promo.name + "| Promotional Media | Arts on the Hudson"
    variables = {'title':title, 'cssclass':cssclass, 'promo':promo}
    return render(request,'website/video.html', variables)

def contact(request):
    cssclass = 'acontact'
    title = 'Contact | Jersey City | Arts on the Hudson'
    variables = {'title':title, 'cssclass':cssclass,}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['_replyto'].lower()
        message = request.POST['message'].lower()
        form_message = 'Thanks for signing up!'
        sub_time = datetime.datetime.now()
        sub_date = datetime.date.today()
        Incomingmessages.objects.create(email = email, name = name, message = message, sub_time = sub_time, sub_date = sub_date)
        submit_message = 'Thanks for the message, ' + name.split(' ')[0] + '!'
        send_mail('Tenemos un mensajito nuevotito', name + '\n' + email +'\n' + message, 'The Arts on the Hudson team',
                           ['contact@artsonthehudson.com'], fail_silently=True)
        variables = {'title':title, 'cssclass':cssclass, 'submit_message': submit_message }
        return render(request,'website/contact.html', variables )  
    else:
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

