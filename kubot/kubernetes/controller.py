from kubernetes import client, config

def init_kubernetes_controller():
    config.load_kube_config()

    v1 = client.AutoscalingV1Api()
    print(v1.list_horizontal_pod_autoscaler_for_all_namespaces())