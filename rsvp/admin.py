from django.contrib import admin
from .models import GuestGroup

# Register your models here.
admin.site.register(GuestGroup)

class GuestGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'email', 'attending', 'guests_count')
    list_filter = ('attending',)
    search_fields = ('group_name', 'email')