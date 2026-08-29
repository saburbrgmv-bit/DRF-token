from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Crud'],  summary='List Create')
class BlogListCraeteView(generics.ListCreateAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer

@extend_schema(tags=['Crud'],  summary='Delete Update')
class BlogUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

   queryset = Blog.objects.all()
   serializer_class = BlogSerializer
