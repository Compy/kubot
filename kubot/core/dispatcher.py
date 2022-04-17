commands: dict = {}

def register_command(command, callback, access="*", help_text=""):
    if command.lower() in commands:
        raise Exception(f"The command {command} is already registered")
    commands[command.lower()] = {
        "callback": callback,
        "access": access,
        "help": help_text
    }
    print(f"Registered command {command}")

def handle_command(command, args, message, say):
    if command.lower() not in commands:
        say("I don't recognize that command. Use `.help` or DM me with `help` for a list of commands")
        return
    commands[command.lower()]["callback"](args, message, say)