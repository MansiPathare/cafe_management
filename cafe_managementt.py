import qrcode
from PIL import Image

# Define the menu with items and prices in INR
menu = {
    "Coffee": 3.00,
    "Tea": 2.50,
    "Sandwich": 5.00,
    "Salad": 4.00,
    "Cake": 3.50
}

# Define orders and QR codes
orders = {}
table_qr_codes = {i: f"QR_{i}" for i in range(1, 6)}  # Simulate 5 tables with unique QR codes

def generate_qr_codes():
    """Generate and save QR codes for each table."""
    for table, qr_code in table_qr_codes.items():
        img = qrcode.make(qr_code)
        img.save(f"table_{table}.png")
        print(f"Generated QR code for Table {table}: {qr_code} (saved as table_{table}.png)")

def display_menu():
    """Display the café menu."""
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

def take_order(table_number):
    """Take the order from the user for a given table number."""
    print(f"\nTable {table_number} Order")
    while True:
        display_menu()
        order_item = input("Enter the item you want to order (or type 'done' to finish): ").strip().title()
        if order_item.lower() == 'done':
            break
        elif order_item in menu:
            quantity = int(input(f"Enter the quantity for {order_item}: "))
            if table_number not in orders:
                orders[table_number] = []
            orders[table_number].append((order_item, quantity))
        else:
            print("Item not found in the menu. Please try again.")

def generate_bill(table_number):
    """Generate and display the bill for a given table number."""
    if table_number not in orders:
        print(f"No orders found for Table {table_number}")
        return
    print(f"\nBill for Table {table_number}:")
    total_cost = 0
    for item, quantity in orders[table_number]:
        item_cost = menu[item] * quantity
        total_cost += item_cost
        print(f"{item} (x{quantity}): ₹{item_cost}")
    print(f"Total Cost: ₹{total_cost}")

def start_cafe_management_system():
    """Start the café management system."""
    print("Welcome to our café!")

    # Show available QR codes for tables
    print("Available QR Codes for Tables (images saved as table_<number>.png):")
    for table, qr in table_qr_codes.items():
        print(f"Table {table}: {qr}")

    generate_qr_codes()

    while True:
        qr_code = input("\nEnter your table's QR code (or type 'exit' to quit): ").strip()
        if qr_code.lower() == 'exit':
            break

        # Find the table number based on the entered QR code
        table_number = None
        for table, qr in table_qr_codes.items():
            if qr == qr_code:
                table_number = table
                break

        if table_number is not None:
            take_order(table_number)
            generate_bill(table_number)
        else:
            print("Invalid QR code. Please try again.")

# Start the café management system
start_cafe_management_system()
