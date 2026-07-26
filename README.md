# Trade Matcging Engine Simulator

A terminal-based **Limit Order Book Simulator** built in Python.  
This project simulates how buy and sell orders are placed, stored, matched, and executed in a basic trading system.

The simulator uses **heap data structures** to maintain order priority and execute trades based on price conditions.

---

## Project Overview

In financial markets, a limit order book stores buy and sell orders for a particular asset.  
Buyers place buy orders at a price they are willing to pay, and sellers place sell orders at a price they are willing to accept.

A trade is executed when the highest buy price is greater than or equal to the lowest sell price.

This project demonstrates the basic working of an order matching system using Python.

---

## Features

- Add buy and sell orders from the terminal
- Match orders automatically when prices are compatible
- Uses max-heap behavior for buy orders
- Uses min-heap behavior for sell orders
- Supports partial order matching
- Displays current buy orders
- Displays current sell orders
- Maintains trade execution history
- Handles invalid input safely

---

## Technologies Used

- Python
- heapq module
- Object-Oriented Programming

---

## Data Structures Used

### Buy Orders

Buy orders are stored using a heap with negative prices.

Python's `heapq` module works as a min-heap by default.  
To create max-heap behavior for buy orders, prices are stored as negative values.

Example:

```python
heapq.heappush(buy_orders, (-price, order_id, order))
```

This ensures that the highest buy price gets priority.

### Sell Orders

Sell orders are stored using a normal min-heap.

Example:

```python
heapq.heappush(sell_orders, (price, order_id, order))
```

This ensures that the lowest sell price gets priority.

---

## Order Matching Logic

The simulator checks the best buy order and the best sell order.

A trade is executed when:

```python
buy_order.price >= sell_order.price
```

If the buy price is lower than the sell price, no trade happens.

The traded quantity is calculated as:

```python
traded_quantity = min(buy_order.quantity, sell_order.quantity)
```

This allows partial matching when one order has more quantity than the other.

---

## How to Run

### Step 1: Clone the Repository

```bash
git clone <your-repository-link>
```

### Step 2: Open the Project Folder

```bash
cd limit-order-book-simulator
```

### Step 3: Run the Python File

```bash
python3 main.py
```

If you are using Windows, you can try:

```bash
python main.py
```

---

## Sample Input and Output

```text
Welcome to the Limit Order Book Simulator
------------------------------------------
This program simulates buy/sell order matching.

Enter Order Type (buy/sell): buy
Enter Quantity: 100
Enter Price: 55

Current Buy Orders:
[Rs55 x 100] (ID 1)

Current Sell Orders:
(none)

Trade History:
(none)

Do you want to enter another order? (y/n): y

Enter Order Type (buy/sell): sell
Enter Quantity: 50
Enter Price: 50

Trade Executed: Rs50 x 50

Current Buy Orders:
[Rs55 x 50] (ID 1)

Current Sell Orders:
(none)

Trade History:
Buy ID 1 matched with Sell ID 2 at Rs50 x 50
```

---

## Example Explanation

Suppose a buy order is placed for 100 quantity at Rs55.

Then a sell order is placed for 50 quantity at Rs50.

Since the buy price Rs55 is greater than the sell price Rs50, a trade is executed.

Only 50 quantity is matched, so the remaining 50 quantity of the buy order stays in the order book.

---

## Concepts Demonstrated

- Object-Oriented Programming
- Classes and objects
- Constructor usage
- Heap data structure
- Priority-based order matching
- Partial order execution
- Input validation
- Trade history tracking

---

## Classes Used

### Order Class

The `Order` class stores details of each order.

Attributes:

- Order ID
- Order type
- Price
- Quantity

### Trade Class

The `Trade` class stores details of executed trades.

Attributes:

- Buy order ID
- Sell order ID
- Trade price
- Trade quantity

---

## Interview Explanation

This project is a Python-based limit order book simulator.  
It simulates how buy and sell orders are matched in a trading system.

I used Python's `heapq` module to maintain priority between orders.  
For buy orders, I used negative prices to create max-heap behavior, so the highest buy price gets priority.  
For sell orders, I used normal prices, so the lowest sell price gets priority.

The system compares the best buy order and best sell order.  
If the buy price is greater than or equal to the sell price, a trade is executed.  
It also supports partial matching, where if one order has more quantity than the other, the remaining quantity is added back to the order book.

Through this project, I learned about heap data structures, priority-based matching, object-oriented programming, and how basic trading systems work.

---

## Future Improvements

- Add support for market orders
- Add order cancellation feature
- Add CSV file logging
- Add user authentication
- Add graphical user interface
- Add real-time price chart
- Store orders and trades in a database

---

## Author

**Shashank Kumar**

