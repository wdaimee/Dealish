from django.forms import ModelForm
from .models import Review, Note, Favourite

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']

class NotesForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text']

class FavouritesForm(ModelForm):
    class Meta:
        model = Favourite
        fields = []