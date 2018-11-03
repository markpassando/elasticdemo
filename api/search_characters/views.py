import json
from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from elasticsearch import Elasticsearch

from . import models


class GetUsers(APIView):

    def get(self, request, format=None):
        """Get all Users"""
        try:
            users = models.User.objects.all().values()

            return Response({'data': list(users)})
        except Exception as exception:
            print(exception)
            return Response({'error': str(exception)})


class UserSearch(APIView):

    def get(self, request, **kwargs):
        """Search for a User"""
        try:
            # users = models.User.objects.all().values()
            # Get user
            user = models.User.objects.get(name="foo")

            # Get index_list permissions
            index_list = list(
                user.index_list.values_list(
                    'name', flat=True))

            # Connects to localhost:9200 by default
            es = Elasticsearch()
            # hard code for now
            es_query = es.search(index=index_list, doc_type="character", body={
                                 "query": {"match": {"first_name": "fred"}}})

            es_query = es_query['hits']['hits']

            return_data = {"results": []}
            for hit in es_query:
                character = {
                    "id": hit['_id'],
                    "full_name": f"{hit['_source']['first_name']} {hit['_source']['last_name']}",
                    "location": hit['_source']['location']}
                return_data['results'].append(character)

            return Response(return_data)
        except Exception as exception:
            print(exception)
            return Response({'error': str(exception)})
