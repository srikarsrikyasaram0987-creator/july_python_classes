# Question 1:
# What is the output of the following code?
# my_list = [10, 20, 30, 40, 50]
# print(my_list[1:4])
# a) [20, 30, 40]
# b) [10, 20, 30]
# c) [30, 40, 50]
# d) [20, 40, 50]

# ans: a

# Question 2:
# Which method is used to add multiple elements to the end of a list?
# a) add()
# b) append()
# c) extend()
# d) insert()

# ans: c

# Question 3:
# Consider the following list:
# fruits = ['apple', 'banana', 'orange']
# How can you remove 'banana' from the list?
# a) fruits.remove('banana')
# b) fruits.delete('banana')
# c) fruits.pop('banana')
# d) fruits.exclude('banana')

# ans: a

# Question 4:
# What does the len() function return when applied to a list?
# Quiz Questions: 2
# a) The sum of all elements in the list
# b) The average of all elements in the list
# c) The number of elements in the list
# d) The maximum element in the list

# ans: c

# Question 5:
# Which of the following list comprehensions generates a list of even numbers
# from 0 to 10?
# a) [x for x in range(11) if x % 2 == 0]
# b) [x for x in range(10) if x % 2 == 0]
# c) [x**2 for x in range(11)]
# d) [x**2 for x in range(10) if x % 2 == 0]

# ans: a

# Task 1:
# Reverse List:
# Write Python code to reverse the order of elements in the given list my_list .
# Print the reversed list.
# my_list = [10, 20, 30, 40, 50, 11]
# Your code here
# Output should be: [11,50,40,30,20,10]

my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()
print(my_list)

# Task 2:
# Common Elements:
# Given two lists list1 and list2 , find and print the common elements between
# them.
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# Your code here

emptylist=[]
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
for i in list1:
    for j in list2:
        if i==j:
            emptylist.append(i)
print(emptylist)       

# Task 4:
# Remove Duplicates:
# Remove duplicate elements from the given list duplicated_list and print the list
# without duplicates while preserving the order.
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]

emptylist=[]
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
for i in duplicated_list:
    if i not in emptylist:
        emptylist.append(i)
print(emptylist)

# Exercise 1: List Concatenation
# Write a Python script that concatenates two lists and prints the result.

list1=[1,2,3,4,5]
list1.extend([6,7,8,9,10])
print(list1)

# Exercise 2: List Repetition
# Write a Python script that repeats a list three times and prints the result.

list=[1,2,3,4]
for i in range(3):
    print(list)

# Exercise 3: List Removal
# Write a Python script that removes the elements at even indices from a list.

list=[1,2,3,4,5,6,7,8,9,10]
print(list[0::2])

# Exercise 4: List Insertion
# Quiz Questions: 4
# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
# a list

list=[1,2,3]
list.insert(0,10)
list.insert(0,11)
list.insert(0,12)
print(list)

# List comprehensions
# 1. Square Numbers: Create a list of squares of numbers from 1 to 10.

res=[i for i in range(1,11) ]
print(res)

# 2. Even Numbers: Generate a list of even numbers from 1 to 20.

even=[i for i in range(1,21) if i%2==0]
print(even)

# 3. Words Lengths: Given a list of words, create a list containing the lengths of
# each word.
# words = ["apple", "banana", "cherry", "date"]

words = ["apple", "banana", "cherry", "date"]
list=[]
for i in words:
    list.append(len(i))
print(list)
