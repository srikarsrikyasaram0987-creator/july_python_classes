"""Quiz Questions:5

Question 1:
What is the purpose of the for loop in Python?
a) To check a condition and execute a block of code if it's true.
b) To repeatedly execute a block of code for each element in a sequence.
c) To perform arithmetic operations.
d) To define a function.

ans: b

Question 2:
How do you iterate over a range of numbers in a for loop?
a) Using the enumerate() function.
b) Using the range() function.
c) Using the while loop.
d) Using the list() function.

ans: b

Question 3:
When does a while loop stop executing?
a) When the loop variable reaches the end of the sequence.
b) When the loop condition becomes false.
c) When the loop variable is equal to a specific value.
d) When the loop is explicitly terminated using break.

ans: b

Question 4:
What does the while loop syntax look like in Python?
a)for variable in iterable:
b)while condition:
c)if condition:
d)loop while condition:

ans: b
"""
"""Exercise 1: Sum of Squares
Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop."""
sum=0
for i in range(1,6):
    res=i**2
    sum=sum+res
    print(f"square of {i} is {res}")
print("Sum is",sum)

"""Exercise 2: Countdown
Write a Python program that uses a while loop to print a countdown from 5 to 1."""  
count=5
while count>=1:
    print("countdown",count)
    count=count-1

"""Exercise 3: Multiplication Table with Nested For Loop
Write a Python program to print the multiplication table for a user-specified number using a nested for loop."""
num1=int(input("Enter any table:"))
for i in range(1,11):
    for j in range(1):
        print(f"{num1} x {i}={num1*i}")

"""Exercise 4:
Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive)."""
sum=0 
for i in range(0,11):
    if i%2==0:
        sum=sum+i
print("sum of even",sum)

"""Exercise 5:
Calculate the sum of all numbers from 1 to a given number"""
num=int(input("Enter the num: "))
s=0
for i in range(1,num+1):
    s=s+i
print("Sum is :",s)

"""Exercise 6:
Display numbers from a list using loop"""
list=[20,32,45,89] 
for i in list:
    print(i)

"""Exercise 7:
Display numbers from -10 to -1 using for loop"""
for i in range(-10,0):
    print(i)

"""Exercise 8:
Write a Python program to print the cube of all numbers from 1 to a given number"""
num=int(input("Enter num: "))
for i in range(1,num+1):
    cube=i**3
    print(f"cube of {i} is {cube}")



