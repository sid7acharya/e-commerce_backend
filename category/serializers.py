from rest_framework import serializers
from .models import Category

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
    def create(self, validated_data):
        name=validated_data.get('name',None)
        
        category=Category.objects.create(
            name=name,
        )
        return category