produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# 1. Combine the two lists into one list of sections
groceries = [produce, dairy]

# 2. Outer loop over each section (produce, then dairy)
for section in groceries:
    # 3. Inner loop over each item in the current section
    for item in section:
        # 4. Print in the required format
        print("Item name:", item)