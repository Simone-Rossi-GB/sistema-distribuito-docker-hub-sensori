from flask import Flask
import paho.mqtt.client as mqtt

def publish(data):
    pass

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/")
    