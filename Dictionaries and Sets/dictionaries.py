# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# result = dict(zip(keys, values))
# print(result)

# result2={x:y for x in keys for y in values}
# print(result2)


# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)

# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])

# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# {'Kelly': {'designation': 'Developer', 'salary': 8000}, \
#  'Emma': {'designation': 'Developer', 'salary': 8000}}

# value=dict.fromkeys(employees, defaults)
# print(value)


# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# keys = ["name", "salary"]
# # Keys to extract
# keys = ["name", "salary"]


#SOLUTION 1
# our_dict={key:sample_dict[key] for key in keys}

#SOLUTION 2
# our_dict={key:values for key, values in sample_dict.items() if key in keys}
# print(our_dict)

#DELETE A LIST OF KEY FROM A dict

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]
#SOLUTION 1
# our_dict={key:values for key, values in sample_dict.items() if key not in keys}
# print(our_dict)

#SOLUTION 2
# for item in keys:
#     sample_dict.pop(item)
# print(sample_dict)

#SOLUTION 3
# for item in keys:
#     del [sample_dict[item]]
# print(sample_dict)

# Exercise 7: Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.

# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# for item in sample_dict.values():  
#     if item == 200:
#         print("200 dey")


# Write a program to rename a key city to a location in the following dictionary.


# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "city": "New york",
#   "salary": 8000,
# }

# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

# sample_dict.pop("city")
# sample_dict.update({"location":"New York"})
# print(sample_dict)

# Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Mathsjnlkdmpjeewo': 65,
#   'history': 75
# }

# for item, value in sample_dict.items():
#     if value == min(sample_dict.values()):
#         print(item)

# print(min(sample_dict, key=sample_dict.get))

# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
# sample_dict["emp3"]["salary"]=8500

# print(sample_dict)

#SOLUTION 2
# def update_salary(dicto: dict, salary: int, employee: str):
#     for item , value in dicto.items():
#         if value["name"] == employee:
#             value["salary"]= salary

#     return dicto
# print(update_salary(sample_dict, 8500, "Brad"))

