from django.urls import path
from rest_framework.routers import DefaultRouter
from .api_views import CategoryViewSet, BlogViewSet, CommentViewSet

"""Registering CategoryViewSet,BlogViewSet and CommentViewSeT"""
router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'Blog', BlogViewSet)
router.register(r'Comment', CommentViewSet)

urlpatterns = [  
 
]
urlpatterns += router.urls