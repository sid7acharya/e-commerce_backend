from rest_framework import serializers
from .models import Cart

class CartCreateSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField(many=True)
    user=serializers.StringRelatedField()
    
    class Meta:
        model=Cart
        fields='__all__'
        
    def create(self, validated_data):
        product=validated_data.get('product',None)
        user=validated_data.get('user',None)
        quantity=validated_data.get('quantity',None)
        
        seller=validated_data.get('seller',None)
        cart=Cart.objects.create(
            product=product,
            user=user,
            quantity=quantity
        )
        
        return cart
    
    
class CartListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Cart
        fields='__all__'
         
         
        
         
            
            
    

    


