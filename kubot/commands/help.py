from kubot.core.handlers import cmd
import kubot.core.dispatcher


@cmd(command="help", access="*", help_text="""
List all commands and their arguments
""")
def help(args, message, say):
    if len(args) == 0:
        response = "```"
        for cmd, v in kubot.core.dispatcher.commands.items():
            response = response + cmd
            if 'help' in v and v['help'] != "":
                response = response + " - " + v['help'].strip()
            response = response + "\n"
        response = response + "```"
        say(response)
    else:
        if args[0].lower() not in kubot.core.dispatcher.commands:
            say(f"<@{message['user']}> {args[0]} is not a valid command")
        elif kubot.core.dispatcher.commands[args[0].lower()]['help'] == "":
            say(f"<@{message['user']}> I don't have any information for command {args[0]}")
        
        response = "```"
        response = response + f"Help for command '{args[0]}'\n"
        response = response + kubot.core.dispatcher.commands[args[0].lower()]['help'] + "```"
        say(response)