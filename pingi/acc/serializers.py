from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)


class NowSerializer(serializers.Serializer):
    now = serializers.DateTimeField()


class StatsSerializer(serializers.Serializer):
    user = serializers.CharField()
    open_count = serializers.IntegerField()