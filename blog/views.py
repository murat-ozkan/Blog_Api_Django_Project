from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .serializers import (
    Category, CategorySerializer, 
    Post, PostSerializer
    )

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    