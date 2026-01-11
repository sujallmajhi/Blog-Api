from rest_framework.response import Response
from .serializers import CategorySerializer,BlogSerializer,CommentSerializer
from rest_framework import viewsets
from blogs.models import Category,Blog,Comment
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .customfilter import BlogFilter
from .permissions import IsAdminOrReadOnly
from rest_framework import authentication

'''Category ViewSet'''
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    pagination_class=PageNumberPagination
    filter_backends=[filters.SearchFilter]
    search_fields=["category_name",]
    permission_classes=[IsAdminOrReadOnly]
    authentication_classes=[authentication.TokenAuthentication]
'''Blog Viewset'''
class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    pagination_class=PageNumberPagination
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    filterset_class=BlogFilter
    search_fields=['title',"category__category_name","author__username",]
    permission_classes=[IsAdminOrReadOnly]
    authentication_classes=[authentication.TokenAuthentication]
    '''Comment Viewset'''
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    pagination_class=PageNumberPagination
    filter_backends=[filters.SearchFilter]
    search_fields=['comment',]
    permission_classes=[IsAdminOrReadOnly]
    authentication_classes=[authentication.TokenAuthentication]