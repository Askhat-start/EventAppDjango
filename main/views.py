from django.shortcuts import render
from .models import *
from booking.models import *
from .forms import EventForm
from django.shortcuts import redirect


def main_events(request):
    events = Event.objects.all()
    return render(request, 'main/main.html', {'events': events})


def event_description(request, event_id):
    event = Event.objects.get(id=event_id)
    already_take_part = False
    if request.user.is_authenticated:
        if event in [i.event for i in EventUser.objects.filter(user=request.user)]:
            already_take_part = True
    return render(request, 'main/description.html', {'event': event, 'already_take_part': already_take_part})


def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            events = Event.objects.all()
            return render(request, 'main/main.html', {'events': events})

    form = EventForm()
    return render(request, 'main/event_creator.html', {'form': form})
