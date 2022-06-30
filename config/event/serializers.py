from unicodedata import name
from rest_framework import serializers
from .models import Event, StudentGroup

class GetDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('start_date','end_date')

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['name']


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'url', 'students')

    def get_students(self, obj):
        return StudentGroup.objects.filter(name=obj)

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
