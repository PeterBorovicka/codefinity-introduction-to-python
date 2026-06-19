# Definition of dictionary
grocery_inventory = {
# Key Milk maps to a tuple (immutable sequence type—much like a list, but once you create it you cannot change (add, remove, or reassign) its item) with 3 elements    
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}
# Check Eggs price and reduce if needed - it's 5.50 as seen above - 2nd element with index 1 for Eggs
eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],
        eggs_price - 1,
        grocery_inventory["Eggs"][2],
    )
else:
    print("The price of Eggs is reasonable.")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes: ", grocery_inventory)

# Store the current "Milk" stock in a variable named milk_stock. If it is below 10, add 20 units and print "Milk needs to be restocked. Increasing stock by 20 units." Otherwise, print "Milk has sufficient stock.

milk_stock = grocery_inventory["Milk"][2]

if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        milk_stock + 20,
    )
else:
    print("Milk has sufficient stock.")

# If "Apples" price exceeds 2$, remove it and print "Apples removed from inventory due to high price."
apples_price = grocery_inventory["Apples"][1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
 
print("Updated inventory:", grocery_inventory)