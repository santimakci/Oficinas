from django.shortcuts import render

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Models
from oficinas.models import Office
#Serializers
from oficinas.serializers import (OfficeModelSerializer, OfficeSerializer)

class OfficeViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = OfficeModelSerializer

    def retrieve(self, request, pk=None):
        
        queryset = Office.objects.filter(id=int(pk))
        #import code; code.interact(local=dict(globals(), **locals()))
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = OfficeModelSerializer(queryset, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)   

    def get_queryset(self):
        offices_filtered = Office.objects.all()
        return offices_filtered   