from django.shortcuts import render
from .serializer import StudentSeralizer,StudentClassSeralizer
import io
from .models import Student,StudentClass
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
class UserViewSet(viewsets.ModelViewSet):
	serializer_class = StudentSeralizer
	queryset = Student.objects.all()
	# authentication_classes = [SessionAuthentication]
	# permission_classes = [IsAuthenticatedOrReadOnly]

class ClassStudentView(viewsets.ModelViewSet):
	serializer_class = StudentClassSeralizer
	queryset = StudentClass.objects.all()
	# authentication_classes = [SessionAuthentication]
	# permission_classes = [IsAuthenticatedOrReadOnly]
"""
#Read only view set use list and retrive
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = StudentSeralizer
	queryset = Student.objects.all()
"""
"""
class StudentList(ListModelMixin,GenericAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSeralizer
	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

class StudentCreate(CreateModelMixin,GenericAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSeralizer
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

class StudentRetrieve(RetrieveModelMixin,GenericAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSeralizer
	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)


class StudentUpdate(UpdateModelMixin,GenericAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSeralizer
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

class StudentDelete(DestroyModelMixin,GenericAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSeralizer
	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)


"""

"""
class StudentApi(APIView):
	def get(self,request,pk=None,format=None):
		id=pk
		if id is not None:
			stu=Student.objects.get(id=id)
			serializer=StudentSeralizer(stu)
			return Response(serializer.data)
	
		stu=Student.objects.all()
		serializer=StudentSeralizer(stu,many=True)
		return Response(serializer.data)
	def post(self,request,format=None):
		serializer=StudentSeralizer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'this is a post method'})
		return Response(serializer.errors)

	def put(self,request,pk=None,format=None):
		id= pk
		stu=Student.objects.get(pk=id)
		serializer=StudentSeralizer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'this is a put method'})
		return Response(serializer.errors)

	def patch(self,request,pk=None,format=None):
		id= pk
		stu=Student.objects.get(pk=id)
		serializer=StudentSeralizer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'this is a patch method'})
		return Response(serializer.errors)	

	def delete(self,request,pk=None,format=None):
		id= pk
		stu=Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'this is a delete method'})

"""

"""
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def hello(request,pk=None):
	if request.method == 'GET':
		# id= request.data.get('id')
		id=pk
		if id is not None:
			stu=Student.objects.get(id=id)
			serializer=StudentSeralizer(stu)
			return Response(serializer.data)
	
		stu=Student.objects.all()
		serializer=StudentSeralizer(stu,many=True)
		return Response(serializer.data)

	if request.method == 'POST':
		serializer=StudentSeralizer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'this is a post method'})
		return Response(serializer.errors)
	if request.method == 'PUT':
		id= pk
		# id= request.data.get('id')
		stu=Student.objects.get(pk=id)
		serializer=StudentSeralizer(stu,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'this is a put method'})
		return Response(serializer.errors)	
	if request.method == 'PATCH':
		id= pk
		# id= request.data.get('id')
		stu=Student.objects.get(pk=id)
		serializer=StudentSeralizer(stu,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'this is a patch method'})
		return Response(serializer.errors)	
	if request.method == 'DELETE':
		id= pk
		# id= request.data.get('id')
		stu=Student.objects.get(pk=id)
		stu.delete()
		return Response({'msg':'this is a delete method'})


"""





