from django.shortcuts import render

# Django REST Framework
from rest_framework import mixins, status, viewsets 
from rest_framework.response import Response

from rest_framework.decorators import action

# Models
from reserves.models import Reserve
#Serializers
from reserves.serializers import (ReserveModelSerializer, ReserveSerializer)

class ReserveViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = ReserveModelSerializer

    def get_queryset(self):
        res = Reserve.objects.all()
        return res  

        
    def create(self, request, *args, **kwargs):
        serializer = ReserveSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        res = serializer.save()
        data = ReserveModelSerializer(res).data
        return Response(data, status=status.HTTP_201_CREATED)            

    @action(detail=True)
    def get_last_reserves(self, request, pk=None ):
        queryset = Reserve.objects.filter(office_id=int(pk)).order_by('-id')[:20]
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ReserveModelSerializer(queryset, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)  
