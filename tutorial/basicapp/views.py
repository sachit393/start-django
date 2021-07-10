from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student, Organizer
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, OrganizerSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class OrganizerList(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class OrganizerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

# @api_view(['POST','GET'])
# def login(request):
#     serializer = LoginSerializer(request.data)
#     if(request.method=='POST'):
#         serializer = LoginSerializer(request.data)
#
#         try :
#             student = Student.objects.get(name=serializer.data['name'])
#         except Student.DoesNotExist:
#             return HttpResponse(status=404)
#
#         if student.check_password(serializer.data['password']):
#             return HttpResponse(status=200)
#         else :
#             return HttpResponse(status=403)
#     elif request.method == 'GET':
#         students = Student.objects.all()
#         serializer = LoginSerializer(students, many=True)
#         return JsonResponse(serializer.data, safe=False)
