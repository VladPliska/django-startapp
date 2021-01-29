from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializer import UserSerializer
from .models import User


# Create your views here.
class UserView(APIView):
    @api_view(['GET'])
    def user(self):
        user = User.objects.all()
        serializer = UserSerializer(user)
        return HttpResponse(status=200, data=serializer.data)
