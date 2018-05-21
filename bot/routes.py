from bot import app
from bot.middleware import switch
from os import environ
import requests
from flask import request, jsonify


@app.route("/newMessage", methods=['POST', 'GET'])
def new_message_handler():
    update_json = request.get_json()

    if not (update_json["message"]):
        return jsonify({"success": False})

    chat_id = update_json["message"]["chat"]["id"]
    payload_text = switch(update_json["message"]["text"])
    payload = {
        "chat_id": chat_id,
        "text": payload_text
    }

    resp = requests.post(environ.get("bot_base_url") + "/sendMessage", payload)
    return "Request received"


@app.route("/")
def hello():
    return "GET / works"
