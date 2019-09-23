import requests
from celery import Celery
from decouple import config

from mes_gateway.models import Event


REDIS_HOST = config("REDIS_HOST")
API_URL = config("API_URL")

app = Celery('tasks', broker=f"redis://{REDIS_HOST}:6379")


@app.task
def send_to_api(*event_args):
    event = Event(event_args)
    requests.post(API_URL, json=event._asdict())
