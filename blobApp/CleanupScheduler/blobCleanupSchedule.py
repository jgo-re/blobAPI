from apscheduler.schedulers.background import BackgroundScheduler
from blobApp import blobRepository

def start():
    blobRepository.CleanupTask()
    scheduler = BackgroundScheduler()
    scheduler.add_job(blobRepository.CleanupTask, "interval", minutes=1, id="blobCleanup", replace_existing=True)
    scheduler.start()