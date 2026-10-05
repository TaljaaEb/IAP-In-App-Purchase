# Eben Taljaard
from order import get_order


def handle_return(order_id):

    order = get_order(order_id)

    if not order:

        return {
            "status": "unknown"
        }

    if order["status"] == "completed":

        return {
            "status": "success",
            "order_id": order_id,
            "product_id":
                order["product_id"],
        }

    if order["status"] == "failed":

        return {
            "status": "failed",
            "order_id": order_id,
        }

    return {
        "status": "pending",
        "order_id": order_id,
    }
