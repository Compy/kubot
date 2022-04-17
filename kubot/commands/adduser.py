from kubot.core.handlers import cmd

@cmd("adduser", access="admin", help_text="Add a user to the system")
def adduser(args, message, say):
    if len(args) < 1:
        say("""```Syntax: adduser @username [access level]
        Where access level is either user or admin
        ```""")
        return
    access_level = "user"
    if len(args) > 1:
        access_level = args[1].lower()
    print(message)
    say(f"Added user {args[0]} with access level `{args[1]}`")