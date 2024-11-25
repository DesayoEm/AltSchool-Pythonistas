# Given two lists, l1 and l2, 
# write a program to create a third list l3 by picking an odd-index element 
# from the list l1 and even index elements from the list l2.
#SOLUTION 1
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# l1 = l1[1::2] 
# l2 = l2[0::2]
# l1.extend(l2)
# print(l1)


# Write a program to remove the item present at index 4 and add it to the 2nd position and
# at the end of the list.

# list1 = [34, 54, 67, 89, 11, 43, 94]
# val=list1.pop(4)
# list1.insert(2, val)
# list1.append(val)
# print(list1)

# Slice list into 3 equal chunks and reverse each chunk

# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# length=len(sample_list)//3
# div=3
# l1=list(reversed(sample_list[:length]))
# l2=list(reversed(sample_list[div:div*2]))
# l3=list(reversed(sample_list[div*2:div*3]))
# print(l1)
# print(l2)
# print(l3)


# Create a Python set such that it shows the element from both lists in a pair


# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# res=set(zip(first_list, second_list))
# print(res)

# Find the intersection (common) of two sets and remove
#  those elements from the first set

# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# first_set.difference_update(second_set)
# print(first_set)


# Exercise 7: Checks if one set is a subset or superset of another set. 
# If found, delete all elements from that set

# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

# print(first_set.issubset(second_set))
# print(second_set.issubset(first_set))

# print(first_set.issuperset(second_set))
# print(second_set.issuperset(first_set))

# if first_set.issubset(second_set):
#     first_set.clear()
# else:
#     pass

# print(first_set)
# print(second_set)

# Iterate a given list and check if a given element exists as a key’s value in 
# a dictionary. If not, delete it from the list

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]

# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# roll_number=[item for item in roll_number if item in sample_dict.values()]
# print(roll_number)

# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates


# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# outcome=list({value for value in speed.values()})
# print(outcome)

# Exercise 10: Remove duplicates from a list and create a tuple 
# and find the minimum and maximum number

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# unique_items=tuple(set(sample_list))
# print(unique_items)
# print(min(unique_items))
# print(max(unique_items))