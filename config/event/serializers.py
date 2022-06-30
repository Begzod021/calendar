from rest_framework import serializers
from .models import Event

class GetDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('start_date','end_date', 'students')


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'url')

class GetEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'url', 'id', 'students')

class GetEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'url', 'id')

class UpdateEventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'id')
