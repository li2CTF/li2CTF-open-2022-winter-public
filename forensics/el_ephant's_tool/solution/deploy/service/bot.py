import time
import flask
import telebot
from telebot import types
from subprocess import run, PIPE
import datetime as dt
from json import dumps, loads
import sys
from os import system

messages_to_send = dict()

with open("/ttt/TOKEN", "r") as f:
    BOT_TOKEN = f.read().strip()

system("rm /ttt/TOKEN");

PHP_WRAPPER = 'eval("echo %s;");'
WEBHOOK_HOST = 'b.li2sites.ru'
WEBHOOK_PORT = 22000
WEBHOOK_LISTEN = "0.0.0.0"

WEBHOOK_URL_BASE = "http://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s" % (BOT_TOKEN)

app = flask.Flask(__name__)
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

def gen_message(
        chat_id, text,
        disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None,
        parse_mode=None, disable_notification=None, timeout=None,
        entities=None, allow_sending_without_reply=None):
    payload = {'chat_id': str(chat_id), 'text': text}
    if disable_web_page_preview is not None:
        payload['disable_web_page_preview'] = disable_web_page_preview
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if parse_mode:
        payload['parse_mode'] = parse_mode
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if timeout:
        payload['timeout'] = timeout
    if entities:
        payload['entities'] = dumps(types.MessageEntity.to_list_of_dicts(entities))
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    return payload


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


@app.route(WEBHOOK_URL_PATH + '/', methods=['POST'])
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        json_d = loads(json_string)
        bot.process_new_updates([update])
        return messages_to_send[str(json_d["message"]["chat"]["id"])]
    else:
        flask.abort(403)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: telebot.types.Message):
    reply = gen_message(message.chat.id, "Hello, Mr. El Ephant, I'm 3l3ph4n7, your pocket code executor (calculator mostly)!\nWrite me something:")
    reply["method"] = "sendMessage"
    messages_to_send[str(message.chat.id)] = flask.jsonify(reply)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def exec_php_cmd(message):
    cmd = message.text
    cmd_result = run(["php", "-r", PHP_WRAPPER % cmd], stdout=PIPE, stderr=PIPE)
    result = b"output: " + cmd_result.stdout
    if cmd_result.stderr:
        result = b"error occured\n\n" + result
    print("====== cmd =====")
    print(PHP_WRAPPER % cmd)
    print("================")
    reply = gen_message(message.chat.id, result.decode())
    reply["method"] = "sendMessage"
    messages_to_send[str(message.chat.id)] = flask.jsonify(reply)


if __name__ == "__main__":
    # Start flask server
    app.run(host=WEBHOOK_LISTEN,
            port=WEBHOOK_PORT)
