
# pip install paho-mqtt
import paho.mqtt.client as mqtt
import random
import time
import json
import pandas as pd

MQTT_BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "curs/iot/temperatura" # echivalent cu o frecventa radio


## Stocare a datelor
received_data = []
DATA_LIMIT = 5

def perform_analysis (received_data):
    df = pd.DataFrame(received_data)
    print(df)

    temperatura_medie = df['temperatura'].mean()
    temperatura_maxima = df['temperatura'].max()
    temperatura_minima = df['temperatura'].min()

    print("t max:", temperatura_maxima)
    print("t mean:", temperatura_medie)
    print("t min:", temperatura_minima)


def on_connect(client, userdata, connect_flags, reason_code):
    if reason_code == 0:
        print("Dispozitivul s-a conectat cu success")
        client.subscribe(TOPIC)
    else:
        print(f"Conexiunea este esuata: {reason_code}")

def on_message(client, userdata, message):
    "Se apeleaza de fiecare data cand primesc un mesaj"
    global received_data

    print(f"Topic: {message.topic}")
    payload_string = message.payload.decode()
    print(f"Mesajul primit este: {payload_string}")

    data = json.loads(payload_string)
    received_data.append(data)
    print("Received_data:", received_data)

    if len(received_data) >= DATA_LIMIT:
        client.loop_stop()
        client.disconnect()
        perform_analysis (received_data)


client_id = "IOT_ABONAT_" + str(random.randint(1, 1000))
print(client_id)

client = mqtt.Client(client_id=client_id)

client.on_connect = on_connect
client.on_message = on_message

## Logica Principala
try:
    client.connect(MQTT_BROKER, PORT, 60)
    client.loop_forever()

except Exception as e:
    print(f"A aparut o eroare {e}")