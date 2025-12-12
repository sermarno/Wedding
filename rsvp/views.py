from django.shortcuts import render, get_object_or_404, redirect
from .models import Guest
from .forms import RSVPForm

# handles rsvp form
def rsvp_view(request, code):
    guest = get_object_or_404(Guest, code=code)

    if request.method == "POST":
        # instance=guest prefills form with QR code guest info
        form = RSVPForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return render(request, "rsvp/thankyou.html", {"guest": guest})
        
    else:
        form = RSVPForm(instance=guest)

    return render(request, "rsvp/form.html", {"form": form, "guest": guest})