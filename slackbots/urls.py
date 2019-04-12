from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from slackbots.views import Events

from . import views

urlpatterns = [
    path('timelog',Events.as_view(), name = 'timelog'),    
    path('test/', views.test, name = 'staff' ),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
