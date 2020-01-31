from rest_framework import serializers
from quizapiapp.models import Employee1

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee1
        fields = '__all__'