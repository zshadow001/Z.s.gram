from flask import Flask, render_template
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

app = Flask(__name__)

client = TelegramClient(
    StringSession(STRING_SESSION),
    API_ID,
    API_HASH
)

client.connect()

# Startup pe hi data load kar lo
me = client.get_me()

try:
    dialogs = client.get_dialogs(limit=100)
except Exception:
    dialogs = []

channel_list = []

for d in dialogs:
    try:
        if d.is_channel:
            channel_list.append(d)
    except:
        pass


@app.route("/")
def home():
    return render_template(
        "index.html",
        name=me.first_name,
        username=me.username,
        phone=me.phone
    )


@app.route("/profile")
def profile():
    return render_template(
        "profile.html",
        me=me
    )


@app.route("/chats")
def chats():
    return render_template(
        "chats.html",
        dialogs=dialogs
    )


@app.route("/channels")
def channels():
    return render_template(
        "channels.html",
        channels=channel_list
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)