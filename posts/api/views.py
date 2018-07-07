from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )

from posts.models import Post 
from posts.api.serializers import (
    PostListSerializer, 
    PostDetailSerializer, 
    PostCreateUpdateSerializer
    )
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"
    # lookup_url_kwarg = "slugurl"

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = "slug"

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"