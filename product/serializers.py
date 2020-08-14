from rest_framework import serializers
from product.models import Product
from product.models import PurchaseOrder
from company.serializers import CompanySerializer



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','productName','companyName']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        company=CompanySerializer()
        product=ProductSerializer(read_only=True)
        fields=['id','po','companyName','productname','quantity','totalPrice']
