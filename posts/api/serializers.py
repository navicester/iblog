from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField

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

post_detail_url = HyperlinkedIdentityField(
    view_name = "posts-api:detail",
    lookup_field = "slug",
    )

post_delete_url = HyperlinkedIdentityField(
    view_name = "posts-api:delete",
    lookup_field = "slug",
    )

class PostListSerializer(serializers.ModelSerializer):
    url = post_detail_url
    delete_url = post_delete_url
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            # "slug",
            "publish",
            "user",
            "delete_url"
        ]

    def get_user(self, obj):
        return str(obj.user.username)

class PostDetailSerializer(serializers.ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "slug",
            "publish",
            "user",
            "image",
            "content",
            "html"
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        if obj.image and obj.image.url:
            return obj.image.url
        return None

    def get_html(self, obj):
        return obj.get_markdown()

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