from django.shortcuts import render
from .models import Event
from .serializers import CreateEventSerializer, GetEventsSerializer
from rest_framework.views import APIView
from rest_framework import status, generics
from  rest_framework.response import Response
# Create your views here.


class CreateEvent(APIView):
    serializer_class =CreateEventSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            title = serializer.data.get('title')
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            url = serializer.data.get('url')


            event = Event(title=title, start_date=start_date, end_date=end_date, url=url)
            event.save()

            return Response(CreateEventSerializer(event).data, status=status.HTTP_201_CREATED)

        return Response({"msg":"No Content"}, status=status.HTTP_204_NO_CONTENT)


class GetEvent(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = GetEventsSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
