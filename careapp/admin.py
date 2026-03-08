from django.contrib import admin
from careapp.models import *       # Asterik reps all models in models.py

# Register your models here.
admin.site.register(patient)

admin.site.register(doctor)

admin.site.register(myAppointment)

admin.site.register(Transaction)