from django import forms
from .models import User, Appointment, DoctorAdvice, Prescription, Ambulance


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
class patientAppointment(forms.ModelForm):
    class Meta:
        model=Appointment
        fields="__all__"

class DoctorAdviceForm(forms.ModelForm):
    class Meta:
        model=DoctorAdvice
        fields=['remedy','patientname']
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model=Prescription
        fields="__all__"
class AmbulanceForm(forms.ModelForm):
    class Meta:
        model=Ambulance
        fields="__all__"






