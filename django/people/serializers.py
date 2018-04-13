from django.contrib.auth.models import User
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Type, Person


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("last_login", "first_name", "last_name", "email")

class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = "__all__"


class PersonSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    user = UserSerializer()

    class Meta:
        model = Person
        fields = "__all__"

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        instance = super().update(instance, validated_data)
        instance.user.first_name = user_data["first_name"]
        instance.user.last_name = user_data["last_name"]
        instance.user.email = user_data["email"]

        return instance

