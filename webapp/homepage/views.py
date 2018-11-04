from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        # Query API if a Query is submitted
        if 'q' in request.GET:
            first_name_query = request.GET['q']

            result = requests.get(f"http://127.0.0.1:80/api/users/foo/?first_name={first_name_query}").text
            context['characters'] = json.loads(result)
    

        return render(request, self.template_name, context)