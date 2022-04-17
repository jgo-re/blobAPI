from rest_framework.parsers import JSONParser
from django.http import response
from django.views.decorators.csrf import csrf_exempt
from blobApp import blobRepository

# Create your views here.
@csrf_exempt
def blobApi(request, key=''):
    if request.method == 'GET':
        (success, data) = blobRepository.Get(key)

        if (not success):
            return response.HttpResponseNotFound()
                
        return response.JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            blobData = JSONParser().parse(request)
        except:
            return response.HttpResponseBadRequest()

        value = blobData.get('Value')
        if (not value or value.isspace()):
            return response.HttpResponseBadRequest()

        key = blobRepository.Create(value)
        return response.JsonResponse(key, safe=False)