from rest_framework import serializers
from .models import Student, Organizer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Please type in your password',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Student
        fields = ['username', 'password', 'email', 'college', 'cgpa', 'description', 'cv', 'college','phone_no', 'id', 'department', 'year', 'degree']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(username=validated_data.get('username'), password=validated_data.get('password'),)
        validated_data['user']=user
        return super(StudentSerializer, self).create(validated_data)


    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        instance.username = validated_data['username']
        instance.password = validated_data['password']
        instance.email = validated_data['email']
        instance.college = validated_data['college']
        instance.cgpa = validated_data['cgpa']
        instance.description = validated_data['description']
        instance.cv = validated_data['cv']
        instance.phone_no = validated_data['phone_no']
        instance.department = validated_data['department']
        instance.year = validated_data['year']
        instance.degree = validated_data['degree']
        instance.save()
        user = instance.user
        user.password = validated_data['password']
        user.username = validated_data['username']
        user.save()
        return instance


class OrganizerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Please type in your password',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Organizer
        fields = ['username', 'password', 'description', 'contact', 'id']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(username=validated_data.get('username'), password=validated_data.get('password'),)
        validated_data['user']=user
        return super(OrganizerSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        instance.username = validated_data['username']
        instance.password = validated_data['password']
        instance.description = validated_data['description']
        instance.contact = validated_data['contact']
        instance.save()
        user = instance.user
        user.password = validated_data['password']
        user.username = validated_data['username']
        user.save()
        return instance


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    # class Meta:
    #     fields = ['name', 'password']
