discounted = False
lowStock = True
movingProduct = discounted or lowStock
#print(movingProduct)
promotion = (not discounted) and (not lowStock)
print("Is the item eligible for promotion?", promotion)
