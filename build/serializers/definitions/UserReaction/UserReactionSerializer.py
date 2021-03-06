from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
from fb_post.build.serializers.definitions.User.UserSerializer import UserType
from fb_post.build.serializers.definitions.UserReaction.UserReaction.Schema1.Schema1Serializer import Schema1Serializer
from fb_post.build.serializers.definitions.UserReaction.UserReaction.Schema1.Schema1Serializer import Schema1Type

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize

class UserReactionType(UserType, Schema1Type):
    def __init__(self, **validated_data):
        UserType.__init__(self, **validated_data)
        Schema1Type.__init__(self, **validated_data)
        

class UserReactionSerializer(UserSerializer, Schema1Serializer):
    def create(self, validated_data):
        
        userSerializer, _ = deserialize(UserSerializer, validated_data, many=False, partial=True)
        validated_data.update(userSerializer.__dict__)
        
        schema1Serializer, _ = deserialize(Schema1Serializer, validated_data, many=False, partial=True)
        validated_data.update(schema1Serializer.__dict__)
        
        return UserReactionType(**validated_data)
