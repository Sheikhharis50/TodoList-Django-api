from django.urls import path, include
from django.contrib.auth.models import User
from .models import *
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class todoSerializer(serializers.ModelSerializer):
    """
    todo Serializer
    """
    class Meta:
        model = todo
        fields = ['id', 'title', 'completed', 'created']
