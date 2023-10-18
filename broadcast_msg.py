import os
import sys

from linebot import LineBotApi
from linebot.models import TextSendMessage

channel_access_token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
line_bot_api.broadcast(
    [
        TextSendMessage(text="THIS IS A BROADCAST MESSAGE"),
    ]
)
