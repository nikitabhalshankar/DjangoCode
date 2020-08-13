from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from product import models
from.serializers import ProductSerializer

# Create your views herz
class ListProduct(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class=ProductSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = models.Product.objects.all()
#     serializer_class = ProductSerializer
