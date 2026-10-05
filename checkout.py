# Eben Taljaard
import json
import urllib.request
from urllib.parse import urlparse, parse_qs


WEBHOOK_URL = (
    "http://127.0.0.1:5555/webhook/iap"
)


def simulate_purchase(order_id, product_id):

    payload = {
        "event": "iap.purchase.completed",

        "order_id": order_id,

        "product_id": product_id,

        "purchase_token":
            f"SIM-{order_id}",

        "status": "completed",
    }

    data = json.dumps(payload).encode()

    request = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={
            "Content-Type":
                "application/json"
        },
        method="POST",
    )

    with urllib.request.urlopen(request) as response:

        return response.read().decode()
