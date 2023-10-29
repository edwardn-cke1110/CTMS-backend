# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Treatment(models.Model):
#     treatmentid = models.AutoField(db_column='TreatmentID', primary_key=True)  # Field name made lowercase.
#     treatmentname = models.TextField(db_column='TreatmentName')  # Field name made lowercase.
#     supplier = models.TextField(db_column='Supplier')  # Field name made lowercase.
#     treatmenttype = models.CharField(db_column='TreatmentType', max_length=255)  # Field name made lowercase.
#     dosage = models.CharField(db_column='Dosage', max_length=255)  # Field name made lowercase.

#     class Meta:
#         # managed = False
#         db_table = 'treatment'

class Observation(models.Model):
    observationid = models.AutoField(db_column='ObservationID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    date = models.DateTimeField(db_column='DateCreated', auto_now_add=True)  # Field name made lowercase.
    treatment = models.TextField(db_column='Treatment')
    staffid = models.ForeignKey('Staff', models.CASCADE, db_column='StaffID')  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.CASCADE, db_column='PatientID')  # Field name made lowercase.
    trialid = models.ForeignKey('Trial', models.CASCADE, db_column='TrialID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'observation'

class Trial(models.Model):
    trialid = models.AutoField(db_column='TrialID', primary_key=True)  # Field name made lowercase.
    trialname = models.CharField(db_column='TrialName', max_length=255)  # Field name made lowercase.
    trialdescription = models.TextField(db_column='Description')
    status = models.CharField(db_column='Status', max_length=15)  # Field name made lowercase.
    datecreated = models.DateField(db_column='DateCreated', auto_now_add=True)  # Field name made lowercase.
    # treatmentid = models.ForeignKey(Treatment, models.DO_NOTHING, db_column='TreatmentID')  # Field name made lowercase.
    organisationid = models.ForeignKey('TrialOrganisation', models.CASCADE, db_column='OrganisationID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'trial'

class Patient(models.Model):
    patientid = models.AutoField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    m_gender = models.BooleanField(db_column='M_Gender')
    dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
    trialid = models.ForeignKey('Trial', models.CASCADE, db_column='TrialID')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'patient'


class PrivilegeGroup(models.Model):
    privilegeid = models.AutoField(db_column='PrivilegeID', primary_key=True)  # Field name made lowercase.
    groupname = models.TextField(db_column='GroupName')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'privilege_group'


class Staff(models.Model):
    staffid = models.AutoField(db_column='StaffID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    privilegeid = models.ForeignKey(PrivilegeGroup, models.CASCADE, db_column='PrivilegeID')  # Field name made lowercase.
    trials = models.ManyToManyField(Trial)

    class Meta:
        # managed = False
        db_table = 'staff'


class TrialOrganisation(models.Model):
    organisationid = models.AutoField(db_column='OrganisationID', primary_key=True)  # Field name made lowercase.
    organisationname = models.TextField(db_column='OrganisationName')  # Field name made lowercase.
    contactnumber = models.TextField(db_column='ContactNumber')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'trial_organisation'
