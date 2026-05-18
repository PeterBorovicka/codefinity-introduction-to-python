# Define the grocery_inventory dictionary with item details as (ID, category)
grocery_inventory = {
    "Milk":   (113, "Dairy"),
    "Eggs":   (116, "Dairy"),
    "Bread":  (117, "Bakery"),
    "Apples": (141, "Produce")
}
#Print the details of "Bread": Details of Bread: <$bread_details>.
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)

#After adding "Cookies", print the updated inventory: Inventory after adding Cookies: <$grocery_inventory>.
grocery_inventory["Cookies"] = (143, "Bakery")
print("Inventory after adding Cookies:", grocery_inventory)

#After removing "Eggs", print the updated inventory: Inventory after removing Eggs: <$grocery_inventory>.
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)





