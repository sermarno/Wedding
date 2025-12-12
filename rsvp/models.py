from django.db import models
import uuid

# Create your models here.

### Guest table for RSVP form
class GuestGroup(models.Model):
    group_name = models.CharField(max_length=100)
    attending = models.BooleanField(default=False)
    guests_count = models.PositiveIntegerField(default=1)
    code = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.group_name