from django.db import models
from rest_framework import serializers
from .models import Student

# Create your models here.
"""
class StudentSeralizer(serializers.Serializer):
	name=serializers.CharField(max_length=200)
	roll=serializers.IntegerField()
	city=serializers.CharField(max_length=200)
	def create(self, validated_data):
		return Student.objects.create(**validated_data)
"""
class StudentSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']