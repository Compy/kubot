from kubot.core.dispatcher import register_command

def cmd(command, access="*", help_text=""):
    def decorate(fn):
        register_command(command, fn, access, help_text)
        return fn
    return decorate