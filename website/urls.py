from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from .models import Education, Events, Media

from . import views

info_dict = {
    'queryset' : Education.objects.all()
}

urlpatterns = [
    path('', views.index, name = 'home'),
    path('staff/', views.staff, name = 'staff' ),
    path('contact/', views.contact, name = 'contact'),
    path('press/', views.press, name = 'press'),
    path('donate/', views.give, name = 'donate'),
    path('education/', views.education, name = 'education'),
    path('about/', views.founder, name = 'education'),
    path('mission/', views.mission, name = 'mission'),
    path('promomedia/', views.media, name = 'media'),
    path('promomedia/<promourl>', views.promo, name = 'promo'),
    path('<events>/', views.events, name = 'events'),
    path('events/<eventurl>', views.eventpage, name = 'event'),
    path('education/<programurl>/', views.program, name = 'program'), 
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)