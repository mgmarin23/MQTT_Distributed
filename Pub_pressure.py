# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "plane/control/pressure/external"
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
    client.publish("plane/pressure/external", "", retain=True)


    def fttomb(ft):
        mb = 1013 - (ft / 27)
        return mb

    while True:


        msg = f"messages: {msg_count}"
        pressure_outside = [0, 0, 0, 0, 0, 0, #TAKEOFF
                            1428, 2857, 4285, 5714, 7142, 8571, 10000, 10000, 10000, 10000, 15790, 21600, 27400, 33200,
                            39000,
                            39000, 39000, 39000, 39000, 39000, 39000, 39000, 39000, 39000, 39000,
                            36000, 34500, 31000, 30000, 30000, 30000,
                            27850, 25710, 23560, 21420, 19280, 17140, 15000, 12850, 10710, 8560, 6420, 2140,
                            1500,900,500,200,150,100,50,
                            0, 0, 0, 0, 0]
        HIGH = 'TAKE_OFF'
        for press in pressure_outside:
            time.sleep(1)

            client.publish("plane/control/pressure/external", press)

            if HIGH == 'TAKE_OFF':
                if press > 1000:
                    HIGH = 'CLIMB'
                    client.publish("plane/service/status", "CLIMB")
                    continue
                HIGH = 'TAKE_OFF'
                client.publish("plane/service/status", "TAKEOFF")
                continue
            else:
                if HIGH == 'CLIMB':
                    if press > 33200:
                        HIGH = 'CRUISE'
                        print('START CRUISE')
                        print('Available plane service')
                        print('Automatic plane control')
                        client.publish("plane/service/status", "CRUISE")
                        continue
                    HIGH = 'CLIMB'
                    client.publish("plane/service/status", "CLIMB")
                    continue
                else:
                    if HIGH == 'CRUISE':
                        if press == 39000:
                            client.publish("plane/service/status", "CRUISE")
                            HIGH = 'CRUISE'
                            continue
                        else:
                            HIGH = 'DECENT'
                            print('START DECENT')
                            print('Unavailable plane service')
                            print('Manual plane control')
                            client.publish("plane/service/status", "DESCENDING")
                            continue
                    else:
                        if HIGH == 'DECENT':
                            HIGH = 'DECENT'
                            if press < 1500:
                                HIGH = 'GROUND'
                                client.publish("plane/service/status", "GROUND")
                                continue
                            client.publish("plane/service/status", "DESCENDING")
                            continue
                        else:
                            if HIGH == 'GROUND':
                                HIGH = 'GROUND'
                                client.publish("plane/service/status", "GROUND")
                                continue


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
    time.sleep(10)
    client.disconnect()

def disconnect():
    client = connect_mqtt()
    time.sleep(10)
    client.disconnect()


if __name__ == '__main__':
    run()


