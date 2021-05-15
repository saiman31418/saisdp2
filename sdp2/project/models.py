from django.db import models

# Create your models here.
from spyder.Scripts.runxlrd import options


class User(models.Model):
		# fields of the model

        Username = models.CharField(max_length=40)

        email = models.CharField(max_length=50, unique=True)
        phone = models.CharField(max_length=30)
        pass1 = models.CharField(max_length=200)
class Appointment(models.Model):
    selectlocation=models.CharField(max_length=20, choices=(("viajayawada", "vijawada"), ("hyderabad", "hyderabad")),
                                      default="select location")
    selectdepartment=models.CharField(max_length=30,
                                        choices=(("cardio", "cardio"), ("neuro", "neuro"), ("gastro", "gastro")),
                                        default="selectdepartment")
    patientname=models.CharField(max_length=30)
    patientmobile=models.CharField(max_length=30)
    patientEmail=models.CharField(max_length=30)
    doctor=models.CharField(max_length=40,
                                        choices=(("k.jayasurya", "k.jayasurya"), ("b.padmanabhasimha", "b.padmanabhasimha")),
                                        default="doctor")
    datetime=models.DateField(auto_now_add=True,auto_now=False,blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)









class Prescription(models.Model):
     patientname=models.CharField(max_length=40)
     symptoms=models.CharField(max_length=40)

     def __str__(self):
         return self.patientname +"/"+ self.symptoms
class Ambulance(models.Model):
    name=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    location=models.CharField(max_length=30)






class DoctorAdvice(models.Model):
    patientname=models.ForeignKey(Prescription,on_delete=models.CASCADE)

    remedy=models.CharField(max_length=40)







