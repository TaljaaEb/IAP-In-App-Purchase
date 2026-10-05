# Eben Taljaard
import uuid
from datetime import datetime, timezone

from storage import load_state, save_state


def create_order(product_id):

    order_id = str(uuid.uuid4())

    state = load_state()

    state["orders"][order_id] = {
        "order_id": order_id,
        "product_id": product_id,
        "status": "created",
        "created": datetime.now(
            timezone.utc
        ).isoformat(),
    }

    save_state(state)

    return order_id


def update_order(order_id, status):

    state = load_state()

    if order_id not in state["orders"]:
        raise ValueError(
            f"Unknown order: {order_id}"
        )

    state["orders"][order_id]["status"] = status

    save_state(state)


def get_order(order_id):

    state = load_state()

    return state["orders"].get(order_id)
