import os
import sys

from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, BroadcastRequest, TextMessage


channel_access_token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

configuration = Configuration(access_token=channel_access_token)

with ApiClient(configuration) as api_client:
    line_bot_api = MessagingApi(api_client)
    line_bot_api.broadcast(
        BroadcastRequest(
            messages=[
                TextMessage(text="THIS IS A BROADCAST MESSAGE")
            ]
        )
    )
