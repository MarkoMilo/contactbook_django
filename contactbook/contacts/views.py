from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *


class PersonViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Person.objects.all()