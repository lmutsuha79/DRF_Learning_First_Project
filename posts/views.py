from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework import generics

"""
Common Generic Views
CreateAPIView: For creating new instances.
ListAPIView: For listing multiple instances.
RetrieveAPIView: For retrieving a single instance.
UpdateAPIView: For updating an existing instance.
DestroyAPIView: For deleting an instance.
ListCreateAPIView: Combines listing and creating instances.
RetrieveUpdateAPIView: Combines retrieving and updating instances.
RetrieveDestroyAPIView: Combines retrieving and deleting instances.
RetrieveUpdateDestroyAPIView: Combines retrieving, updating, and deleting instances.
"""


class CreateListPostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ManagePostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
