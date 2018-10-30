from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import csv
import json
from django.views.generic import TemplateView
from urllib.parse import unquote

class RedesView(TemplateView):
    template_name = "pages/redes.html"
    def get_context_data(self, **kwargs):
        final_array = []
    
        with open('experimento_twitter/static/_xls/twitter.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                final_array.append(
                        {
                            'id do Tweet': row['id do Tweet'],
                            'link permanente do Tweet': row['link permanente do Tweet'],
                            'texto do Tweet': row['texto do Tweet'],
                            'impressões': row['impressões'],
                        }
                    )

        return {'content':(final_array)}


def index(request):
    final_array = []
    
    with open('experimento_twitter/static/_xls/twitter.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            final_array.append(
                    {
                        'id do Tweet': row['id do Tweet'],
                        'link permanente do Tweet': row['link permanente do Tweet'],
                        'texto do Tweet': row['texto do Tweet'],
                        'impressões': row['impressões'],
                    }
                )
    return JsonResponse(final_array, safe=False)