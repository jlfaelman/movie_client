import json
import traceback
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests

api_url = "http://127.0.0.1:5000"
# Create your views here.
def index(request):

    try:
        genres = replace_none_with_null(get_genres())

        url = api_url + "/api/list"
        response = requests.get(url)
        data = response.json()
        data = replace_none_with_null(data)
        data = replace_false(data)
        return render(request, 'index.html', {"data":data, "genres":genres})
    except Exception as e:
        if e: traceback.print_exc()


def replace_none_with_null(data):
    if isinstance(data, list):
        return [replace_none_with_null(item) for item in data]
    elif isinstance(data, dict):
        return {key: replace_none_with_null(value) for key, value in data.items()}
    elif data is None:
        return 'null'
    else:
        return data
    
def replace_false(data):
    if isinstance(data, list):
        return [replace_false(item) for item in data]
    elif isinstance(data, dict):
        return {key: replace_false(value) for key, value in data.items()}
    elif data is False:
        return 'False'
    else:
        return data
    


def get_genres():
    try:
        url = api_url + "/api/genres"
        response = requests.get(url)
        data = response.json()
        return {"data":data}
    except Exception as e:
        if e: traceback.print_exc()
        return {"data":{}}

    return