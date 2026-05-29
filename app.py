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

me = client.get_me()


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
    me = client.get_me()

    return render_template(
        "profile.html",
        me=me
    )


@app.route("/chats")
def chats():
    dialogs = client.get_dialogs(limit=100)

    return render_template(
        "chats.html",
        dialogs=dialogs
    )


@app.route("/channels")
def channels():
    dialogs = client.get_dialogs(limit=100)

    channel_list = []

    for d in dialogs:
        if d.is_channel:
            channel_list.append(d)

    return render_template(
        "channels.html",
        channels=channel_list
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)