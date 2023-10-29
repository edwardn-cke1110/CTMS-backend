from rest_framework import serializers
from .models import *

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ('observationid','description', 'date','treatment','staffid', 'patientid', 'trialid')

class TrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trial
        fields = ('trialid', 'trialname', 'trialdescription', 'status', 'datecreated','organisationid')
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('patientid','firstname','lastname','m_gender','dateofbirth','trialid')

class PrivGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivilegeGroup
        fields = ('privilegeid', 'groupname')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('staffid','firstname','lastname','privilegeid')
        
class TrialOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialOrganisation
        fields = ('organisationid', 'organisationname', 'contactnumber')