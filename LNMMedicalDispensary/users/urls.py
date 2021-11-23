from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('doctor/', views.doctor, name='doctor'),
    path('chemist/', views.chemist, name='chemist'),
    path('patient/', views.patient, name='patient'),
    path('scheduleTest/', views.scheduleTest, name='scheduleTest'),
    path('patientHistory/', views.patientHistory, name='patientHistory'),
<<<<<<< HEAD
    path('viewPatientHistory/', views.viewPatientHistory, name='viewPatientHistory'),
=======
    path('feedback/', views.feedback, name='feedback'),
    path('patientProfile/', views.patientProfile, name='patientProfile'),
>>>>>>> 1bd8fe30dd84a3fe18d284c5d2c9f192e4bd4b21
]
