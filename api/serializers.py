from rest_framework import serializers
from blogs.models import Category,Blog,Comment


'''Category Serializer'''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
"""BlogSerializer"""
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"
    
'''Comment Serializer'''
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"