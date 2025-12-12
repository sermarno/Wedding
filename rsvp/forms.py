from django import forms
from .models import Guest

# user display form

class RSVPForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['attending', 'guests_count']