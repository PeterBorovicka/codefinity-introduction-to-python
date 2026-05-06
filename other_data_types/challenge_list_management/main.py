# 1–2: Initialize
meat     = ["Ham",     3.99,  50,  "Sliced"]
cheese   = ["Cheddar", 5.49, 100, "Sharp"]
condiment= ["Mustard", 1.99,  75,  "Spicy"]

# 3: Main list & initial print
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)

# 4: Restock Ham if needed
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

# 5: Add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# 6: Remove condiment
deli_dept.remove(condiment)

# 7: Sort alphabetically by item name
deli_dept.sort()

# 8: Final print
print("Updated Deli List:", deli_dept)
