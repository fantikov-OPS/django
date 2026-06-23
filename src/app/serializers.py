from rest_framework import serializers
from app.models import Comment, Product


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'firstname', 'lastname', 'age', 'text')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity', 'comment')

class ProductSerializerV2(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity', 'comment')
    
    def get_name(self, obj):
        return f'{obj} + test'