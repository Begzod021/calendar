from django.urls import path
from .views import *
urlpatterns = [
    path('', calendar_s, name='calendar'),
    path('create', CreateEvent.as_view()),
    path('events', GetEvents.as_view()),
    path('update', UpdateEvent.as_view()),
    path('delete', DeleteEvent.as_view()),
    path('events/<int:pk>', DetailEvent.as_view(), name='events'),
]