# Sets Quiz 1
# Sets Quiz
# Question 1:
# What is the output of the following code?
# my_set = {1, 2, 3, 4, 5}
# print(len(my_set))
# a) 1
# b) 5
# c) 4
# d) 0

# ans: b

# Question 2:
# Which of the following methods is used to add an element to a set?
# a) add()
# b) insert()
# c) append()
# d) update()

# ans: a

# Question 3:
# Consider the following sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Which method would you use to find the elements that are common in both
# sets?
# a) intersection()
# b) union()
# c) difference()
# d) symmetric_difference()

# ans: a

# Sets Quiz 2
# Question 4:
# Which of the following statements about sets in Python is true?
# a) Sets are ordered collections of elements.
# b) Sets allow duplicate elements.
# c) Sets are mutable.
# d) Sets support indexing.

# ans: c


# Task 1: Set Intersection
# Write Python code to find and print the intersection of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {4, 5}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))

# Task 2: Set Union
# Write Python code to find and print the union of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))

# Task 3: Set Difference
# Write Python code to find and print the elements present in set1 but not in
# set2 :
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))

# Task 4: Set Symmetric Difference
# Write Python code to find and print the symmetric difference of the following
# two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.symmetric_difference(set2))

# Task 5: Set Membership Test
# Write Python code to check if the element 3 is present in the set my_set :
# my_set = {1, 2, 3, 4, 5}
# Your code here
# Output should be: True
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

# Exercise 1: Set Intersection
# Write a Python script that finds and prints the intersection of two sets.
set1 = {1, 4, 3, 4, 5}
set2 = {4, 5, 3, 7, 1}
print(set1.intersection(set2))

# Exercise 2: Set Union
# Write a Python script that finds and prints the union of two sets.
set1 = {"bunny","akhil","suuny"}
set2 = {"srikar","yashwanth"}
print(set1.union(set2))

# Exercise 3: Set Difference
# Write a Python script that finds and prints the difference between two sets.
set1 = {1, 2, 3, 3, 5}
set2 = {4, 5, 6, 3, 8}
print(set1.difference(set2))

# Exercise 4: Set Symmetric Difference
# Write a Python script that finds and prints the symmetric difference between
# two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 5}
print(set1.symmetric_difference(set2))