from django.db import models
from main.models import Event
from django.contrib.auth.models import User


class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return [self.event, self.user]
