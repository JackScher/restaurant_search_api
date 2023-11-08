from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = Employee
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(EmployeeSerializer, self).create(validated_data)
