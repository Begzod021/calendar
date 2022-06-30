from .models import StudentGroup
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentGroup
        fields = ('name','id',)