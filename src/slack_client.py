from slack_sdk.webhook import WebhookClient

def send_notification(hook_url: str, message: str):
    url = hook_url
    webhook = WebhookClient(url)

    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
    return response