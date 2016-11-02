from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=254)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
