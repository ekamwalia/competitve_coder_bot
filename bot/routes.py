from bot import app
from bot.codechef import codechef_scraper
from os import environ
import json
import requests
from flask import request


@app.route("/newMessage", methods=['POST', 'GET'])
def new_message_handler():
    update_json = request.get_json()

    chat_id = update_json["message"]["chat"]["id"]
    print(update_json)
    payload_text = switch()
    payload = {
        "chat_id": chat_id,
        "text": payload_text
    }

    resp = requests.post(environ.get("bot_base_url") + "/sendMessage", payload)
    return "Request received"


@app.route("/")
def hello():
    return "GET / works"
