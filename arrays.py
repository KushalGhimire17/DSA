"""
list in python saves 'pointer to contents of list' in contagious memory
"""
new_list = [1, 2, 3]
result = new_list[0]

# search method 1
if 1 in new_list:
    print(True)

# search method 2
for n in new_list:
    if n == 1:
        print(True)
        break

# insertion
numbers = []  # currently allocates memory for one element
len(numbers)
numbers.append(2)
# 0,4,8,16,25,35,46.. triggers resize of list on these points
numbers.append(200)
numbers.extend([7, 9, 0])  # extend in a list
print(numbers)

# extend can be used instead of append
num = []
num.extend([4, 6, 8])
print(num)

# Update
num[0] = 2
print(num)
