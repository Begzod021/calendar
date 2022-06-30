from django.shortcuts import render
from event.models import *
# Create your views here.

def list(request):
    student = StudentGroup.objects.all()
    context = {
        'student':student
    }
    return render(request, 'tables.html', context )

def events(request, pk):
    

    context = {
        'id':pk
    }
    return render(request, 'events.html', context)