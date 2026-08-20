# Dictionary Quiz:
# Question 1:
# What is the output of the following code?
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(len(my_dict))
# a) 1
# b) 2
# c) 3
# d) 4

# ans: c

# Question 2:
# Which method is used to add a new key-value pair to a dictionary?
# a) add()
# b) insert()
# c) append()
# d) update()

# ans: d

# Question 3:
# Consider the following dictionary:
# my_dict = {'name': 'python', 'age': 30, 'city': 'Tadepalligud
# em'}
# How can you access the value associated with the key 'age'?
# a) my_dict.get('age')
# b) my_dict['age']
# c) my_dict.value('age')
# Dictionary Quiz: 2
# d) my_dict.retrieve('age')

# ans: b

# Question 4:
# What happens if you try to access a key that doesn't exist in a dictionary using
# square brackets notation?
# a) It returns None.
# b) It raises a KeyError.
# c) It returns False.
# d) It adds the key to the dictionary.

# ans: b

# Question 5:
# Which of the following methods returns a list of all the keys in a dictionary?
# a) keys()
# b) get_keys()
# c) all_keys()
# d) list_keys()

# ans: a

# Task 1: Dictionary Update
# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}
# Your code here
# Output should be: {'name': 'python', 'age': 25, 'city': 'west godavari'}
my_dict = {'name': 'python', 'age': 25}
my_dict.update({"city":"Nizamabad"})
print(my_dict)

# Task 2: Dictionary Access
# Write Python code to access and print the value associated with the key 'price' in
# the following dictionary:
# Dictionary Quiz: 3
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
# Your code here
# Output should be: 1200
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
s=product_info.get("price")
print(s)

# Task 3: Dictionary Removal
# Write Python code to remove the key-value pair with the key 'city' from the
# following dictionary:
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Your code here
# Output should be: {'name': 'John', 'age': 30}
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop("city")
print(my_dict)

# Task 4: Dictionary Keys
# Write Python code to print all the keys present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# Your code here
# Output should be: ['name', 'age', 'city']
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())

# Task 5: Dictionary Values
# Write Python code to print all the values present in the following dictionary:
# Dictionary Quiz: 4
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# Your code here
# Output should be: ['python', 25, 'tanuku']
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())


# Exercise 1: Dictionary Update
# Write a Python script that updates a dictionary with a new key-value pair.
dict={"app":"snap","Ram":4}
dict.update({"storage":64})
print(dict)

# Exercise 2: Dictionary Access
# Write a Python script that accesses and prints the value associated with a specific
# key in a dictionary.
dict={"app":"snap","Ram":4,"storage":64}
print(dict.get("app"))

# Exercise 3: Dictionary Removal
# Write a Python script that removes a key-value pair from a dictionary.
dict={"app":"snap","Ram":4,"storage":64}
dict.pop("app")
print(dict)

# Exercise 4: Dictionary Keys
# Write a Python script that prints all the keys present in a dictionary.
dict={"app":"snap","Ram":4,"storage":64,"name":"realme","year":2026}
s=dict.keys()
print(s)

# Exercise 5: Dictionary Values
# Write a Python script that prints all the values present in a dictionary.
dict={"app":"snap","Ram":4,"storage":64,"name":"realme","year":2026}
s=dict.values()
print(s)
