from django.urls import include, path
from .views import *
from .models import *
from rest_framework import routers

urlpatterns = [
    path('todo', todoView.as_view()),
    path('todo/<int:id>/', todoDetailView.as_view()),
    path('testing', testing),
    path('ping', pingToDB),
]
