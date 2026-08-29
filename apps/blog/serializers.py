from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ['title', 'bio']
    only_read = ['create_at']
    