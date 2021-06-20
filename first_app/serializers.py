from rest_framework import serializers 
from .models import Products
from django.contrib.auth.models import User


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
