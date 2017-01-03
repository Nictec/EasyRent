from django.shortcuts import HttpResponse 
from django.forms.models import model_to_dict
import json

def render_to_ember(data): 
    return HttpResponse(json.dumps(data),  content_type='application/json') 

