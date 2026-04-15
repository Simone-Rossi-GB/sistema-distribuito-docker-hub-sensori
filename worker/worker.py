import paho.mqtt.client as mqtt

def connected(client, userdata, flags, reason_code, properties):
    print("connesso al MQTT broker")
    client.subscribe("notifications")

def on_message(client, userdata, message):
    print(f"messaggio del topic {message.topic}: {message.payload.decode()}")


if __name__ == "__main__":
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = connected
    client.on_message = on_message
    client.connect("emqx", 1883, 60)
    client.loop_forever()