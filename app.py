from flask import Flask, render_template
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 12345678
API_HASH = "YOUR_API_HASH"
STRING_SESSION = "YOUR_STRING_SESSION"

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