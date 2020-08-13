from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=200)
    gst= models.TextField()

    def __str__(self):
        return self.name
