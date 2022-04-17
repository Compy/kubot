from kubot.core.handlers import cmd
from kubernetes import client


@cmd("status", access="admin", help_text="Get deployment status")
def adduser(args, message, say):
    namespaces = args
    v1 = client.AppsV1Api()
    ret = v1.list_deployment_for_all_namespaces()
    blocks = []
    for i in ret.items:
        if len(namespaces) == 0 or i.metadata.namespace in namespaces:
            if i.status.ready_replicas == i.status.replicas:
                status = ":large_green_circle:"
            else:
                status = ":large_yellow_circle:"

            image_list = []
            for c in i.spec.template.spec.containers:
                image_list.append(c.image)

            images = ", ".join(image_list)

            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{status} *{i.metadata.name}* - {i.status.ready_replicas} ready of {i.status.replicas}\nImages: `{images}`"
                }
            })
    if len(blocks) == 0:
        say("I have no deployments")
    else:
        for i in range(0, len(blocks), 50):
            say(blocks=blocks[i:i+50])
