from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView
    )

from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from .permissions import IsOwnerReadonly

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
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"
    # lookup_url_kwarg = "slugurl"

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = "slug"
    permission_classes = [IsOwnerReadonly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"