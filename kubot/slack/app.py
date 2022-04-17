import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from kubot.core import dispatcher

app = App(token=os.environ["SLACK_BOT_TOKEN"])

from kubot.commands import *

@app.event("message")
def on_message_event(message, say):
    # First check if this is an IM or a channel
    # If the message is in a channel but doesn't begin with our prefix, then ignore the message
    if message["channel_type"] == "channel" and message["text"][0] != os.environ["BOT_COMMAND_PREFIX"]:
        return
    
    command = message["text"].split()[0]
    if message["channel_type"] == "channel":
        command = command[1:]
    elif message["text"][0] == os.environ["BOT_COMMAND_PREFIX"]:
        command = command[1:]
    args = message["text"].split()[1:]

    # Split the message payload into 
    dispatcher.handle_command(command, args, message, say)

def slack_init():
    #print(app.client.users_list())
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()