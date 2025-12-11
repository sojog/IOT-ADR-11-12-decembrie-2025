

# pip install paho-mqtt
import paho.mqtt.client as mqtt
import random
import time

MQTT_BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "curs/iot/temperatura" # echivalent cu o frecventa radio


def on_connect(client, userdata, connect_flags, reason_code):
    if reason_code == 0:
        print("Dispozitivul s-a conectat cu success")
    else:
        print(f"Conexiunea este esuata: {reason_code}")


client_id = "IOT_PUBLICATOR_" + str(random.randint(1, 1000))
print(client_id)


client = mqtt.Client(client_id=client_id)

client.on_connect = on_connect


MIN_TEMP = 1
MAX_TEMP = 50

## Logica Principala
try:
    client.connect(MQTT_BROKER, PORT, 60)
    client.loop_start()


    while True:
        MIN_TEMP = 1
        MAX_TEMP = 50
        temperatura = random.randint(MIN_TEMP, MAX_TEMP)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


        payload = f'''{{
            "timestamp" : "{timestamp}",
            "temperatura" : {temperatura}
        }}'''

        print(payload)

        client.publish(TOPIC, payload=payload, qos=0)

        time.sleep(5)

except Exception as e:
    print(f"A aparut o eroare {e}")