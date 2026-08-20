# Quiz Advanced Functions1.
# 1.What is the purpose of the map()function in Python?
# a) To filter elements from an iterable
# b) To apply a function to each element of an iterable
# c) To reduce an iterable to a single value
# d) To sort elements of an iterable2.

# ans: b

# 2.Which of the following functions is NOT a part of the functools module?
# a)map()
# b)filter()
# c)reduce()
# d)partial()

#ans: a and b

# 3.What does the filter() function do?
# a) Applies a function to each element of an iterable
# b) Reduces an iterable to a single value
# c) Filters elements from an iterable based on a condition(function returns True)
# d) Sorts elements of an iterable.

# ans: c

# 4.In Python, what is the purpose of the reduce() function?
# a) To apply a function to each element of an iterable
# b) To filter elements from an iterable
# c) To concatenate strings or join lists
# d) To apply a function to pairs of elements in an iterable until it's reduced to a single value

# ans: d

# Coding exercises:
# 1.Write a Python function square_all(numbers) that takes a list of numbers as
# input and returns a new list containing the square of each number in the input list. Use the
# map() function with a lambda function to implement this.
def square_num(n):
    return list(map(lambda x:x**2,n))
n=[1,2,3,4,5]
obj=square_num(n)
print(obj)

# 2.Write a Python function filter_positive(numbers) that takes a list of numbers as input 
# and returns a new list containing only the positive numbers from the input list. Use the
# filter() function with a lambda function to implement this.
def filter_postive(numbers):
    return list(filter(lambda x:x>0,numbers))
numbers=[1,2,3,-2,-6,4,0,10,-34]
obj=filter_postive(numbers)
print(obj)

# 3.Write a Python function calculate_factorial(n) that calculates the factorial of a given number n.Use the
# reduce()function with an appropriate lambda function to implement this.
from functools import reduce
def calculate_factorial(n):
    return(reduce(lambda x,y:x*y,range(1,n+1)))
n=5
obj=calculate_factorial(n)
print(obj)

# 4.Write a Python functioncount_vowels(string) that takes a string as input and returns the count 
# of vowels (a, e, i, o, u) in the input string. Use the reduce() function with an appropriate 
# lambda function to implement this.
from functools import reduce
def count_vowels(string):
    count=reduce(lambda a,b:a+1 if b in "AEIOUaeiou" else a,string,0)
    return count
name=input("Enter the name: ")
print("voewls are: ",count_vowels(name))
