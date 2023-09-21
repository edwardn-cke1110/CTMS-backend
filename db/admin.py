from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','dob','m_gender','address','email','contactno')

# Register your models here.
admin.site.register(Patient, PatientAdmin)