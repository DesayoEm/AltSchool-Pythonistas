# import os

# def multiply(x,y):
#     return x*y


# x=int(input("Enter your first number"))
# y=int(input("Enter your second number"))

# print(multiply(x,y))

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Use the print() function to format the given words in the mentioned format. 
# Display the ** separator between each string.

# Expected Output:

# For example: print('Name', 'Is', 'James') will display Name**Is**James
# a="Name"
# b="Is"
# c="James"

# my_tuple=(a, b, c)
# old_string = '**'.join(my_tuple) 
# print(old_string)

# print('My', 'Name', 'Is', 'James', sep='**')


# Exercise 3: Convert Decimal number to octal using print() output formatting
# num = 8
# Expected Output:
# The octal number of decimal number 8 is 10

# num = 8
# print('%o' % num)    
            
# Exercise 4: Display float number with 2 decimal places using print()
# num = 458.547315

# print('%.2f' % num)

# print(round(num, 2))

# print(format((num),'.2f'))

        
# Exercise 5: Accept a list of 5 float numbers as an input from the user
# list1=[]
# while len(list1) < 5:
#     num=float(input("Please enter a number"))
#     list1.append(num)

# print(list1)

# list1=[]
# for i in range(5):
#     num=float(input("Please enter a number"))
#     list1.append(num)

# print(list1)

# list1=[]
# while True:
#     num=float(input("Please enter a number"))
#     list1.append(num)
#     if len(list1)==5:
#         break

# print(list1)

# Exercise 7: Accept any three string from one input() call
# Write a program to take three names as input from a user in the single input() function call.


# a,b,c=input("Enter 3 names").split(" ")

# print(a)
# print(b)
# print(c)

# totalMoney = 1000
# quantity = 3
# price = 450

# print(f"I have {totalMoney} dollars so I can buy {quantity} football for {(price):.2f} dollars.")  

# Write a program to check if the given file is empty or not 
# import os

# size = os.stat("new_file.txt").st_size
# if size == 0:
#     print('file is empty')        


# Exercise 10: Read line number 4 from the following file

# with open('file.txt', 'r') as file:
    # while True:
    #      content=file.readline()
    #      if "4" in content:
    #         break
    # print (content)
   

    

    


      






