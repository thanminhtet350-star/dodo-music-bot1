import os
import requests
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN", "")
API = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

def send_message(chat_id, text):
    requests.post(
        f"{API}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=15
    )

@app.route("/")
def home():
    return "DoDo Music Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    from flask import request

    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "")

    if chat_id and text == "/start":
        send_message(
            chat_id,
            "🎵 Welcome to DoDo Music Bot!\n\n"
            "🆓 Free Music Bot\n"
            "🎧 သီချင်းရှာရန် /music\n"
            "📢 ကြော်ငြာအတွက် Admin ကို ဆက်သွယ်ပါ။"
        )

    elif chat_id and text == "/music":
        send_message(
            chat_id,
            "🎵 သီချင်းနာမည်ကို ရိုက်ပို့ပေးပါ။\n"
            "လက်ရှိမှာ သီချင်းရှာဖွေစနစ်ကို "
            "ဆက်လက်တည်ဆောက်နေပါတယ်။"
        )

    return {"ok": True}

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
