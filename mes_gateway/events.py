import json
import time

from mes_gateway.tasks import send_to_api
from mes_gateway.models import Event


def _decouple_payload(payload):
    payload = json.loads(payload.decode())
    try:
        body = chr(payload.get("p"))
    except TypeError:
        body = payload.get("p")

    device_id = payload.get("i")
    timestamp = int(time.time())
    return Event(device_id=device_id, body=body, timestamp=timestamp)


def send(mqtt_payload):
    event = _decouple_payload(mqtt_payload)
    send_to_api.delay(*event)

