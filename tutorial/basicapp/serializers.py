from rest_framework import serializers
from .models import Student, Organizer
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
        fields = ['name', 'password', 'college', 'cgpa', 'description', 'cv', 'college','phone_no', 'qualification', 'id']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(StudentSerializer, self).create(validated_data)

    def update(self,instance, validated_data):
        instance.password = make_password(validated_data.get('password',instance.password))
        instance.save()
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
        fields = ['name', 'password', 'description', 'contact', 'id']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(OrganizerSerializer, self).create(validated_data)

    def update(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(StudentSerializer, self).update(validated_data)


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    # class Meta:
    #     fields = ['name', 'password']
