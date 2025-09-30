Item_one = 30
Item_two = 50
Item_three = 80

total_budget = 180

total_cost = Item_one + Item_two + Item_three

print("Total cost of items:", total_cost)
print("Budget:", total_budget)

if total_cost > total_budget :
    money_needed = total_cost - total_budget
    print("Ypu are over budget yo need money:", money_needed)
elif total_cost < total_budget:
    money_left = total_budget - total_cost
    print("You have Extra money:", money_left)
else:
    print("Palanced cost")