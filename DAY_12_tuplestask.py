# numbers = (10,20,10,30,10)
# print(numbers.count(10))

# fru=("cat","dog","snake")
# print(fru.index("snake"))

# t1=("kyasaram")
# t2=("srikar")
# s=t1+t2
# print(s)

# t=("om",)
# print(t*3)

# f=(1,2,3)
# print(1 in f)

# f=("cat","dog","snake")
# print(len(f))

# numbers = (10,50,20)
# print(max(numbers))

# numbers = (10,50,20,5,43,72,23)
# print(min(numbers))

# numbers = (10,20,30)
# print(sum(numbers))

# """Tuple operations"""

# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A.union(B))

# A = {1, 2, 3,3,3,4,4,5}
# B = {4,5,6,7,8}
# print(A.intersection(B))

# A = {1, 2, 3}
# B = {2, 4}
# print(A.difference(B))

# A = {1, 2}
# B = {3, 4,2}
# print(B.isdisjoint(A))

# A = {1, 2}
# B = {1, 2, 3, 4}
# print(B.issubset(A))

# A = {1, 2, 3, 4}
# B = {2, 3}
# print(A.issuperset(B))

# A = frozenset([1, 2, 3])
# A.add(4)

# Quiz Questions: 1
# Quiz Questions:
# 1. Question 1:
# What does the
# all() function return when applied to an empty tuple?
# A) True
# B) False
# C) Error

# ans: a

# 2. Question 2:
# Which of the following statements correctly creates a tuple?
# A) my_tuple = [1, 2, 3]
# B) my_tuple = (1, 2, 3)
# C) my_tuple = {1, 2, 3}

# ans: b

# 3. Question 3:
# What is the output of the following code snippet?
# my_tuple = (1, 2, 3)
# print(len(my_tuple))
# A) 1
# B) 2
# C) 3

# ans: c

# 4. Question 4:
# Which of the following statements about tuples in Python is true?
# A) Tuples are mutable.
# B) Tuples can only store elements of the same data type.
# C) Tuples use parenthesis ( ) for declaration.

# ans: c

# Coding Exercise:
# 1. Create a Tuple: Write a program that creates a tuple containing three
# elements: your name, your age, and your favorite color. Then print the tuple
tuple_1=("Srikar",20,"orange")
print(tuple_1)

# Quiz Questions: 2
# 2. Access Tuple Elements: Write a program that creates a tuple containing the
# days of the week. Then, print the third element of the tuple.
Days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(Days[2])

# 3. Tuple Concatenation: Write a program that creates two tuples, one
# containing odd numbers from 1 to 5 and another containing even numbers
# from 2 to 6. Concatenate these two tuples and print the result.
Tuple_1=(1,3,5)
Tuple_2=(2,4,6)
obj=Tuple_1+Tuple_2
print(obj)

# 4. Tuple Unpacking: Write a program that defines a tuple containing the
# dimensions of a rectangle (length and width). Then, unpack this tuple into
# two variables and calculate the area of the rectangle.
Rectangle=(20,34)
length,width=Rectangle
print(f"The area of the rectangle:{length*width}")

# 5. Check if an Element Exists: Write a program that checks if a given element
# exists in a tuple.
Tuple=(1,2,"dog","ball")
print("dog" in Tuple)

# 6. Write a Python program to generate a bill for a supermarket purchase. The
# program should store the items and their prices in a list of tuples. It should
# then iterate over this list to print out each item along with its price. Finally,
# calculate and print the total cost of all the items
# Sample Input:
# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# Sample Output:
# Item Price
# --------------------
# Apple 99.00
# Banana 99.00
# Milk 49.00
# --------------------
# Total 247.00

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
sum=0
print("Item\tPrice")
print("-"*25)
for i,j in items:
    print(i,float(j))
    sum+=float(j)
print("-"*25)
print("Total",sum)
print("-"*25)

