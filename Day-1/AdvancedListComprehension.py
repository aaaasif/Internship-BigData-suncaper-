# Given lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = []

for x in list1:
    for y in list2:
        product = x * y
        if product % 3 == 0:
            result.append(product)

print(result)