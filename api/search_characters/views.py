from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models

class GetUsers(APIView):

  def get(self, request, format=None):
        """Get all Users"""
        try:
            users = models.User.objects.all().values()

            return Response({'data': list(users)})
        except Exception as exception:
            print(exception)
            return Response({'error': str(exception)})

class UserSearch(APIView):

  def get(self, request, **kwargs):
        """Search for a User"""
        try:
            users = models.User.objects.all().values()

            return Response({'data': list(users)})
        except Exception as exception:
            print(exception)
            return Response({'error': str(exception)})