# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "plane/pressure"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)  #1
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    client.publish("plane/pressure", "RETAIN", retain=True)
    client.will_set("plane/pressure", payload="ERROR CRASH", retain=True)
    while True:
        msg_count += 1

        msg = f"messages: {msg_count}"

        while msg_count < 16:
            time.sleep(1)
            msg1 = random.randrange(98, 102, 1)
            msg2 = random.randrange(99, 101)
            msg3 = random.randrange(msg2-1, msg2+1)

            #client.will_set("plane/pressure", "ok", 0, True)
            client.publish("plane/pressure", msg_count)

            msg_count += 1
            #result = client.publish(topic, msg)
        while 15 < msg_count < 31:
            time.sleep(1)
            client.publish("plane/pressure", "msg_count")

            msg_count += 1


        while 30 < msg_count < 46:

        # result: [0, 1]
            time.sleep(1)
            client.publish("plane/pressure", msg_count)
            msg_count += 1

        client.disconnect()
"""
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` kPa to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        """

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

