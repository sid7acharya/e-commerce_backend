from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategoryListSerializer,CategoryCreateSerializer

class CategoryCreateView(CreateAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset=Category.objects.all()
    serializer_class=CategoryCreateSerializer
    
class CategoryListView(ListAPIView):
    
    queryset=Category.objects.all()
    serializer_class=CategoryListSerializer
    
class CategoryUpdateView(UpdateAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset=Category.objects.all()
    serializer_class=CategoryListSerializer
    
class CategoryDestroyView(DestroyAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset=Category.objects.all()
    
    
class CategoryRetrieveView(RetrieveAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    queryset=Category.objects.all()
    serializer_class=CategoryListSerializer
    



    
    