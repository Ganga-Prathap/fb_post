from rest_framework import serializers


class PostIdsResponseSerializer(serializers.ListSerializer):
    child = serializers.IntegerField()
