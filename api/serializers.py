from django.contrib.auth.models import User
from rest_framework import serializers
from Owner.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "email",
            "password",
            "username"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Categories
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields="__all__"

    def create(self, validated_data):
        category=self.context.get("category")
        return Products.objects.create(category=category,**validated_data)

class CartSerializer(serializers.ModelSerializer):
    product = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    created_date = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields="__all__"

    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(**validated_data,user=user,product=product)


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Reviews.objects.create(user=user,product=product,**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    product=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    expected_delivery_date=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=[
            "user",
            "product",
            "created_date",
            "status",
            "delivery_address",
            "expected_delivery_date"
        ]
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Orders.objects.create(user=user,product=product,**validated_data)