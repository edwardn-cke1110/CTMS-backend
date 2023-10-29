from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class ObservationView(viewsets.ModelViewSet):
    serializer_class = ObservationSerializer
    queryset = Observation.objects.all()

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    
class TrialView(viewsets.ModelViewSet):
    serializer_class = TrialSerializer
    queryset = Trial.objects.all()
    
# class TreatmentView(viewsets.ModelViewSet):
#     serializer_class = TreatmentSerializer
#     queryset = Treatment.objects.all()
    
class TrialOrgView(viewsets.ModelViewSet):
    serializer_class = TrialOrgSerializer
    queryset = TrialOrganisation.objects.all()