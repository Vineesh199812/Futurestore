from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions,authentication
from Owner.models import *
from api.serializers import *
from rest_framework.decorators import action

class UserRegistrationView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CategoriesView(ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()


    def perform_create(self, serializer):
        return serializer.save()

    @action(methods=["get"], detail=True)
    def get_product(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        category = Categories.objects.get(id=id)
        product = category.products_set.all()
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)

    @action(methods=["post"], detail=True)
    def add_product(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        category = Categories.objects.get(id=id)
        serializer = ProductSerializer(data=request.data, context={"category": category})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductsView(ModelViewSet):
    serializer_class= ProductSerializer
    queryset = Products.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return Products.objects.filter(user=self.request.user)
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = CategorySerializer(data=request.data, context={"user": request.user})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)

    @action(methods=["post"], detail=True)
    def add_to_cart(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        serializer = CartSerializer(data=request.data, context={"user": user, "product": product})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    @action(methods=["post"], detail=True)
    def add_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        user = request.user
        serializer = ReviewSerializer(data=request.data, context={"user": user, "product": product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["get"], detail=True)
    def get_review(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        reviews = product.reviews_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    @action(methods=["post"], detail=True)
    def order(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get("pk")
        product= Products.objects.get(id=id)
        serializer = OrderSerializer(data=request.data, context={"user": user, "product": product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class CartsView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

#usernames : angular, vineesh
#superusers : xyz
#password :Password@123