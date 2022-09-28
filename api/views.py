from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions,authentication
from Owner.models import Categories,Products
from api.serializers import CategoriesSerializer, ProductSerializer
from rest_framework.decorators import action


# Create your views here.

class CategoriesView(ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     serializer = CategoriesSerializer(data=request.data) #context={"user": request.user})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)

class ProductsView(ModelViewSet):
    serializer_class= ProductSerializer
    queryset = Products.objects.all()
    # authentication_classes = [authentication.BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    @action(methods=["post"], detail=True)
    def add_product(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        user = request.user
        serializer = CategoriesSerializer(data=request.data, context={"user": user, "product": product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

