# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "plane/pressure/external"
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

    pressure_outside = [0,0,0,0,0,0,1428,2857,4285,5714,7142,8571,10000,10000,10000]



    msg_count = 0
    client.publish("plane/pressure/external", "RETAIN", retain=True)
    client.will_set("plane/pressure/external", payload="ERROR CRASH", retain=True)

    def fttomb(ft):
        mb = 1013 - (ft / 27)
        return mb

    while True:
        msg_count += 1

        msg = f"messages: {msg_count}"
        pressure_outside = [0, 0, 0, 0, 0, 0,
                            1428, 2857, 4285, 5714, 7142, 8571, 10000, 10000, 10000, 10000, 15790, 21600, 27400, 33200,
                            39000,
                            39000, 39000, 39000, 39000, 39000, 39000, 39000, 39000, 39000, 39000,
                            36000, 34500, 31000, 30000, 30000, 30000,
                            27850, 25710, 23560, 21420, 19280, 17140, 15000, 12850, 10710, 8560, 6420, 2140,
                            0, 0, 0, 0, 0]

        while msg_count < 60:
            time.sleep(1)

            client.publish("plane/pressure/external", pressure_outside[msg_count])

            msg_count += 1
            #result = client.publish(topic, msg)


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


