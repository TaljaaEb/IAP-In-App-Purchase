# Eben Taljaard
from entitlement import grant_product
from order import update_order


def process_callback(payload):

    if payload.get("event") != \
            "iap.purchase.completed":

        return {
            "ok": False,
            "error": "Unknown event"
        }

    order_id = payload["order_id"]
    product_id = payload["product_id"]

    if payload.get("status") != "completed":

        update_order(
            order_id,
            "failed"
        )

        return {
            "ok": False,
            "order_id": order_id
        }

    # Mark order paid/completed
    update_order(
        order_id,
        "completed"
    )

    # Grant the game item
    grant_product(
        product_id,
        order_id
    )

    return {
        "ok": True,
        "order_id": order_id,
        "product_id": product_id,
        "callback": "accepted",
    }
