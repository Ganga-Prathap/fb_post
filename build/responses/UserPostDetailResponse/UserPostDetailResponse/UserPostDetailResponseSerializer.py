from rest_framework import serializers
from fb_post.build.serializers.definitions.Post.PostSerializer import PostSerializer

class UserPostDetailResponseSerializer(serializers.ListSerializer):
    child = PostSerializer()
