from django.urls import path
from .views import *
urlpatterns = [
    path('', list),
    path('events/<int:pk>', events, name='test'),
    path('list', StudentList.as_view()),
    path('create', PostStudent.as_view())
]