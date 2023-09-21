from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    m_gender = models.BooleanField()
    address = models.TextField()
    email = models.CharField(max_length=255)
    contactno = models.CharField(max_length=10)
    
    def _str_(self):
        return self.firstname + ' ' + self.lastname