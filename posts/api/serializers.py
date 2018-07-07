from rest_framework import serializers

from posts.models import Post 

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            # "slug",
            "publish"
        ]

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "publish"
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "publish"
        ]

"""
from posts.models import Post
from posts.api.serializers import PostDetailSerializer

data = {
    "title" : "hi, there",
    "slug": "new-content-new",
    "publish": "2018-02-02"
}

obj = Post.objects.get(id=3)
new_item = PostDetailSerializer(obj, data=data)
# new_item = PostSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print new_item.errors
"""