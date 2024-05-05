from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from category.models import Category
from rest_framework import exceptions

from .models import Product
from .serializers import ProductListSerializer , ProductCreateSerializer

# Create your views here.

class ProductCreateView(CreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Product.objects.all()
    serializer_class=ProductCreateSerializer
    
class ProductListView(ListAPIView):
    
    queryset=Category.objects.all()
    serializer_class=ProductListSerializer
    
class ProductUpdateView(UpdateAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer
    
class ProductDestroyView(DestroyAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset=Product.objects.all()
    
    
class ProductRetrieveView(RetrieveAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer
    

class ProductByCategory(ListAPIView):
    serializer_class=ProductListSerializer
    queryset=Product.objects.all()
    
    def get_queryset(self):
        category_name=self.kwargs['name']
        try:
            Category= Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            raise exceptions.APIException("Category not found")
        
        queryset= Product.objects.filter(category=Category)
        return queryset
    
