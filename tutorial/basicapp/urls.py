from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('students/', views.StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('organizations/', views.OrganizerList.as_view(), name='organizer_list'),
    path('organizations/<int:pk>', views.OrganizerDetail.as_view(), name='organizer_detail'),
    # path('students/login', views.login, name='login'),
]
