from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    
class StaffStudyView(viewsets.ModelViewSet):
    serializer_class = StaffStudySerializer
    queryset = StaffStudy.objects.all()
    
class StudyView(viewsets.ModelViewSet):
    serializer_class = StudySerializer
    queryset = Study.objects.all()
    
class TreatmentView(viewsets.ModelViewSet):
    serializer_class = TreatmentSerializer
    queryset = Treatment.objects.all()
    
class TrialOrgView(viewsets.ModelViewSet):
    serializer_class = TrialOrgSerializer
    queryset = TrialOrganisation.objects.all()
    