from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')

    def create(self, validated_data):
        print("Create Method")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("Update Method")
        print("self: ", self)
        return super().update(instance, validated_data)
