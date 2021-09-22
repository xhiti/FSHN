from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.student, name='studenti'),
    path('njoftime/', views.notifications, name='njoftime'),
    path('bursa/', views.burses, name='bursa'),
]
