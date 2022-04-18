from datetime import datetime
from .serializers import BlobSerializer
from .models import Blob
from datetime import *
import time
import secrets

BLOB_TTL_MINUTES = 15

def Get(key):
    try:
        blob = Blob.objects.get(Key=key)
    except Blob.DoesNotExist:
        return (False, {})
    
    if((time.time() - blob.CreatedOn.timestamp()) > (BLOB_TTL_MINUTES*60)):
        blob.delete()
        return (False, {})

    blobsSerializer = BlobSerializer(blob)
    return (True, blobsSerializer.data)


def Create(value):
    newKey = secrets.token_urlsafe(7)
    newBlob = Blob(Key=newKey, Value=value)
    newBlob.save()
    return newKey


def CleanupTask():
    blobs = Blob.objects.filter(CreatedOn__lt=(datetime.now(tz=timezone.utc) - timedelta(minutes=BLOB_TTL_MINUTES)))
    print(f'Deleting: {blobs.count()} expired blobs.')
    blobs.delete()