
def product_details(pid, name, quantity, price):
    return (
        f"Product ID: {pid}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )

print(product_details(101, "Laptop", 2, 45000))
