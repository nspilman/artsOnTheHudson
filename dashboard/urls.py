from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from . import views
from timelog import views as timeviews

urlpatterns = [
    path('', views.dashboard, name = 'dashboard' ),
    path('time/',timeviews.reporting_home, name = 'timereport'),
]