from rest_framework import serializers # pyright: ignore[reportMissingImports]
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'