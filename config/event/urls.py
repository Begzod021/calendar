from django.urls import path
from .views import *
urlpatterns = [
    path('create', CreateEvent.as_view()),
    path('events', GetEvents.as_view()),
    path('event', GetDetailEvent.as_view()),
    path('update', UpdateEvent.as_view()),
]