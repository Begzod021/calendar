from django.urls import path
from .views import *
urlpatterns = [
    path('create', CreateEvent.as_view()),
    path('events', GetEvent.as_view()),
    path('event', GetDetailEvent.as_view()),
]