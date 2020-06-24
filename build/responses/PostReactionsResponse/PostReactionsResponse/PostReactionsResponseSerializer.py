from rest_framework import serializers
from fb_post.build.serializers.definitions.UserReaction.UserReactionSerializer import UserReactionSerializer

class PostReactionsResponseSerializer(serializers.ListSerializer):
    child = UserReactionSerializer()
