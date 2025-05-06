from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
