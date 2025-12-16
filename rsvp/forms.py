from django import forms
from .models import GuestGroup

class RSVPForm(forms.ModelForm):
    ATTENDING_CHOICES = [
        (True, "Yes, I'll be there!'"),
        (False, "No, I can't make it."),
    ]

    attending = forms.ChoiceField(
        choices=ATTENDING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
        label="Will you be attending?"
    )

    GUEST_COUNT_CHOICES = [(i, str(i)) for i in range(1, 11)]

    guests_count = forms.ChoiceField(
        choices=GUEST_COUNT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-input'}),
        label="How many total guests (including yourself)?"
    )

    email = forms.EmailField(
        required=False,
        label="Email (for updates)",
        widget=forms.EmailInput(attrs={'class': 'form-input'})
    )

    guest_names = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, 'class': 'form-input'}),
        required=False,
        label="Names of additional guests"
    )

    class Meta:
        model = GuestGroup
        fields = ['email', 'attending', 'guests_count', 'guest_names']
