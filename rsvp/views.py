from django.shortcuts import render, get_object_or_404
from .models import GuestGroup
from .forms import RSVPForm

# handles rsvp form
def rsvp_view(request, code):
    group = get_object_or_404(GuestGroup, code=code)

    if request.method == "POST":
        # instance=guest prefills form with QR code guest info
        form = RSVPForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return render(request, "rsvp/thankyou.html", {"group": group})
        
    else:
        form = RSVPForm(instance=group)

    return render(request, "rsvp/form.html", {"form": form, "group": group})