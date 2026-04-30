from flask import Flask, request, abort
from linebot.v3.webhook import WebhookHandler
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
import os

CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

app = Flask(__name__)

configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/")
def home():
    return "OK"


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    handler.handle(body, signature)
    return "OK"


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    text = event.message.text


    if "雞雞" in text:
        reply = "關鍵字包含免疫狗沒有的東西"
    elif "很色" in text:
        reply = "ㄏㄏ"
    elif "好色" in text:
        reply = "ㄏㄏ"
    elif "很大" in text:
        reply = "沒你大"
    elif "噴出" in text:
        reply = "輪機系帶你見見世面OK?"
    elif "噴很多" in text:
        reply = "輪機系帶你見見世面OK?"
    elif "尻尻" in text:
        reply = "-"*2000
    elif "噴噴" in text:
        reply = "好可憐 腦子長水泡"
    elif "麻麻" in text:
        reply = "好可憐 腦子長水泡"
    elif "尻噴麻" in text:
        reply = "好可憐 腦子長水泡"
    elif "女房" in text:
        reply = "好可憐 整天意淫人家"
    elif "女室" in text:
        reply = "好可憐 整天意淫人家"
    elif "把握" in text:
        reply = "說說仔 準備300萬比較快"
    elif "沒機會" in text:
        reply = "說說仔 準備300萬比較快"
    else:
        return

    with ApiClient(configuration) as api_client:
        MessagingApi(api_client).reply_message(
            ReplyMessageRequest(
                replyToken=event.reply_token,
                messages=[TextMessage(text=reply)]
            )
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
