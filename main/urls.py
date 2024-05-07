from django.urls import path
from . import views
from booking import views as booking_views


app_name = 'main'

urlpatterns = [
    path('', views.main_events, name='main'),
    path('event/<int:event_id>', views.event_description, name='event_description'),
    path('event/<int:event_id>/take_part', booking_views.take_part, name='take_part'),
    path('create_event/', views.create_event, name='create_event')
]
