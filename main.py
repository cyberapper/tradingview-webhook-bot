import json
import time

from flask import Flask, request

from tradingview_webhook_bot.handler import *
from tradingview_webhook_bot.emitter import EventEmitter

app = Flask(__name__)

event_emitter = None

if config.rabbitmq_url != "":
    event_emitter = EventEmitter(config.rabbitmq_url)

def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data["key"]
            if key == config.sec_key:
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200

            else:
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return "Refused alert", 400

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return "Error", 400


@app.route("/broadcast", methods=["POST"])
def broadcast():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data.get("key")
            if key == config.sec_key:
                print(get_timestamp(), "Broadcast Alert Received & Sent!")
                broadcast_message(data)
                return "Broadcast sent", 200
            else:
                print("[X]", get_timestamp(), "Broadcast Alert Received & Refused! (Wrong Key)")
                return "Refused broadcast", 400
    except Exception as e:
        print("[X]", get_timestamp(), "Error in broadcast:\n>", e)
        return "Error in broadcast", 400


@app.route("/trade", methods=["POST"])
def trade():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data.get("key")
            if key == config.sec_key:
                print(get_timestamp(), "Trade Alert Received & Sent!")
                if event_emitter:
                    event_emitter.publish(
                        json.dumps(
                            {"event": "TVWebhook.tradeTriggered", "payload": data}
                        )
                    )
                return "Trade alert sent", 200
            else:
                print("[X]", get_timestamp(), "Trade Alert Received & Refused! (Wrong Key)")
                return "Refused trade alert", 400
    except Exception as e:
        print("[X]", get_timestamp(), "Error in trade alert:\n>", e)
        return "Error in trade alert", 400


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=80)
