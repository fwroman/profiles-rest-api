from django.shortcuts import render

# VIEWS TO DO CRUD OPERATIONS TO DATABASE:
from rest_framework import viewsets
# IMPORTING API VIEW FROM DJANGO-REST-FRAMEWORK:
from rest_framework.views import APIView
# STANDARD RESPONSE OBJECT WE RETURN FROM THIS VIEW:
from rest_framework.response import Response

from rest_framework import status
# THIS IS USED TO ALLOW ONLY AUTHENTICATED USERS UPDATE OR DELETE INFORMATION:
from rest_framework.authentication import TokenAuthentication
# THIS IS USED TO SEARCH USERS BY A FILTER
from rest_framework import filters
# THIS IS USED TO LOGIN USERS:
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# THIS IS USED TO ALLOW USERS TO UPDATE INFORMATION IF THEY'RE LOGGED OR RESTRICT
# THEM TO READ INFORMATION ONLY
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# THIS IS USED TO ALLOW USERS TO UPDATE OR READ INFORMATION IF THEY'RE LOGGED OR RESTRICT
# THEM IF NOT
from rest_framework.permissions import IsAuthenticated

# IMPORTING SERIALIZERS CLASS
from . import serializers
from . import models
from . import permissions

# Create your views here.


class HelloApiView(APIView):
    """
    THE API VIEW
    """

    serializer_class = serializers.HelloSerializer

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

        serializer = serializers.HelloSerializer(data=request.data)

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


class HelloViewSet(viewsets.ViewSet):
    """
    TEST API VIEWSETS
    """

    serializer_class = serializers.HelloSerializer

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

        serializer = serializers.HelloSerializer(data=request.data)

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


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    HANDLES CREATING, RETRIEVEING AND UPDATING PROFILES.
    """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """
    CHECKS email AND password AND RETURNS AN AUTH TOKEN
    """
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """
        USE THE ObtainAuthToken APIView TO VALIDATE AND CREATE A TOKEN.
        """
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    HANDLES CREATING, READING AND UPDATING PROFILE FEED ITEMS
    """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    # permission_classes = (permissions.PostOnStatus, IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.PostOnStatus, IsAuthenticated,)

    def perform_create(self, serializer):
        """
        SETS THE USER PROFILE TO THE LOGGED IN USER
        """

        serializer.save(user_profile=self.request.user)
