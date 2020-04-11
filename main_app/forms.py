from django.forms import ModelForm
from .models import Review, Notes

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['text']