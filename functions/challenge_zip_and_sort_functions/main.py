# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Task: Combine into a list of tuples
combined_list = list(zip(products, prices, quantities_sold))
[('Banana', 1.2, 50),
 ('Apple', 0.5, 100),
 ('Mango', 2.5, 25),
 ('Cherry', 1.75, 40)]

sorted_products = sorted(combined_list)
for name, price, qty in sorted_products:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {qty}")

    
