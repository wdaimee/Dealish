from django.shortcuts import render, redirect
from .forms import ReviewForm, NotesForm
from django.http import HttpResponse

# Create your views here.
def redirect_view(request):
    return redirect('deals/')

def deals_index(request):
    pass
    
def restaurant_detail(request):
    pass

# follow add feeding cats lesson, form will be needed
def add_review(request):
    pass

def delete_review(request):
    pass
# Use the same form as add_review
def update_review(request):
    pass

def add_like(request):
    pass

def dislike(request):
    pass

def user_detail(request):
    pass

def favourites_index(request):
    pass

def add_favourite(request):
    pass

def delete_favourite(request):
    pass

# form needed
def add_note(request):
    pass

def delete_note(request):
    pass

def update_note(request):
    pass

def signup(request):
    pass

