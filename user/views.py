from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer, LogoutSerializer, SignupSerializer, UserListSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

# Create your views here.

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username=serializer.validated_data.get('username')
        password=serializer.validated_data.get('password')

        try:
            User=user.objects.get(username=username)
        except user.DoesNotExist:
            return Response({"message":"Invalid credential"}, status=401)
        
        if not User.check_password(password):
            return Response({"message":"Invalid credential"}, status=401)
        
        token, created=Token.objects.get_or_create(user=User)
        
        return Response({'message':"Login Successful","token":token.key})
        
        
class LogoutView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        token_from_user=serializer.validated_data.get("token")
        try:
            token=Token.objects.get(key=token_from_user)
            token.delete()
            return Response ({"message":"Logout Successful"}, status=200)
        
        except Token.DoesNotExist:
            return Response({"message":"Logout Successful"}, status=400)
        


class Signup(CreateAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=user.objects.all()
    serializer_class=SignupSerializer
    
class UserListView(ListAPIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    
    queryset=user.objects.all()
    serializer_class=UserListSerializer
    
class UserUpdateView(UpdateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    queryset=user.objects.all()
    serializer_class=UserListSerializer
       
    
class UserDeleteView(DestroyAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    queryset=user.objects.all()
    

class UserRetrieveView(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    queryset=user.objects.all()
    serializer_class=UserListSerializer
       

    
    
    
        
        
        