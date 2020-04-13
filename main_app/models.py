from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.db import models
from django.contrib.auth.models import User
import geopy.geocoders
from geopy.geocoders import GoogleV3
from urllib.error import URLError
import os

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100, default='Toronto')
    phone_number = models.CharField(max_length=20)
    picture = models.CharField(max_length=20) # possibly change to imagefield?
    Likes = models.IntegerField(default=0)
    coordinates = gis_models.PointField(u"longitdue/latitude", geography=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.coordinates:
            address = f"{self.address} {self.city}"
            address = address.encode('utf-8')
            geocoder = GoogleV3(api_key=os.environ['GOOGLE_API_KEY'])
            try:
                _, latlon = geocoder.geocode(address)
            except (URLError, ValueError, TypeError):
                pass
            else:
                point = f"POINT({latlon[1]} {latlon[0]})"
                self.coordinates = geos.fromstr(point)
        super(Restaurant, self).save()

class Deal(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    restraurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Review(models.Model):
    text = models.TextField(max_length=250)
    restraurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favourite(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Note(models.Model):
    text = models.TextField(max_length=250)
    favourite = models.ForeignKey(Favourite, on_delete=models.CASCADE)