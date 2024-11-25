# tuple1 = (10, 20, 30, 40, 50)

# SOL1
# # print(tuple1[::-1])

# SOL2
# tuple2=tuple(reversed(tuple1))
# print(tuple2)

# SOL3  
# tuple2=list(tuple1)
# tuple2.reverse()
# print(tuple(tuple2))



# Exercise 2: Access value 20 from the tuple
# The given tuple is a nested tuple. write a Python program to print the value 20.

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])

# Exercise 3: Create a tuple with single item 50
# tuptup=(50,)
# print(tuptup)
# print(type(tuptup))


# Exercise 4: Unpack the tuple into 4 variables
# Write a program to unpack the following tuple into four variables and display each variable.

# tuple1 = (10, 20, 30, 40)
# a, b, c, d = tuple1

# print(type(d))


# Exercise 5: Swap two tuples in Python
# Given:

# tuple1 = (11, 22)
# tuple2 = (99, 88)

# SOLUTION1
# tuple1, tuple2 = tuple2, tuple1
# print(tuple1)
# print(tuple2)

# SOLUTION2
# if tuple1 != tuple2:
#     t1=tuple1
#     tuple1=tuple2
#     tuple2=t1

# print(tuple1)
# print(tuple2)

# SOLUTION3
# def swap_tuptup(t1, t2):     
#     return t2, t1 
# tuple1, tuple2 = swap_tuptup(tuple1, tuple2)  
# print("tuple1:", tuple1)   
# print("tuple2:", tuple2)

# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

# tuple1 = (11, 22, 33, 44, 55, 66)
# SOLUTION1
# tuple2=tuple1[3:5]
# print(tuple2)

# SOLUTION2
# tuple2 = [item for item in tuple1 if item == 44 or item == 55]
# tuple2=tuple(tuple2)
# print(tuple2)

# SOLUTION 3
# tuple2 = tuple(x for x in tuple1 if x == 44 or x == 55)
# print(tuple2)  

# Exercise 7: Modify the tuple
# Given is a nested tuple. 
# Write a program to modify the first item (22) of a list inside a following tuple to 222
# tuple1 = (11, [22, 33], 44, 55)

# tuple1[1][0]=222
# print(tuple1)

# Exercise 8: Sort a tuple of tuples by 2nd item

# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# (('c', 11), ('a', 23), ('d', 29), ('b', 37))

# def get_num(num):
#     return num[1]

# tuple2=tuple(sorted(tuple1, key=get_num))
# print(tuple2)

# Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
# countx=tuple1.count(50)
# print(countx)

# Exercise 10: Check if all items in the tuple are the same
# tuple1 = (45, 45, 45, 45)

# SOLUTION 1
# if tuple1[0]==tuple1[1]==tuple1[2]==tuple1[3]:
#     print(True)
# else:
#     print(False)


# SOLUTION 2
# check_num=min(tuple1)==max(tuple1)
# print(check_num)

# # num=45
# if any(item !=45 for item in tuple1):
#     print (False)
# else:
#     print(True)


print(globals())