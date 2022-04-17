from kubot.core.handlers import cmd

@cmd("whoami", help_text="""
Sample command
""")
def whoami(args, message, say):
    #say(f"You are <@{message['user']}>!")
    say(blocks=[
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "New request"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Type:*\nPaid Time Off"
                },
                {
                    "type": "mrkdwn",
                    "text": "*Created by:*\n<example.com|Fred Enriquez>"
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*When:*\nAug 10 - Aug 13"
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "<https://example.com|View request>"
            }
        }
    ])