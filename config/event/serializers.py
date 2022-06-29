from rest_framework import serializers
from .models import Event


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date')

class GetEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'url', 'id')

class GetEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'url', 'id')

class UpdateEventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'id')
