from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ['id','name', 'description' , 'price' , 'category' , 'tags']
        fields = '__all__'
        depth = 1

class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'