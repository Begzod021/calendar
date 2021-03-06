import re
from django.shortcuts import render
from event.models import *
from .serializers import StudentSerializer, CreateStudentSerializer, DeleteStudentSerializer
from .models import StudentGroup
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
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

class StudentList(ListAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination


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
        
        else:
            data = {}

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class DeleteStudent(APIView):
    serializer_class = DeleteStudentSerializer

    def get(self, request, pk):
        
        student = StudentGroup.objects.filter(id=pk)
        student = student[0]
        student.delete()

        return Response({"msg":"DELETED"}, status=status.HTTP_200_OK)