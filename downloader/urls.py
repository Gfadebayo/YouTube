
from django.urls import path
from . import views

app_name = 'downloader'
urlpatterns = [
path('', views.home, name='home'),
path('processing/', views.process, name='process'),
]
