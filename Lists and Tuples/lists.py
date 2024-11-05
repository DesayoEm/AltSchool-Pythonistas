# Exercise 1: Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1) 

# SOLUTION 2
# list2= list(reversed(list1))
# print(list2)

# SOLUTION 3
# list1=list1[::-1]
# print(list1)

# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise.
#  
# Create a new list that contains the 0th index item from both the list, then the 1st index item
# and so on till the last element. any leftover items will get added at the end of the new list.
# ['My', 'name', 'is', 'Kelly']


# list1 = ["M", "na", "i", "Ke", "wwt", "wwt"]
# list2 = ["y", "me", "s", "lly"]
# list1_len=len(list1)
# list2_len=len(list2)


# length=list1_len if list1_len<list2_len else list2_len

# if list1_len==list2_len:
#     pass
# elif list2_len > length:
#     rem=list2[length:]
# else:
#     rem=list1[length:]
# print (rem)

# list3=list(zip(list1,list2))
# list4=[x+y for x, y in list3]
# list4.extend(rem)
# print(list4)

# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# numbers = [1, 2, 3, 4, 5, 6, 7]
# result=[x*x for x in numbers]
# print(result)

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# # print(list3)
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# list3=[x+y for x in list1 for y in list2]
#DEMO USING NESTED LOOPS
# for x in list1:
#     for y in list2:
#         z=x+y
#         print(z)

# Given a two Python list.
# Write a program to iterate both lists simultaneously and display items from list1 in 
# original order and items from list2 in reverse order.

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list3=list(zip(list1,list2[::-1]))
# for s,y in list3:
#     print(s, y)

# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# SOLUTION 1
# list2=[item for item in list1 if item.isalnum()]
# SOLUTION 2
# list2=[item for item in list1 if item != ""]
# SOLUTION 3
# list2=list(filter(None, list1))
# print(list2)
