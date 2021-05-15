from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import message
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, request
from .forms import UserForm, patientAppointment, PrescriptionForm, DoctorAdviceForm, AmbulanceForm
from .models import Appointment, Prescription, DoctorAdvice, Ambulance
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from .models import User
from django.core.mail import send_mail
from  sdp2 import settings
# Create your views here.
def index(request):
   return  render(request,"index.html")
def register(request):
   if request.method == "POST":

     form=UserForm(request.POST)
     if form.is_valid():

        form.save()
        return render(request,"login.html")

     else:
        return HttpResponse("invalid")

   else:
      form=UserForm()


   return render(request, 'register.html',{"form":form})







def login(request):
   if request.method == 'POST':
      username=request.POST["username"]
      pass1=request.POST["pass1"]
      #user=auth.authenticate(username=username,password=pass1)
      ex=User.objects.get(Username=username)

      if username==ex.Username and pass1==ex.pass1:
         return render(request,"home.html")


      #if user is not None:
       #  auth.login(request,user)
        # return render(request,"home.html")

      else:
         return HttpResponse("invalid")






   else:
      return render(request,"login.html")
def appointment(request):

   if request.method=='POST':
      appointmentform = patientAppointment(request.POST)
      if appointmentform.is_valid():
         appointmentform.save()
      else:
         return HttpResponse("invalid")
   else:
      appointmentform = patientAppointment()

   return render(request,"appointment.html",{"appointmentform":appointmentform})

def Admin(request):
   if request.method == 'POST':
      username=request.POST["username"]
      pass1=request.POST["pass1"]
      user=auth.authenticate(username=username,password=pass1)
      if user is not None:
         auth.login(request,user)
         return redirect("AdminAppointments")

      else:
         print("invalid")







   else:
      return render(request,"admin.html")
def AdminAppointments(request):
   ap=Appointment.objects.all()

   return render(request,"adminpage.html",{"ap":ap})
def prescription(request):
   if request.method == 'POST':
      prescriptionform = PrescriptionForm(request.POST)
      if prescriptionform.is_valid():
         prescriptionform.save()
      else:
         return HttpResponse("invalid")
   else:
      prescriptionform = PrescriptionForm()

   return render(request, "prescription.html", {"prescriptionform": prescriptionform})
def doctoradvice(request):
   if request.method == 'POST':
      doctoradvice = DoctorAdviceForm()
      patient = Prescription.objects.all()
      context = {
         "patient": patient,
         "doctoradvice": doctoradvice}
      doctoradvice = DoctorAdviceForm(request.POST)
      if doctoradvice.is_valid():
         doctoradvice.save()
      else:
         return HttpResponse("invalid")
   else:
         doctoradvice= DoctorAdviceForm()
         patient=Prescription.objects.all()
         context={
            "patient": patient,
            "doctoradvice":doctoradvice }
   return render(request, "doctoradvice.html",  context)
def Getadvice(request):
   da= DoctorAdvice.objects.all()
   return  render(request,"getadvice.html",{"da":da})


class HomeView(View):
   def get(self, request, *args, **kwargs):
      return render(request, 'ds.html')


class ChartData(APIView):
   authentication_classes = []
   permission_classes = []


   def get(self, request, format=None):
      a = 0
      labels = []
      chartLabel = "my data"
      chartdata = []
      emp = Prescription.objects.raw('SELECT distinct * FROM project_Prescription GROUP BY symptoms')
      for i in emp:
         labels.append(i.symptoms)
         emp1 = Prescription.objects.filter(symptoms=i.symptoms).distinct()
         for j in emp1:
            a=a+1
         chartdata.append(a)
         a=0
      print(chartdata)

      data = {
         "labels": labels,
         "chartLabel": chartLabel,
         "chartdata": chartdata,
      }
      return Response(data)
def ambulance(request):
   res=0
   if request.method == "POST":

     form=AmbulanceForm(request.POST)
     if form.is_valid():
        obj=Ambulance.objects.all()
        for i in obj:
           subject = "alert!!!!"
           msg = "name:" + i.name +"\n"+ "location" + i.location+ "\n"+"phone" + i.phonenumber + ""
           to = "bharathcherukuri00@gmail.com"
           res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        if (res == 1):
           msg = "Mail Sent" + i.name+ " Successfuly "
        else:
           msg = "Mail could not sent"



        form.save()



     else:
        return HttpResponse("invalid")

   else:
      form=AmbulanceForm()


   return render(request, 'ambulance.html',{"form":form})
def amb(request):

      form=AmbulanceForm()


      return render(request, 'ambulance.html',{"form":form})














