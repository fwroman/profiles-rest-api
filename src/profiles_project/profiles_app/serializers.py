# IMPORTS DIFFERENT KIND OF SERIALIZERS THAT DJANGO-REST-FRAMEWORK USES
from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """
    SERIALIZERS A NAME FIELD FOR TESTING OUR APIVIEW.
    """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """
    A SERIALIZER FOR OUR USER PROFILE OBJECTS.
    """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        CREATE AND RETURN A NEW USER.
        """
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """
    A SERIALIZER FOR PROFILE FEED ITEMS.
    """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')

        extra_kwargs = {'user_profile': {'read_only': True}}
