from django.shortcuts import render
from rest_framework import viewsets
from owners.models import Owner
from owners.serializers import OwnerSerializer
from permissions.services import APIPermissionClassFactory

# Create your views here.
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer 
    # permisos
    permission_classes = (
         APIPermissionClassFactory(
             name='OwnerPermission',
             permission_configuration={
                 'base': {
                     'create': True,
                     'list': True,
                 },
                 'instance': {
                     'retrieve': True,
                     'destroy': True,
                     'update': True,
                     'partial_update': True,
                 }
             }
         ),
     ) 