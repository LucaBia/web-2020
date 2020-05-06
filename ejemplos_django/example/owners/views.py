from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from owners.models import Owner
from owners.serializers import OwnerSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer 