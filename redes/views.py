from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import csv
import json
from django.views.generic import TemplateView

class TwitterView(TemplateView):
    template_name = "pages/twitter.html"
    def get_context_data(self, **kwargs):
        final_array = []
    
        with open('experimento_twitter/static/_csv/twitter.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                final_array.append(
                        {
                            "id do Tweet": row['id do Tweet'],
                            "link permanente do Tweet": row['link permanente do Tweet'],
                            "texto do Tweet": row['texto do Tweet'].replace("'",'').replace('"', ''),
                            "impressões": row['impressões'],
                            "horário": row['horário'],
                            "interações": row['interações'],
                            "respostas": row['respostas'],
                            "taxa de envolvimento": float(row['interações']) / float(row['impressões']),
                        }
                    )
            
        return {'content':(str(final_array).replace("'", '"'))}
        
class FacebookView(TemplateView):
    template_name = "pages/facebook.html"
    def get_context_data(self, **kwargs):
        final_array = []
    
        with open('experimento_twitter/static/_csv/twitter.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                final_array.append(
                        {
                            "id do Tweet": row['id do Tweet'],
                            "link permanente do Tweet": row['link permanente do Tweet'],
                            "texto do Tweet": row['texto do Tweet'].replace("'",'').replace('"', ''),
                            "impressões": row['impressões'],
                            "horário": row['horário'],
                            "interações": row['interações'],
                            "respostas": row['respostas'],
                            "taxa de envolvimento": float(row['interações']) / float(row['impressões']),
                        }
                    )
            
        return {'content':(str(final_array).replace("'", '"'))}