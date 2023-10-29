from django.contrib import admin
from .models import *

class ObservationAdmin(admin.ModelAdmin):
    list_display = ('observationid', 'description', 'date','staffid', 'patientid', 'trialid')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patientid','firstname','lastname','m_gender','dateofbirth','trialid')

class PrivGroupAdmin(admin.ModelAdmin):
    list_display = ('privilegeid', 'groupname')
    
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staffid','firstname','lastname','privilegeid')
    
# class TreatmentAdmin(admin.ModelAdmin):
#     list_display = ('treatmentid', 'treatmentname', 'supplier', 'treatmenttype', 'dosage')
    
class TrialAdmin(admin.ModelAdmin):
    list_display = ('trialid', 'trialname', 'status', 'datecreated','organisationid')
    
class TrialOrgAdmin(admin.ModelAdmin):
    list_display = ('organisationid', 'organisationname', 'contactnumber')

# Register your models here.
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PrivilegeGroup, PrivGroupAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Trial, TrialAdmin)
# admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(TrialOrganisation, TrialOrgAdmin)