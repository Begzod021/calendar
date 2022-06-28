from django.urls import path
from .views import *
urlpatterns = [
    path('', calendar),
    path('create', CreateEvent.as_view()),
    path('events', GetEvent.as_view()),

]