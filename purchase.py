# Eben Taljaard
from order import create_order


CHECKOUT_URL = "http://127.0.0.1:5555/checkout"


def start_purchase(product_id):

    order_id = create_order(product_id)

    print(
        f"[PURCHASE] Created order {order_id}"
    )

    redirect_url = (
        f"{CHECKOUT_URL}"
        f"?order_id={order_id}"
        f"&product_id={product_id}"
    )

    print(
        f"[PURCHASE] Redirect -> {redirect_url}"
    )

    return redirect_url
