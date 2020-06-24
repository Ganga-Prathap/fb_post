from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class PostType(object):
    def __init__(self, post_id, posted_by, posted_at, post_content, reactions, comments, comments_count,  **kwargs):
        self.post_id = post_id
        self.posted_by = posted_by
        self.posted_at = posted_at
        self.post_content = post_content
        self.reactions = reactions
        self.comments = comments
        self.comments_count = comments_count

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class PostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
    posted_by = UserSerializer(allow_null=True)
    posted_at = serializers.CharField()
    post_content = serializers.CharField()
    from fb_post.build.serializers.definitions.Reactions.ReactionsSerializer import ReactionsSerializer
    reactions = ReactionsSerializer(allow_null=True)
    from fb_post.build.serializers.definitions.Comments.CommentsSerializer import CommentsSerializer
    comments = CommentsSerializer(many=True)
    comments_count = serializers.IntegerField()

    def create(self, validated_data):
        from fb_post.build.serializers.definitions.User.UserSerializer import UserSerializer
        posted_by_val, _ = deserialize(UserSerializer, validated_data.pop("posted_by", None), many=False, partial=True)
        
        from fb_post.build.serializers.definitions.Reactions.ReactionsSerializer import ReactionsSerializer
        reactions_val, _ = deserialize(ReactionsSerializer, validated_data.pop("reactions", None), many=False, partial=True)
        
        from fb_post.build.serializers.definitions.Comments.CommentsSerializer import CommentsSerializer
        comments_val = []
        comments_list_val = validated_data.pop("comments", [])
        for each_data in comments_list_val:
            each_obj, _ = deserialize(CommentsSerializer, each_data, many=False, partial=True)
            comments_val.append(each_obj)
        
        return PostType(posted_by=posted_by_val, reactions=reactions_val, comments=comments_val, **validated_data)
