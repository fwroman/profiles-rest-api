from django.shortcuts import render

# VIEWS TO DO CRUD OPERATIONS TO DATABASE:
from rest_framework import viewsets

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


class helloViewSet(viewsets.ViewSet):
    """
    TEST API VIEWSETS
    """

    serializer_class = serializers.helloSerializer

    def list(self, request):
        """
        RETURN A HELLO MESSAGE.
        """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            "Automatically maps to URL's using Routers",
            "Providers more functionality with less code.",
        ]

        return Response({"message": "Hello", "a_viewset": a_viewset})

    def create(self, request):
        """
        CREATE A NEW HELLO MESSAGE
        """

        serializer = serializers.helloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = "Hello {}".format(name)

            return Response({"message": message})

        return Response({"errors": [serializer.errors]}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        HANDLE GETTING AN OBJECT BY ITS ID.
        """

        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """
        HANDLES UPDATING AN OBJECT
        """

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """
        HANDLES UPDATING PART OF AN OBJECT
        """

        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """
        HANDLES REMOVING AN OBJECT.
        """

        return Response({"http_method": "delete"})
