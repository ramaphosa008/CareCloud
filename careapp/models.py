from os import name

from django.db import models

# Create your models here. # A model is a table 
class patient(models.Model) :
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    dateregistered = models.DateTimeField()        # DateTime - used to display date and time
    medhistory = models.TextField() # Text field is used when the text area has multiple lines of data

    def __str__(self) :
          return self.firstname +""+ self.lastname 
    
class doctor(models.Model) :
     firstname = models.CharField(max_length=255)
     lastname = models.CharField(max_length=25)
     birthdate = models.DateField()
     age = models.IntegerField()
     gender = models.CharField(max_length=10)
     dateemployed = models.DateTimeField
     position = models.CharField(max_length=20)
     speciality = models.CharField(max_length=50)


class myAppointment(models.Model) :
     name = models.CharField(max_length=200)
     email = models.EmailField()
     phone = models.CharField(max_length=20)
     datetime = models.DateTimeField()
     department = models.CharField(max_length=100)
     doctor = models.CharField(max_length=20)
     message = models.TextField()

     def __str__(self):
          return self.name

class Transaction(models.Model) :
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"




