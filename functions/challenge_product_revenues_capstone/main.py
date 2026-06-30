# 1) Define your functions first

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        # Multiply the price and quantity at the same index i
        rev = prices[i] * quantities_sold[i]
        # Append that result into the revenue list
        revenue.append(rev)
    return revenue

def formatted_output(revenues):
    for prod, rev in sorted(revenues):
        print(f"{prod} has total revenue of ${rev}")

# 2) Then initialize data and call them

products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)