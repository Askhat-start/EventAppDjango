from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.my_events, name='my_events'),
    path('delete_book/<int:event_id>', views.delete_book, name='delete_book')
]
