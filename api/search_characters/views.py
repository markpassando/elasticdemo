import json
from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from django.core.exceptions import ObjectDoesNotExist

from . import serializers, models


class GetUsers(APIView):

    def get(self, request, format=None):
        """Get all Users"""
        try:
            users = models.User.objects.all().values()

            return Response({'data': list(users)})
        except Exception as exception:
            print(exception)
            return Response({'error': str(exception)})


class CharacterSearch(APIView):
    serializers_class = serializers.CharacterSearchSerializer

    def get(self, request, **kwargs):
        """Search for a Character, requires a first_name"""
        try:
            print(f"INFO - Inside GET CharacterSearch View")
            serializer = self.serializers_class(
                data=request.query_params)

            if serializer.is_valid():
                validated_data = serializer.validated_data

                # Check for an authenticated user in the DB
                authenticated_user = kwargs['user']
                try:
                    user = models.User.objects.get(
                        name=authenticated_user)
                except ObjectDoesNotExist:
                    # Refactor Error Responses
                    print(
                        f"ERROR - User '{authenticated_user}' was not found in DB")
                    return Response(
                        {'error': f"User '{authenticated_user}' does not exist!"},
                        status=status.HTTP_403_FORBIDDEN)

                # Get index_list permissions
                index_list = list(
                    user.index_list.values_list(
                        'name', flat=True))

                # Connects to localhost:9200 by default
                es = Elasticsearch()
                # Validate connection
                if not es.ping():
                    print(f"ERROR - Could not reach Elasticsearch")
                    return Response(
                        {'error': 'Could not reach Elasticsearch'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                # Query Elasticsearch with the authenticated_user's
                # 'index_list' permissions and the 'first_name' query
                es_query = es.search(index=index_list, doc_type="docs", body={
                    "query": {"match": {"first_name": validated_data['first_name']}}})
                # NOTE: Nested hits
                es_query = es_query['hits']['hits']

                return_data = {"results": []}
                for hit in es_query:
                    character = {
                        "id": hit['_id'],
                        "full_name": f"{hit['_source']['first_name']} {hit['_source']['last_name']}",
                        "location": hit['_source']['location']}
                    return_data['results'].append(character)

                print(
                    f"INFO - Successfully returning data from GET CharacterSearch View")
                return Response(return_data)
            else:
                # Query serializer was not valid
                print(f"ERROR - Serializer was invalid")
                return Response(
                    {'error': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception as exception:
            print(exception)
            return Response({'error': str(exception)},
                            status=status.HTTP_400_BAD_REQUEST)
