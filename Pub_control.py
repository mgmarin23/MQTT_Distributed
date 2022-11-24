# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "plane/control/control"
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
    client.publish("plane/control", "", qos=1, retain=True)
    client.publish(topic, "", qos=1, retain=True)

    msg_count = 0
    while True:
        while msg_count < 61:
            time.sleep(1)
            if msg_count == 1:
                runway = random.randrange(1, 7)
                client.publish(topic, "Takes off on runway " + str(runway), qos=1, retain=True)
            if msg_count == 54:
                runway2 = random.randrange(1, 7)
                client.publish(topic, "Land on runway " + str(runway2) , qos=1, retain=True)

            msg_count += 1
            # result = client.publish(topic, msg)
        client.disconnect()

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

