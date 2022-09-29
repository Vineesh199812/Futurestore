from django.contrib.auth.models import User
from rest_framework import serializers
from Owner.models import Categories,Products



class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        return Categories.objects.create(**validated_data,user=user)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Products.objects.create(author=user,product=product,**validated_data)