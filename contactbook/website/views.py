from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from contacts.models import *


def welcome(request):
    return HttpResponse("Dobrodosli u meeting planner")


class PersonViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    # query = Person.queryset.ob
    queryset = Person.objects.all()
