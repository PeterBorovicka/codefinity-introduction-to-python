# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

#empty list, total_sales_list, which you will populate with each product’s total sales.
total_sales_list = []

#to iterate over both keys and values of a dict you use the .items() method
for product, values in products.items():
    price_str, qty_str = values
    #convert the strings into the correct numeric types
    price = float(price_str)
    quantity = int (qty_str)
    total_sales = price * quantity
    print(f"Total sales for {product}: ${total_sales}")
    total_sales_list.append(total_sales)
    total_sum = sum(total_sales_list)

total_sum = sum(total_sales_list)
print(f"\nTotal sum of all sales: ${total_sum}")
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")