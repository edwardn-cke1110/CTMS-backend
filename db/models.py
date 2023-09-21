from django.db import models

# Models
class Patient(models.Model):
    patientid = models.IntegerField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', max_length=255)  # Field name made lowercase.
    m_gender = models.BooleanField(db_column='Gender')
    dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255)  # Field name made lowercase.
    email = models.TextField(db_column='Email', max_length=255)
    contactnumber = models.TextField(db_column='ContactNumber', max_length=10)  # Field name made lowercase.
    studyid = models.ForeignKey('Study', models.DO_NOTHING, db_column='StudyID')  # Field name made lowercase.
    treatmentid = models.ForeignKey('Treatment', models.DO_NOTHING, db_column='TreatmentID')  # Field name made lowercase.

    # class Meta:
    #     # managed = False
    #     db_table = 'patient'
        
class PrivilegeGroup(models.Model):
    privilegeid = models.IntegerField(db_column='PrivilegeID', primary_key=True)  # Field name made lowercase.
    groupname = models.TextField(db_column='GroupName', max_length=255)  # Field name made lowercase.

    # class Meta:
    #     # managed = False
    #     db_table = 'privilege_group'


class Staff(models.Model):
    staffid = models.IntegerField(db_column='StaffID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', max_length=255)  # Field name made lowercase.
    m_gender = models.BooleanField(db_column='Gender')
    dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
    email = models.TextField(db_column='Email', max_length=255)
    contactnumber = models.TextField(db_column='ContactNumber', max_length=10)  # Field name made lowercase.
    privilegeid = models.ForeignKey('PrivilegeGroup', models.DO_NOTHING, db_column='PrivilegeID')  # Field name made lowercase.

    # class Meta:
    #     # managed = False
    #     db_table = 'staff'

#Composite key not supported
class StaffStudy(models.Model):
    staffid = models.OneToOneField('Staff', models.DO_NOTHING, db_column='StaffID', primary_key=True)  # Field name made lowercase. The composite primary key (StaffID, StudyID) found, that is not supported. The first column is selected.
    studyid = models.ForeignKey('Study', models.DO_NOTHING, db_column='StudyID')  # Field name made lowercase.

    # class Meta:
    #     # managed = False
    #     db_table = 'staffstudy'
    #     unique_together = (('staffid', 'studyid'),)

class Study(models.Model):
    studyid = models.IntegerField(db_column='StudyID', primary_key=True)  # Field name made lowercase.
    studyname = models.TextField(db_column='StudyName', max_length=255)  # Field name made lowercase.
    observations = models.TextField(db_column='Observations')  # Field name made lowercase.
    status = models.TextField(db_column='Status', max_length=15)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=255)  # Field name made lowercase.
    treatmentid = models.ForeignKey('Treatment', models.DO_NOTHING, db_column='TreatmentID')  # Field name made lowercase.
    organisationid = models.ForeignKey('TrialOrganisation', models.DO_NOTHING, db_column='OrganisationID')  # Field name made lowercase.

    # class Meta:
    #     # managed = False
    #     db_table = 'study'


class Treatment(models.Model):
    treatmentid = models.IntegerField(db_column='TreatmentID', primary_key=True)  # Field name made lowercase.
    treatmentname = models.TextField(db_column='TreatmentName')  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=255)
    description = models.TextField(db_column='Description')
    supplier = models.TextField(db_column='Supplier')  # Field name made lowercase.

    # class Meta:
    #     # managed = False
    #     db_table = 'treatment'


class TrialOrganisation(models.Model):
    organisationid = models.IntegerField(db_column='OrganisationID', primary_key=True)  # Field name made lowercase.
    organisationname = models.TextField(db_column='OrganisationName', max_length=255)  # Field name made lowercase.
    contactnumber = models.TextField(db_column='ContactNumber', max_length=10)  # Field name made lowercase.

    # class Meta:
    #     # managed = False
    #     db_table = 'trial_organisation'
