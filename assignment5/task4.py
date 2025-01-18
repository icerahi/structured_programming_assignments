#Task 4: Inventory Management System with Sales Tracking


inventory = {
    "P001": {"name": "Product 1", "quantity": 100, "price": 10},
    "P002": {"name": "Product 2", "quantity": 50, "price": 20},
    "P003": {"name": "Product 3", "quantity": 75, "price": 15},
}

sales = []

def display_inventory():
    print("\nInventory Status:")
    for product_id, details in inventory.items():
        print(f"{product_id}: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")

def record_sale(product_id, quantity, date):
    if product_id in inventory:
        if inventory[product_id]["quantity"] >= quantity:
            inventory[product_id]["quantity"] -= quantity
            sales.append({"product_id": product_id, "quantity": quantity, "date": date})
            print("Sale recorded.")
        else:
            print("Insufficient stock.")
    else:
        print("Invalid product ID.")

def display_sales_report():
    print("\nSales Report:")
    total_sales = 0
    for sale in sales:
        product = inventory[sale["product_id"]]
        sale_total = sale["quantity"] * product["price"]
        total_sales += sale_total
        print(f"Date: {sale['date']}, Product: {product['name']}, Quantity Sold: {sale['quantity']}, Total: {sale_total}")
    print(f"Total Sales: {total_sales}")

while True:
    print("\n1. Display Inventory\n2. Record Sale\n3. Display Sales Report\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        display_inventory()
    elif choice == "2":
        product_id = input("Enter Product ID: ")
        quantity = int(input("Enter Quantity Sold: "))
        date = input("Enter Date (YYYY-MM-DD): ")
        record_sale(product_id, quantity, date)
    elif choice == "3":
        display_sales_report()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
