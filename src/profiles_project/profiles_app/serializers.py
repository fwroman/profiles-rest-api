# IMPORTS DIFFERENT KIND OF SERIALIZERS THAT DJANGO-REST-FRAMEWORK USES
from rest_framework import serializers


class helloSerializer(serializers.Serializer):
    """
    SERIALIZERS A NAME FIELD FOR TESTING OUR APIVIEW.
    """
    name = serializers.CharField(max_length=10)
