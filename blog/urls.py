from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('<id>', views.post, name = ''),
    path('', views.posts, name = ''),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)