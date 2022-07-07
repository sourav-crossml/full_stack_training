from dataclasses import fields
from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer
    """
    class Meta:
        """
        meta class
        """
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    """
    Category serializer
    """
    class Meta:
        """
        meta class
        """
        model = Product
        fields = "__all__"
