import heapq


class Order:
    def __init__(
        self,
        order_id: int,
        order_type: str,
        price: int,
        quantity: int,
    ) -> None:
        self.id = order_id
        self.type = order_type
        self.price = price
        self.quantity = quantity


class Trade:
    def __init__(
        self,
        buy_id: int,
        sell_id: int,
        price: int,
        quantity: int,
    ) -> None:
        self.buy_id = buy_id
        self.sell_id = sell_id
        self.price = price
        self.quantity = quantity


def display_order_book(
    buy_orders: list,
    sell_orders: list,
) -> None:
    print("\nCurrent Buy Orders:")

    if not buy_orders:
        print("(none)")
    else:
        temp_buy = sorted(
            buy_orders,
            key=lambda item: (item[0], item[1]),
        )

        for negative_price, order_id, order in temp_buy:
            print(
                f"[Rs{order.price} x {order.quantity}] "
                f"(ID {order.id})"
            )

    print("\nCurrent Sell Orders:")

    if not sell_orders:
        print("(none)")
    else:
        temp_sell = sorted(
            sell_orders,
            key=lambda item: (item[0], item[1]),
        )

        for price, order_id, order in temp_sell:
            print(
                f"[Rs{order.price} x {order.quantity}] "
                f"(ID {order.id})"
            )


def display_trade_history(trade_history: list[Trade]) -> None:
    print("\nTrade History:")

    if not trade_history:
        print("(none)")
        return

    for trade in trade_history:
        print(
            f"Buy ID {trade.buy_id} matched with "
            f"Sell ID {trade.sell_id} "
            f"at Rs{trade.price} x {trade.quantity}"
        )


def main() -> None:
    buy_orders = []
    sell_orders = []
    trade_history = []

    order_id = 1

    print("Welcome to the Limit Order Book Simulator")
    print("------------------------------------------")
    print("This program simulates buy/sell order matching.")
    print("You will be asked to enter:")
    print("1. Order Type (buy or sell)")
    print("2. Quantity (e.g., 100)")
    print("3. Price (e.g., 55)")

    while True:
        order_type = input(
            "\nEnter Order Type (buy/sell): "
        ).strip().lower()

        if order_type not in ("buy", "sell"):
            print(
                "Invalid type. Please enter 'buy' or 'sell'."
            )
            continue

        try:
            quantity = int(input("Enter Quantity: "))
            price = int(input("Enter Price: "))

            if quantity <= 0 or price <= 0:
                print("Quantity and price must be positive.")
                continue

        except ValueError:
            print("Please enter valid whole numbers.")
            continue

        new_order = Order(
            order_id=order_id,
            order_type=order_type,
            price=price,
            quantity=quantity,
        )

        order_id += 1

        if order_type == "buy":
            # Negative price creates max-heap behaviour.
            heapq.heappush(
                buy_orders,
                (-new_order.price, new_order.id, new_order),
            )
        else:
            heapq.heappush(
                sell_orders,
                (new_order.price, new_order.id, new_order),
            )

        # Matching logic
        while buy_orders and sell_orders:
            buy_order = buy_orders[0][2]
            sell_order = sell_orders[0][2]

            if buy_order.price < sell_order.price:
                break

            traded_quantity = min(
                buy_order.quantity,
                sell_order.quantity,
            )

            trade_price = sell_order.price

            print(
                f"Trade Executed: Rs{trade_price} "
                f"x {traded_quantity}"
            )

            trade_history.append(
                Trade(
                    buy_id=buy_order.id,
                    sell_id=sell_order.id,
                    price=trade_price,
                    quantity=traded_quantity,
                )
            )

            heapq.heappop(buy_orders)
            heapq.heappop(sell_orders)

            if buy_order.quantity > traded_quantity:
                buy_order.quantity -= traded_quantity

                heapq.heappush(
                    buy_orders,
                    (
                        -buy_order.price,
                        buy_order.id,
                        buy_order,
                    ),
                )

            if sell_order.quantity > traded_quantity:
                sell_order.quantity -= traded_quantity

                heapq.heappush(
                    sell_orders,
                    (
                        sell_order.price,
                        sell_order.id,
                        sell_order,
                    ),
                )

        display_order_book(
            buy_orders=buy_orders,
            sell_orders=sell_orders,
        )

        display_trade_history(trade_history)

        continue_choice = input(
            "\nDo you want to enter another order? (y/n): "
        ).strip().lower()

        if continue_choice != "y":
            break

    print(
        "\nExiting Limit Order Book Simulator. Thank you!"
    )


if __name__ == "__main__":
    main()
