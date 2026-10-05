# Eben Taljaard
from storage import load_state


def get_inventory():

    state = load_state()

    return state.get(
        "inventory",
        {}
    )


def get_gems():

    return get_inventory().get(
        "gems",
        0
    )


def get_coins():

    return get_inventory().get(
        "coins",
        0
    )
