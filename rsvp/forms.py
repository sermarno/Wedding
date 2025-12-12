from django import forms
from .models import GuestGroup

# user display form

class RSVPForm(forms.ModelForm):
    class Meta:
        model = GuestGroup
        fields = ['attending', 'guests_count']