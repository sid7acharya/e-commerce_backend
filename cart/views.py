from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from rest_framework import exceptions

from .models import Cart
from .serializers import CartCreateSerializer, CartListSerializer

# Create your views here.

class CartCreateView(CreateAPIView):
    
    # authentication_classes=[IsAuthenticated]
    # permission_classes=[TokenAuthentication]
    
    queryset=Cart.objects.all()
    serializer_class=CartCreateSerializer
    
class CartListView(ListAPIView):
    
    authentication_classes=[IsAuthenticated]
    permission_classes=[TokenAuthentication]
    
    queryset=Cart.objects.all()
    serializer_class=CartListSerializer
    
class CartDeleteView(DestroyAPIView):
    
    authentication_classes=[IsAuthenticated]
    permission_classes=[TokenAuthentication]
    
    queryset=Cart.objects.all()
    serializer_class=CartListSerializer
    
class CartUpdateView(UpdateAPIView):
    
    authentication_classes=[IsAuthenticated]
    permission_classes=[TokenAuthentication]
    
    queryset=Cart.objects.all()
    serializer_class=CartListSerializer
    

class CartRetrieveView(RetrieveAPIView):
    
    authentication_classes=[IsAuthenticated]
    permission_classes=[TokenAuthentication]
    
    queryset=Cart.objects.all()
    serializer_class=CartListSerializer
    
    
    
