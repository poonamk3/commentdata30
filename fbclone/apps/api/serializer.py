from django.db import models
from rest_framework import serializers
from .models import Student,StudentClass

# Create your models here.
"""
class StudentSeralizer(serializers.Serializer):
	name=serializers.CharField(max_length=200)
	roll=serializers.IntegerField()
	city=serializers.CharField(max_length=200)
	def create(self, validated_data):
		return Student.objects.create(**validated_data)
"""
class StudentClassSeralizer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ['classname']
class StudentSeralizer(serializers.ModelSerializer):
	stuclass=serializers.StringRelatedField(many=True,read_only=True)
	class Meta:
		model = Student
		fields = ['id', 'name', 'roll', 'city','stuclass']

        
