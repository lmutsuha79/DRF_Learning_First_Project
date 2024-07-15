from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import PostSerializer
from .models import Post
from rest_framework import mixins, generics

"""

Memory updated
Great! Understanding DRF's generic views and mixins can significantly streamline your API development process. Here's an overview to get you started:

Generic Views
Django REST Framework (DRF) provides a set of generic views that are designed to handle the common patterns in building APIs. These views abstract the repetitive code into reusable components.

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
These views help you avoid writing boilerplate code. For example, instead of manually creating a view for listing and creating objects, you can use ListCreateAPIView.

Example
Here is an example of how to use ListCreateAPIView for a Product model:

python
Copy code
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
Mixins
Mixins provide a way to compose views by combining reusable behaviors. DRF includes several mixins that you can use to build your views.

Common Mixins
CreateModelMixin: Adds create functionality.
ListModelMixin: Adds list functionality.
RetrieveModelMixin: Adds retrieve functionality.
UpdateModelMixin: Adds update functionality.
DestroyModelMixin: Adds destroy functionality.

You can combine these mixins with DRF's generic views to customize the behavior of your API.
"""


class CreateListPostsView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ManagePostView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
