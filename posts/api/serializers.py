from rest_framework import serializers

from posts.models import Post 

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
data = {
    "title" : "hi, there",
    "slug": "new-content",
    "publish": "2018-02-02"
}

new_item = PostSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print new_item.errors
"""