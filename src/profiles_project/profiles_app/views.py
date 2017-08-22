from django.shortcuts import render

# IMPORTING API VIEW FROM DJANGO-REST-FRAMEWORK:
from rest_framework.views import APIView
# STANDARD RESPONSE OBJECT WE RETURN FROM THIS VIEW:
from rest_framework.response import Response

from rest_framework import status

# IMPORTING SERIALIZERS CLASS
from . import serializers

# Create your views here.


class helloApiView(APIView):
    """
    THE API VIEW
    """

    serializer_class = serializers.helloSerializer

    def get(self, request, format=None):
        """
        RETURNS A LIST OF APIView FEATURES.
        """

        an_apiview = [
            'Uses HTTP methods as functions(get, post, patch, put, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your ligic',
            'It rapped manually to URLS',
        ]

        my_dic = {'message': 'Hello', 'an_apiview': an_apiview}
        return Response(my_dic)

    def post(self, request):
        """
        CREATES A HELLO MESSAGE WITH OUR NAME
        """

        serializer = serializers.helloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = "Hello {}".format(name)

            return Response({"message": message})

        return Response({"errors": [serializer.errors]}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        HANDLES UPDATING AN OBJECT
        """

        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """
        PATCH REQUEST, ONLY UPDATES FIELDS PROVIDED IN THE REQUEST.
        """

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """
        DELETE AN OBJECT.
        """

        return Response({'method': 'delete'})
