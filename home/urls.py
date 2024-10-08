from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('resume/', views.resume, name='resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)