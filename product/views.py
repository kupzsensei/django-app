from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer , ProductPostSerializer
from .models import Product

# Create your views here.
class ProductView(APIView):

    def get(self , request): # READ       
        products = Product.objects.all() # get all products
        serializer = ProductSerializer(products , many=True)
        return Response(serializer.data)

    def post(self , request): # CREATE
        data = request.data
        serializer = ProductPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True , "detail": 'Product Created' , "data":serializer.data})
        return Response({"ok": False , "detail": serializer.errors})
    
    def patch(self , request): # UPDATE
        data = request.data
        try:
            product_instance = Product.objects.get(id=data['id'])
            serializer = ProductPostSerializer(product_instance, data=data , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"ok": True , "detail": "update success" , "data": serializer.data})
            return Response({"ok": False , "detail": serializer.errors})
        except:
            return Response({"ok":False , "detail": "Product does not exist."})

    def delete(self , request): # DELETE
        try:
            product_instance = Product.objects.get(id=request.data['id'])
            product_instance.delete()
            return Response({"ok": True , "detail": "Product Deleted."})
        except Product.DoesNotExist:
           return Response({"ok":False , "detail": "Product does not exist."})


