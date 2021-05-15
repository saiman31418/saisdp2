from django.contrib.auth.views import LoginView

from . import views
from .views import *
from django.urls import path



urlpatterns=[

    path('',index,name='index'),
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('appointment',appointment,name="appointment"),
    path("Admin",Admin,name="Admin"),
    path("AdminAppointments",AdminAppointments,name="AdminAppointments"),
    path("prescription",prescription,name="prescription"),
    path("doctoradvice",doctoradvice,name='doctoradvice'),
    path("Getadvice",Getadvice,name="Getadvice"),
    path('api', views.ChartData.as_view()),
    path('new', views.HomeView.as_view()),
    path("ambulance", ambulance, name="ambulance"),
    path("amb",amb,name="amb")






]