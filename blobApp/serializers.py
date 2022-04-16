from dataclasses import field
from rest_framework import serializers
from .models import Blob

class BlobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blob
        fields = ('Key', 'Value', 'CreatedOn')