Number_list = list(range(1, 21))
Divisible_by_3 = []

print(f"The original List: \n {Number_list}")
for Number in Number_list:
    if Number % 3 ==0:
        Divisible_by_3.append(Number)

print(f"Number in list the divisible by 3: \n {Divisible_by_3}")
