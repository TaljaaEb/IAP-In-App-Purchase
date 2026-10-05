# Eben Taljaard
from storage import load_state, save_state


def grant_product(product_id, order_id):

    state = load_state()

    inventory = state.setdefault(
        "inventory",
        {}
    )

    if product_id == "gems_100":

        inventory["gems"] = \
            inventory.get("gems", 0) + 100

    elif product_id == "gems_500":

        inventory["gems"] = \
            inventory.get("gems", 0) + 500

    elif product_id == "starter_pack":

        inventory["gems"] = \
            inventory.get("gems", 0) + 250

        inventory["coins"] = \
            inventory.get("coins", 0) + 1000

        inventory["starter_pack"] = True

    else:

        raise ValueError(
            f"Unknown product: {product_id}"
        )

    save_state(state)

    print(
        f"[ENTITLEMENT] "
        f"{product_id} granted "
        f"for {order_id}"
    )
