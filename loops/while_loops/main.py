start_number = 5
#empty list to hold each number
countdown_values = []

current = start_number

#checks current 
while current >= 1:
    #add current to the list
    countdown_values.append(current)
    #decrease current by one in the loop
    current -= 1

print("Discount countdown complete!")
print(countdown_values)