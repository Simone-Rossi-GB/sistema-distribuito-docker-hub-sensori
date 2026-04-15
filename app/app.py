import json
import socket
from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt

def handle_publish(data):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect("emqx", 1883, 60)
    client.publish("notifications", json.dumps(data))
    client.loop(timeout=1.0)  # aspetta che il messaggio venga consegnato
    client.disconnect()

if __name__ == "__main__":
    app = Flask(__name__)

    @app.get("/")
    def health():
        return jsonify({
                "status": 200,
                "message": "alive",
                "server": socket.gethostname()
            })

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

    app.run(host="0.0.0.0", port=5000)