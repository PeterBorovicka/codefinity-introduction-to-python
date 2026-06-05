prices = [29.99, 45.50, 12.75, 38.20]
for cost in range(len(prices)):
    # Apply the discount by reducing the price
    if cost == 0:
        rate = 0.10
    elif cost == 1:
        rate = 0.20
    elif cost == 2:
        rate = 0.15
    else:           # cost == 3
        rate = 0.05
    
    prices[cost] = prices[cost] * (1 - rate)
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")



