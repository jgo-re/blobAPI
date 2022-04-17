#from django.shortcuts import render
import re
import time
import secrets
from multiprocessing import managers
from .serializers import BlobSerializer
from .models import Blob
from rest_framework.parsers import JSONParser
from django.http import response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def blobApi(request, key=''):
    if request.method == 'GET':
        try:
            blob = Blob.objects.get(Key=key)
        except Blob.DoesNotExist:
            return response.HttpResponseNotFound()

        blobsSerializer = BlobSerializer(blob)
        return response.JsonResponse(blobsSerializer.data, safe=False)

    elif request.method == 'POST':
        blobData = JSONParser().parse(request)
        blobData['CreatedOn'] = time.time()
        newKey = secrets.token_urlsafe(7)
        blobData['Key'] = newKey
        blobSerializer = BlobSerializer(data = blobData)

        if blobSerializer.is_valid():
            blobSerializer.save()
            return response.JsonResponse(newKey, safe=False)

        return response.JsonResponse("blob failed", safe=False)