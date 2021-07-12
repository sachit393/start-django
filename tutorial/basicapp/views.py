from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student, Organizer
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, OrganizerSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class EditPermission(BasePermission):
    message = 'You need to login to modify your credentials'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:# safe methos -> read only type permissions
            return True
# object refers to the object whose detail view api will be avilible
# user refers to the request.object who has sent the request(currentlyloggedin)
        if str(obj.username) == str(request.user):
            print("HAHAH")
            return True
        else:
            print("NO")
            return False


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView, EditPermission):
    permission_classes = [EditPermission]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

######################################################


class OrganizerList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


class OrganizerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [EditPermission]
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
