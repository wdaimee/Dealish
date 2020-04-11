from django.db import models

# Create your models here.
class Restraurant(models.Model):
    name: models.CharField(max_length=200)
    address: models.CharField(max_length=250)
    Phone_Number: models.CharField(max_length=20)
