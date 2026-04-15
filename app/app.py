import json

from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

def handle_publish(data):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect("emqx", 1883, 60)
    client.publish("notifictions", json.dumps(data))
    client.disconnect()

if __name__ == "__main__":
    app = Flask(__name__)

    @app.post("/publish")
    def publish():
        data = request.get_json()
        try:
            handle_publish(data)
            return jsonify({
                "status": 200,
                "message": "publish executed succesfully!"
            })
        except Exception as e:
            return jsonify({
                "status": 500,
                "message": repr(e)
            })