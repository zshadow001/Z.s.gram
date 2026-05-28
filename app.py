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

client.start()

@app.route("/")
def home():
    me = client.get_me()

    return render_template(
        "index.html",
        name=me.first_name,
        username=me.username,
        phone=me.phone
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)