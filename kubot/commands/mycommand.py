from kubot.core.handlers import cmd

@cmd("mycommand", access="admin", help_text="A very simple command")
def adduser(args, message, say):
    say(f"I got the following arguments {str(args)}")
    say(f"The message payload was {str(message)}")