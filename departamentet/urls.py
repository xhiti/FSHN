from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('departamenti-biologjisë/', views.biology_department, name='departamenti-biologjisë'),
    path('departamenti-bioteknologjisë/', views.biotechnology_department, name='departamenti-bioteknologjisë'),
    path('departamenti-fizikës/', views.physic_department, name='departamenti-fizikës'),
    path('departamenti-informatikës/', views.informatic_department, name='departamenti-informatikës'),
    path('departamenti-kimisë/', views.chemistry_department, name='departamenti-kimisë'),
    path('departamenti-kimisë-industriale/', views.industrial_chemistry_department, name='departamenti-kimisë-industriale'),
    path('departamenti-matematikës/', views.mathematic_department, name='departamenti-matematikës'),
    path('departamenti-matematikës-aplikuar/', views.applied_mathematic_department, name='departamenti-matematikës-aplikuar'),
    path('qendra-kërkimore-florës-dhe-faunës/', views.search_center_flora_and_fauna_department, name='qendra-kërkimore-florës-dhe-faunës'),
    path('projekte/', views.projects, name='projekte'),
    path('doktoratura/', views.doctoratures, name='doktoratura'),
    path('publikime-dhe-konferenca/', views.publications_and_conferences, name='publikime-dhe-konferenca'),
    path('e-learning/', views.elearning, name='e-learning'),
    path('pedagog/', views.academic, name='pedagog')
]
