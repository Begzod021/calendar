from django.shortcuts import render
from event.models import *
from .serializers import StudentSerializer, CreateStudentSerializer
from .models import StudentGroup
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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

class StudentList(APIView):
    serializer_class = StudentSerializer

    def get(self, request):

        students = StudentGroup.objects.all()
        serializer = self.serializer_class(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostStudent(APIView):
    serializer_class = CreateStudentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            name = serializer.data.get('name')
            student_group = serializer.data.get('student_group')
            description = serializer.data.get('description')

            student = StudentGroup(name=name, student_group=student_group, description=description)
            student.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)