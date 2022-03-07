import RPi.GPIO as GPIO
from pirc522 import RFID
import time

from paho.mqtt import client as mqtt_client
import time

broker = 'broker.hivemq.com'
port = 1883
topic = "/vmk/team3"
client_id = 'python-mqtt-poezd-pub'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected")
        else:
            print("Fail")
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rc522 = RFID()

client = connect_mqtt()
client.loop_start()

while True :
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error:
        (error, uid) = rc522.anticoll()

        if not error:
           client.publish(topic, str(uid))
           time.sleep(1)
