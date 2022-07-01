from django.shortcuts import render
from .models import Event, StudentGroup
from .serializers import (
    CreateEventSerializer,
    GetEventsSerializer,
    GetEventSerializer,
    UpdateEventSerializer,
    GetDateSerializer
)
from rest_framework.views import APIView
from rest_framework import status
from  rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
import requests
class CreateEvent(APIView):
    permission_classes = [IsAdminUser]
    serializer_class =CreateEventSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            url = serializer.data.get('url')
            id= serializer.data.get('students')
            students = StudentGroup.objects.filter(id=id)
            students = students[0]

            event = Event(title=title, start_date=start_date, end_date=end_date, url=url, students=students)
            event.save()

            return Response(CreateEventSerializer(event).data, status=status.HTTP_201_CREATED)

        return Response({"msg":"No Content"}, status=status.HTTP_204_NO_CONTENT)


class GetEvents(APIView):

    serializer_class = GetEventsSerializer
    def post(self, request):
        serializer = GetDateSerializer(data=request.data)
        if serializer.is_valid():
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')

            events = Event.objects.filter(start_date__gte=start_date, start_date__lte=end_date)
            serializer = self.serializer_class(events, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK) 
            

class UpdateEvent(APIView):
    serializer_class = UpdateEventSerializer
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            id = serializer.data.get('id')
            print(start_date)
            queryset = Event.objects.filter(id=id)
            if not queryset.exists():
                return Response({"msg":"Event Not Found"}, status=status.HTTP_404_NOT_FOUND)
            event = queryset[0]

            event.title = title
            event.start_date = start_date
            event.end_date = end_date
            event.save(update_fields=["title", "start_date", "end_date"])

            return Response(UpdateEventSerializer(event, many=False).data, status=status.HTTP_200_OK)

        return Response({"msg":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class DeleteEvent(APIView):
    serializer_class = GetEventSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.data.get('id')
            event = Event.objects.filter(id=id)
            event.delete()
            return Response({'msg':'DELETED'}, status=status.HTTP_200_OK)

def calendar_s(request):
    return render(request, 'index.html')    


class DetailEvent(APIView):
    serializer_class = GetEventsSerializer
    def get(self, request, pk):
        students = StudentGroup.objects.filter(id=pk)
        students = students[0]
        events = Event.objects.filter(students=students)
        serializer = self.serializer_class(events, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
#signal, requests, generic, session, pagination, permission, validates, ORM