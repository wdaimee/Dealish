from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from geopy.geocoders import GoogleV3
from urllib.error import URLError
from django.contrib.gis import geos
from django.contrib.gis import measure
from django.contrib.gis.db.models.functions import Distance
from django.http import JsonResponse
from django.urls import reverse
import json
from django.core.serializers import serialize
import decimal 

from .forms import *
from .models import *

# Create your views here.
def redirect_view(request):
    return redirect('deals/')

# Decimal_default function to convert lat/lan decimal in model to floats, 
# used to convert to JSON in deals_index function
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

#Main page with a list of deals in your area, will send back JSON response with a list of restaurants
# in your area, used to display markers and populate cards with restaurant and deal information
@login_required
def deals_index(request):
    restaurants = []
    if request.GET and request.is_ajax():
        lat = request.GET.get('lat')
        lng = request.GET.get('long')
        restaurants_backend = get_restaurants(lng, lat)
        for restaurant in restaurants_backend:
            deal = restaurant.deal_set.first()
            doc = {"res_id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "city": restaurant.city, "lat": restaurant.lat, "lng": restaurant.lng, 
            'deal_name': deal.name, 'deal_price': deal.price, 'deal_description': deal.description}
            restaurants.append(doc)
            doc = {}
        print(restaurants)    
        return JsonResponse(json.dumps(list(restaurants), default=decimal_default), safe=False)
    return render(request, 'deals/index.html', {'restaurants': restaurants, 'reply':'success'})

@login_required    
def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    review_form = ReviewForm()
    deals = restaurant.deal_set.all()
    reviews = restaurant.review_set.all()
    return render(request, 'restaurant/detail.html', {'restaurant': restaurant, 'deals': deals, 'form': review_form, 'reviews': reviews})

# follow add feeding cats lesson, form will be needed, 
# logged in user needs to be added to review when created

@login_required
def add_review(request, restaurant_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.restaurant_id = restaurant_id
        new_review.user_id = 1
        new_review.save()
    return redirect('restaurant_detail', restaurant_id=restaurant_id)


class Delete_review(LoginRequiredMixin, DeleteView):
    model = Review
    succes_url = '/restaurants/'
    
        

# Use the same form as add_review

class UpdateReview(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['text']

@login_required
def add_like(request):
    pass

@login_required
def favourites_index(request, restaurant_id):
    pass
    
    
@login_required
def add_favourite(request, restaurant_id):
    form = FavouritesForm(request.POST)
    if form.is_valid():
        new_fav = form.save(commit=False)
        new_fav.restaurant_id = restaurant_id
        new_fav.save()
    return redirect('restaurant_detail', restaurant_id=restaurant_id)

class Delete_favourite(LoginRequiredMixin, DeleteView):
    model = Favourite
    success_url = '/favourties/'

# form needed
@login_required
def add_note(request):
    pass

@login_required
def delete_note(request):
    pass

@login_required
def update_note(request):
    pass


def about_dealish(request):
    return render(request, 'about.html')



def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('deals_index')
    context = {'form': form} 
    return render(request, 'registration/signup.html', context)

# Function to get a list of restaurants in your area that are within 10 KM of user location
def get_restaurants(longitude, latitude):
    current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude), srid=4326)
    distance_from_point = {'km': 10}
    restaurants = Restaurant.objects.filter(coordinates__distance_lte=(current_point, measure.D(**distance_from_point))).annotate(distance=Distance('coordinates', current_point)).order_by('distance')
    return restaurants