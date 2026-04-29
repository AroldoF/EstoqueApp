from django.db import models
import uuid
class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=7)
    user_id = models.CharField()
    description = models.TextField()
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    