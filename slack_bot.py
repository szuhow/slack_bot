import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
token_input=input("Podaj token dostepu do slacka:\n")
channel_input=input("Podaj id kanalu do slacka: \n")
#logger = logging.getLogger(__name__)
client = WebClient(token='"'+token_input+'"')
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
@app.route('/kopiernia',methods=['POST'], )
def kopiernia():
        text_to_send = request.form['text']
        userName = request.form['user_name']
        response = client.chat_postMessage(channel='"'+channel_input+'"',text="Wiadomość od " + userName +": " +text_to_send)
        return "Wysłano wiadomość na kanał: " + text_to_send