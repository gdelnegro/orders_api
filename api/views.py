from django.shortcuts import render
from rest_framework import viewsets, filters, views, status
from rest_framework.response import Response
from api.serializers import *
from rest_framework.decorators import detail_route


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'company', 'status')


# Create your views here.
