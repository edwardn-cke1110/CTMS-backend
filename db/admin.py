from django.contrib import admin
from .models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patientid','firstname','lastname','m_gender','dateofbirth','address','email','contactnumber','studyid','treatmentid')

class PrivGroupAdmin(admin.ModelAdmin):
    list_display = ('privilegeid', 'groupname')
    
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staffid','firstname','lastname','m_gender','dateofbirth','email','contactnumber','privilegeid')

class StaffStudyAdmin(admin.ModelAdmin):
    list_display = ('staffid', 'studyid')
    
class StudyAdmin(admin.ModelAdmin):
    list_display = ('studyid', 'studyname', 'observations', 'status', 'startdate', 'enddate', 'duration', 'treatmentid', 'organisationid')
    
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatmentid', 'treatmentname', 'dosage', 'description', 'supplier')
    
class TrialOrgAdmin(admin.ModelAdmin):
    list_display = ('organisationid', 'organisationname', 'contactnumber')

# Register your models here.
admin.site.register(Patient, PatientAdmin)
admin.site.register(PrivilegeGroup, PrivGroupAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffStudy, StaffStudyAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(TrialOrganisation, TrialOrgAdmin)