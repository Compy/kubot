# Kubot
*Because Hubot was taken*

---

## Intro
Kubot is a general purpose Slack bot with an emphasis on automating (and democratizing) Kubernetes tasks.

## Adding Commands
Adding your own commands to Kubot couldn't be easier.

1. Create a new file in `commands/` and name it something simple like `mycommand.py`
2. Inside of that python file, use the following boilerplate code:
```python
from kubot.core.handlers import cmd

@cmd("mycommand", access="admin", help_text="A very simple command")
def adduser(args, message, say):
    say(f"I got the following arguments {str(args)}")
    say(f"The message payload was {str(message)}")
```
3. Restart the bot by either performing a `rollout restart` manually, or using the `.restart kubot` command
4. Test your command by typing `.mycommand` in a public channel or direct messaging the bot with `mycommand`

## Maintainers
- [Compy](https://github.com/compy)