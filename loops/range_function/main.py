# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Loop over indices 0–4 using range()
for i in range(len(weekdays)):
    weekday = weekdays[i]
    promotion = daily_promotions[i]
    print(f"{weekday}: Promotion on {promotion}")