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
    client.publish("control/plane43", "", retain=True)
    while True:

        msg = f"messages: {msg_count}"
        pilot = random.randrange(1, 3)
        stime1 = random.randrange(21, 25)
        stime2 = random.randrange(25, 31)





        #self, topic, payload = None, qos = 0, retain = False, properties = None
        #result = client.publish(topic, msg)


        # result: [0, 1]



        while msg_count < 61:
            time.sleep(1)
            if msg_count == 47:
                client.publish("control/plane43", "Status OK", retain=True)
            msg_count += 1
        '''
            if -1<msg_count<6:
                client.publish("plane/service/status", "TAKEOFF")
            elif 6<msg_count<21:
                client.publish("plane/service/status", "CLIMB")
            elif 21<msg_count<31:
                client.publish("plane/service/status", "CRUISE")
                topic2 = "plane/service/pilot" + str(pilot)
                if(msg_count == stime1):
                    client.publish(topic2, "assistance", qos=1)
                    client.publish("plane/service/status", "CRUISE")
                elif(msg_count == stime2):
                    client.publish(topic2, "assistance", qos=1)
                    client.publish("plane/service/status", "CRUISE")
            elif 31 < msg_count < 48:
                client.publish("plane/service/status", "DESCENDING")
                if msg_count == 47:
                    client.publish("control/plane43","Status OK",retain=True)
            elif 48< msg_count < 60:
                client.publish("plane/service/status", "GROUND")
        '''



            # result = client.publish(topic, msg)

        client.disconnect()

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

