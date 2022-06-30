from django.shortcuts import render
from event.models import *
# Create your views here.

def test(request):
    student = StudentGroup.objects.all()
    context = {
        'student':student
    }
    return render(request, 'tables.html', context )