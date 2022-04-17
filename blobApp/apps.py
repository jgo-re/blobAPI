from django.apps import AppConfig

class BlobappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blobApp'

    def ready(self):
        from .CleanupScheduler import blobCleanupSchedule
        blobCleanupSchedule.start()