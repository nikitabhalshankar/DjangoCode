from django.db import models
from company.models import Company

# Create your models here.
class Product(models.Model):
    productName=models.CharField(max_length=20)
    companyName=models.ForeignKey(Company,on_delete=models.PROTECT)

    def __str__(self):
        return self.productName
