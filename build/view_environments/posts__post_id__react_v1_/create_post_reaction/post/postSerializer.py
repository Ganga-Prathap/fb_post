from rest_framework import serializers

from django_swagger_utils.drf_server.utils.decorator.deserialize import deserialize
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_object
from django_swagger_utils.drf_server.utils.server_gen.type_file_utils import get_type_list_object
from django_swagger_utils.drf_server.fields.collection_format_field import CollectionFormatField


class postType(object):
    def __init__(self, reaction_type,  **kwargs):
        self.reaction_type = reaction_type

    def __str__(self):
        from django_swagger_utils.drf_server.utils.server_gen.get_unicode_str import get_unicode_str
        return get_unicode_str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class postSerializer(serializers.Serializer):
    reaction_type = serializers.ChoiceField(choices=(('WOW', 'WOW'), ('LIT', 'LIT'), ('LOVE', 'LOVE'), ('HAHA', 'HAHA'), ('THUMBS-UP', 'THUMBS-UP'), ('THUMBS-DOWN', 'THUMBS-DOWN'), ('ANGRY', 'ANGRY'), ('SAD', 'SAD')))

    def create(self, validated_data):
        return postType(**validated_data)