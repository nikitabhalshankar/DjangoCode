from django.db import models
from company.models import Company

# Create your models here.
class Product(models.Model):
    productName=models.CharField(max_length=20)
    companyName=models.ForeignKey(Company,on_delete=models.PROTECT)
    cost=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.productName

class PurchaseOrder(models.Model):
    def po_auto_id():
        now=datetime.datetime.now()
        last_entry=PurchaseOrder.objects.all()[PurchaseOrder.objects.counts()-1]
        last_entry_id=last_entry_po
        last_entry_seprated=last_entry_id.split("/")

        if now.day==1 and now.month==1 and now.year==int(last_entry_seprated[1]):
            return "po"/+str(now.year)+"/"+str(1)
        else:
            if last_entry==None:
                return "PO"+str(now.year)+"/"+str(1)
            else:
                str(int(last_entry_seprated[2])+1)

    po=models.CharField(max_length=6,default=po_auto_id, unique=True)
    companyName=models.ForeignKey(Company,on_delete=models.PROTECT)
    productName=models.ForeignKey(Product,on_delete=models.PROTECT)
    rate=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def totalPrice():
        return rate*quantity

    totalPrice = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
