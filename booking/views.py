from django.shortcuts import render
from .models import EventUser
from main.models import Event
from django.core.exceptions import ObjectDoesNotExist


def take_part(request, event_id):
    event = Event.objects.get(id=event_id)
    event.available_seats -= 1
    event.save()

    event_user = EventUser(event=event, user=request.user)
    event_user.save()

    my_events_list = EventUser.objects.filter(user=request.user)

    return render(request, 'booking/my_events.html', {'my_events_list': my_events_list, 'new_event': event})


def my_events(request):
    my_events = EventUser.objects.filter(user=request.user)
    return render(request, 'booking/my_events.html', {'my_events_list': my_events, 'new_event': None})


def delete_book(request, event_id):
    event = Event.objects.get(id=event_id)
    event_user = EventUser.objects.get(event=event, user=request.user)
    event_user.delete()
    event.available_seats += 1
    event.save()

    return render(request, 'booking/my_events.html', {'my_events_list': my_events, 'new_event': None,
                                                      'deleted_event': event})
