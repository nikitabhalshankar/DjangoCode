from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from company import models
from.serializers import CompanySerializer

#Create your views herz
class ListCompany(generics.ListCreateAPIView):
    queryset=models.Company.objects.all()
    serializer_class=CompanySerializer


class DetailCompany(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Company.objects.all()
    serializer_class=CompanySerializer

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = models.Company.objects.all()
#     serializer_class = CompanySerializer
