# Eben Taljaard
PRODUCTS = {
    "gems_100": {
        "id": "gems_100",
        "name": "100 Gems",
        "description": "A small bundle of game gems",
        "price": "R19.99",
        "type": "consumable",
    },

    "gems_500": {
        "id": "gems_500",
        "name": "500 Gems",
        "description": "A large bundle of game gems",
        "price": "R79.99",
        "type": "consumable",
    },

    "starter_pack": {
        "id": "starter_pack",
        "name": "Starter Pack",
        "description": "Gems, coins and starter items",
        "price": "R49.99",
        "type": "non_consumable",
    },
}


def get_product(product_id):
    return PRODUCTS.get(product_id)
