# Eben Taljaard
import tkinter as tk
from tkinter import messagebox

from catalog import PRODUCTS
from purchase import start_purchase
from checkout import simulate_purchase
from return_handler import handle_return
from inventory import get_gems, get_coins


class GameApp:

    def __init__(self, root):

        self.root = root
        self.root.title(
            "Farm Game - IAP Sandbox"
        )

        self.root.geometry(
            "500x400"
        )

        self.status = tk.StringVar(
            value="Farm ready"
        )

        tk.Label(
            root,
            text="🌾 My Farm",
            font=("Arial", 24)
        ).pack(pady=20)

        self.inventory = tk.Label(
            root,
            text=""
        )

        self.inventory.pack(
            pady=10
        )

        tk.Label(
            root,
            text="Shop",
            font=("Arial", 18)
        ).pack(pady=10)

        for product in PRODUCTS.values():

            tk.Button(
                root,
                text=(
                    f"{product['name']}   "
                    f"{product['price']}"
                ),
                command=lambda p=product:
                    self.buy(p["id"]),
                width=35
            ).pack(
                pady=5
            )

        tk.Label(
            root,
            textvariable=self.status
        ).pack(
            pady=20
        )

        self.refresh_inventory()

    def refresh_inventory(self):

        self.inventory.config(
            text=(
                f"💎 Gems: {get_gems()}    "
                f"🪙 Coins: {get_coins()}"
            )
        )

    def buy(self, product_id):

        self.status.set(
            "Creating purchase..."
        )

        # Game → purchase service
        redirect_url = start_purchase(
            product_id
        )

        self.status.set(
            "Redirecting to checkout..."
        )

        # Normally a browser/app-store
        # flow would happen here.
        #
        # For this sandbox we simulate
        # the checkout directly.

        from urllib.parse import (
            urlparse,
            parse_qs
        )

        query = parse_qs(
            urlparse(
                redirect_url
            ).query
        )

        order_id = query[
            "order_id"
        ][0]

        product = query[
            "product_id"
        ][0]

        # Simulated checkout
        simulate_purchase(
            order_id,
            product
        )

        # Return to game
        result = handle_return(
            order_id
        )

        if result["status"] == "success":

            self.status.set(
                "Purchase complete!"
            )

            messagebox.showinfo(
                "Purchase",
                f"{product} added!"
            )

        else:

            self.status.set(
                f"Purchase: "
                f"{result['status']}"
            )

        self.refresh_inventory()


if __name__ == "__main__":

    root = tk.Tk()

    app = GameApp(root)

    root.mainloop()
