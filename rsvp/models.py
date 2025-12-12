from django.db import models
import uuid

# Create your models here.

### Guest table for RSVP form
class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    attending = models.BooleanField(default=False)
    guests_count = models.PositiveIntegerField(default=1)
    code = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name