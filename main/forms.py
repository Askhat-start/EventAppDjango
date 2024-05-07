from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "organizer", "description", "event_time", "event_date", "duration", "city", "location",
                  "seats_amount", "event_type", "available_seats", "photo"]


t = 1