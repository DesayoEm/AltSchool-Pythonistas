# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)

# Return a new set of identical items from two sets
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1=set1.intersection(set2)
# print(set1)

# Exercise 3: Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates.

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# unique=set1.union(set2)-set1.intersection(set2)
# print(unique)

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1=set1-set2
# print(set1)

# Exercise 5: Remove items from the set at once
# Write a Python program to remove items 10, 20, 30 from the following set at once.

# Given:

# set1 = {10, 20, 30, 40, 50}
# val=(10, 20, 30)
# # set1={item for item in set1 if item not in val}
# # print(set1)

# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})
# print(set1)