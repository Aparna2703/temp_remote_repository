from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quizapiapp.models import Employee1
from .serializers import EmployeesSerializer

# Create your views here.
class EmployeeList(APIView):
    def get(self,request):
        employee1=Employee1.objects.all()
        serializers2=EmployeesSerializer(employee1,many=True)
        return Response(serializers2.data)
    def post(self):
        pass
