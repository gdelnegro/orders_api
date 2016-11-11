# -*- coding: utf-8 -*-
# Created by Gustavo Del Negro <gustavodelnegro@gmail.com> on 11/11/16.
from api.models import *
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    company = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    status = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

    class Meta:
        model = Order
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
