import re

def halved(num_list):
    return [item / 2 for item in num_list]
print(halved([2, 4, 6, 8]))

def only_positive(num_list):
    return [item for item in num_list if item > 0]
print(only_positive([-2,-4, 6, 8]))

def total(lst):
    return sum(lst)
print(total([2, 4]))

def stripped_strings(lst):
    return [re.sub("\W", "", string) for string in lst]
print(stripped_strings(["hello123124.....", "213412isfs"]))




def valid_contacts(lst):
    return [contact for contact in lst if len(contact.phone_number) == 10]