from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restraurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    picture = models.CharField(max_length=20) # possibly change to imagefield?
    Likes = models.IntegerField(default=0)

class Deals(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    restraurant = models.ForeignKey(Restraurant, on_delete=models.CASCADE)

class Review(models.Model):
    text = models.TextField(max_length=250)
    restraurant = models.ForeignKey(Restraurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favourite(models.Model):
    restaurant = models.ForeignKey(Restraurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Notes(models.Model):
    text: models.TextField(max_length=250)
    favourite = models.ForeignKey(Favourite, on_delete=models.CASCADE)