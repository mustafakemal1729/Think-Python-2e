
"""
2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

"""

number_of_copy = 60
# Shipping cost = $3 for the first, $0.75 for each additional copy
shipping_costs = 3 + round((0.75 * (number_of_copy - 1)))
cover_price = (24.95 * 6)/10
wholesale_cost = number_of_copy * cover_price + shipping_costs
print(f"The total cost is: {round(wholesale_cost, 2)}")
