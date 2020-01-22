# new_list = []
# for i in old_list:
#     if filter(i):
#         new_list.append(expressions(i))
# You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in old_list if filter(i)]


# [ expression for item in list if conditional ]
# This is equivalent to:
# for item in list:
#     if conditional:
#         expression

def halved(num_list):
    return [item / 2 for item in num_list]
print(halved([2, 4, 6, 8]))

def only_positive(num_list):
    return [item for item in num_list if filter(item > 0, num_list)]
    
print(only_positive([-2,-4, 6, 8]))