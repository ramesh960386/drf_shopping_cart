from ssl import create_default_context
from django.db import models
from users.models import CustomUser


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True)
