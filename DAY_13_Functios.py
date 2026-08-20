# Functions Quiz:
# Question 1:
# What is the purpose of using functions in Python?
# a) To organize code into logical blocks
# b) To improve code readability and maintainability
# c) To enable code reuse
# d) All of the above

# ans: d

# Question 2:
# Which keyword is used to define a function in Python?
# a) def
# b) function
# c) define
# d) fun

#ans: a

# Question 3:
# Which of the following is a valid way to call a function named my_function with
# no arguments in Python?
# a) my_function()
# b) call my_function()
# c) function my_function()
# d) my_function

#ans: a

# Question 4:
# What is the scope of a variable defined inside a function in Python?
# a) Local scope
# b) Global scope
# c) Enclosing scope
# d) Built-in scope

# ans: a

# Functions Quiz: 2
# Task 1: Add Function
# Write a Python function named add that takes two arguments a and b and
# returns their sum.
def add(a,b):
    return(a+b)
obj=add(25,25)
print(obj)

# Task 2: Square Function
# Write a Python function named square that takes a number x as input and
# returns its square.
def square(x):
    return(x**2)
x=int(input("Enter the Number: "))
obj=square(x)
print(obj)

# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as
# input and returns its factorial.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return(fact)
n=int(input("Enter the number: "))
obj=factorial(n)
print(obj)
      
# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and
# returns the maximum value in the list.
def maximum(list):
    return max(list)
list=[1,2,35,4,5]
print(maximum(list))

# Task 5: Reverse Function
# Write a Python function named reverse that takes a string s as input and
# returns its reverse.
def reverse(s):
    return s[::-1]
print(reverse("KYASARAM SRIKAR"))           

# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input
# and returns True if n is prime, otherwise False .
def is_prime(n):
    if n%2==0:
        return False
    else:
        return True
print(is_prime(9)) 

# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as
# input and returns the n th Fibonacci number.
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
    return a
print(fibonacci(10)) 

# Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and
# returns True if s is a palindrome, otherwise False .
def palindrome(s):
    if s==s[::-1]:
        return True
    return False
print(palindrome("markram"))
print(palindrome("srikar"))

# Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that takes a list of numbers as
# input and returns the sum of the squares of those numbers.
def sum_of_square(list):
    sum=0
    for i in list:
        sum+=i**2
    return sum
print(sum_of_square([1,2,3]))

# Task 10: Average Function
# Functions Quiz: 3
# Write a Python function named average that takes a list of numbers as input and
# returns the average value.
def avg(numbers):
    return sum(numbers)/len(numbers)
print(avg([1,2,3,4,5]))