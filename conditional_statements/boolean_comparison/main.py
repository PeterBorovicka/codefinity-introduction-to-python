#Making both booleans True in the output of this script
total_costs = 20
discount_eligible = total_costs >= 20.00

#Following parameter's value change does not change the output of the boolean
total_costs = 10
#Following parameter's value changes the output line with its numeric value
#discount_eligible = 21

# Define the quantity of the item and the low stock threshold
milk_quantity = 12
low_stock_threshold = 13

# Check if the item quantity is below the low stock threshold
low_stock = milk_quantity <= low_stock_threshold

# Print the result
print("Is the item low in stock?", low_stock)
print("Is the purchase eligible for a discount?", discount_eligible)