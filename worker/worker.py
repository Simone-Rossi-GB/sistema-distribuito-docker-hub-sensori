import paho.mqtt.client as mqtt
import time

def connected(client, userdata, flags, reason_code, properties):
    print("connesso al MQTT broker")
    client.subscribe("notifications")

def on_message(client, userdata, message):
    print(f"messaggio del topic {message.topic}: {message.payload.decode()}")


if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = connected
    client.on_message = on_message

    while True:
        try:
            client.connect("emqx", 1883, 60)
            client.loop_forever()
        except Exception as e:
            print(f"connessione fallita: {e}. ESSIRIPROVA GUYZ fra 5 secondi...")
            time.sleep(5)