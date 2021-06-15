from django.db import models

# Create your models here.
class Product(models.Model):
    # product_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()