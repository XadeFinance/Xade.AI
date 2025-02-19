# celery_app.py
from celery import Celery
import os
from dotenv import load_dotenv
from celery.schedules import crontab
import data_cycle  # Import data_cycle module directly for discovery

load_dotenv()

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

celery_app = Celery('data_cycle_tasks',
                    broker=CELERY_BROKER_URL,
                    backend=CELERY_RESULT_BACKEND,
                    include=['data_cycle'])

celery_app.conf.beat_schedule = {
    'run-data-cycle-hourly': {
        'task': 'data_cycle.run_data_cycle_task',
        'schedule': crontab(minute=1),
    },
}
celery_app.conf.timezone = 'UTC'

# Redbeat Configuration - ADD THESE LINES:
celery_app.conf.beat_scheduler = 'redbeat.RedBeatScheduler'
celery_app.conf.redbeat_redis_url = CELERY_BROKER_URL 

print(f"Celery App Instance in celery_app.py: {celery_app}")
print("Registered Celery tasks:", celery_app.tasks.keys()) # Check registered tasks

celery_app.autodiscover_tasks(force=True)

if __name__ == '__main__':
    celery_app.start()