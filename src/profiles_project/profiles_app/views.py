from django.shortcuts import render

# IMPORTING API VIEW FROM DJANGO-REST-FRAMEWORK:
from rest_framework.views import APIView
# STANDARD RESPONSE OBJECT WE RETURN FROM THIS VIEW:
from rest_framework.response import Response

# Create your views here.


class helloApiView(APIView):
    """
    THE API VIEW
    """

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
