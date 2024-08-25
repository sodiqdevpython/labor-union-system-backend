from django.shortcuts import render
from .models import Application
from rest_framework.viewsets import ModelViewSet
from .serializers import ApplicationSerializer

class ApplicationView(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer