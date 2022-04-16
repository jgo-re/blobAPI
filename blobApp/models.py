from django.db import models

class Blob(models.Model):
    Key = models.CharField(max_length=10, primary_key=True)
    Value = models.TextField(max_length=5000)
    CreatedOn = models.DateTimeField(auto_now_add=True)