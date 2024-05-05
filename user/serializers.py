from rest_framework import serializers
from .models import user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    
class LogoutSerializer(serializers.Serializer):
    token=serializers.CharField(required=True)
    
class SignupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=user
        fields=["username","password", "email"]
        
    def create(self, validated_data):
        username= validated_data.get('username',None)
        password=validated_data.get('password',None)
        email=validated_data.get('email',None)
        user=user.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return user
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model= user
        fields=['username',]
