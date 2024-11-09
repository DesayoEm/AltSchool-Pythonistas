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


# Write a program to add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#SOLUTION
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# You have given a nested list.
# Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way 
# that it will look like the following list.

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# Expected Output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
# sub list to add
#sub_list = ["h", "i", "j"]


# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]

# #Solution
# list1[2][1][2].extend(sub_list)
# print(list1)


# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of an item.

# Given:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:
# [5, 10, 15, 200, 25, 50, 20]

# #SOLUTION 1
# list1 = [5, 10, 15, 20, 25, 50, 20]
# i=list1.index(20)
# print(i)
# list1[i]=200
# print(list1)

#SOLUTION2
# def replace_item(item, sub, _list: list):
#     for index, value in enumerate(_list):
#         if _list[index] == item:
#             _list[index] = sub
#             break
#     return _list
    
# list1 = [5, 10, 15, 20, 25, 50, 20]
# print(replace_item(20, 200, list1))

#SOLUTION 3
# def replace_item(item, sub, _list):
#     i = _list.index(item)
#     _list[i] = sub
#     return _list
    
# list1 = [5, 10, 15, 20, 25, 50, 20]
# print(replace_item(20, 200, list1)) 


# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]

#SOLUTION2
# [5, 15, 25, 50]
# list1=[i for i in list1 if i != 20]
# print(list1)
#[item for item in iterable if condition]

# #  SOLUTION 3
# def remove_occurrence(item, _list):
#     while item in _list:
#         _list.remove(item)

#     return _list
    
# list1 = [5, 10, 15, 20, 25, 50, 20]
# print(remove_occurrence(20, list1)) 



# def remove_item():
#     if num==20:
#         del[num] #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        
# list1=list(filter(remove_item(),list1))
# print(list1)