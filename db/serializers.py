from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('patientid','firstname','lastname','m_gender','dateofbirth','address','email','contactnumber','studyid','treatmentid')
        
class PrivGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivilegeGroup
        fields = ('privilegeid', 'groupname')
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('staffid','firstname','lastname','m_gender','dateofbirth','email','contactnumber','privilegeid')
        
class StaffStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffStudy
        fields = ('staffid', 'studyid')
        
class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ('studyid', 'studyname', 'observations', 'status', 'startdate', 'enddate', 'duration', 'treatmentid', 'organisationid')
        
class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ('treatmentid', 'treatmentname', 'supplier')
        
class TrialOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialOrganisation
        fields = ('organisationid', 'organisationname', 'contactnumber')

