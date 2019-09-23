import logging
import asyncio

from mes_gateway.events import send

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_2
from decouple import config

MAIN_TOPIC = config("MQTT_MAIN_TOPIC")
BROKER_URL = config("MQTT_BROKER")

logger = logging.getLogger(__name__)


@asyncio.coroutine
def mqtt_subscribe_coro():
    C = MQTTClient()
    yield from C.connect(BROKER_URL)
    yield from C.subscribe([
            (MAIN_TOPIC, QOS_2),
         ])
    while True:
        try:
            message = yield from C.deliver_message()
            packet = message.publish_packet
            send(packet)

        except ClientException as ce:
            logger.error("Client exception: %s" % ce)
            yield from C.reconnect()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(mqtt_subscribe_coro())
