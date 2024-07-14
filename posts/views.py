
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import PostSerializer
from .models import Post
from rest_framework.views import APIView


class CreateListPostsView(APIView):
    """
    Create a new post or list all posts
    """
    serializer_class = PostSerializer

    def get(self, request: Request):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagePostView(APIView):
    """
    Retrieve, update or delete a post instance
    """
    serializer_class = PostSerializer

    @staticmethod
    def get_post(pid: int):
        return get_object_or_404(Post, pk=pid)

    def get(self, request: Request, pid: int):
        post = self.get_post(pid)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pid: int):
        post = self.get_post(pid)
        serializer = self.serializer_class(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pid: int):
        post = self.get_post(pid)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
