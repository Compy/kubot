from dotenv import load_dotenv
load_dotenv()

import kubot.slack.app
from kubot.kubernetes.controller import init_kubernetes_controller

def run_kubot():
    # TODO: We need to wait for the condition_type enum fix that crashes on boot
    init_kubernetes_controller()
    kubot.slack.app.slack_init()