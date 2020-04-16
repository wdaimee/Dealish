from django.shortcuts import render, redirect
from .forms import ReviewForm, NotesForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def redirect_view(request):
    return redirect('deals/')

def deals_index(request):
    return render(request, 'deals/index.html')
    
def restaurant_detail(request):
    pass

# follow add feeding cats lesson, form will be needed, 
# logged in user needs to be added to review when created
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
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('deals_index')
    context = {'form': form} 
    return render(request, 'registration/signup.html', context)

