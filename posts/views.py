from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import PostSerializer
from .models import Post


@api_view(['GET'])
def posts_listing(request: Request):
    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts, many=True)
    print(serializer)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def post_detail(request: Request, pid: int):
    post = get_object_or_404(Post, id=pid)
    serializer = PostSerializer(instance=post)
    if serializer.is_valid():
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_post(request: Request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_post(request: Request, pid: int):
    post = get_object_or_404(Post, id=pid)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_post(request: Request, pid: int):
    post = get_object_or_404(Post, id=pid)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
