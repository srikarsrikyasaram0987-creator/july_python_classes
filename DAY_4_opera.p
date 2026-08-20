
"""Questions
1)What do identity operators (is and is not) check in Python?
a) Value equality
b) Memory address identity
c) Type equality
d) Sequence membership2

ans: b

2)What do membership operators (in and not in) check in Python?
a) Memory address identity
b) Type equality
c) Value equality
d) Sequence membership

 ans: d

3) Which of the following statements is correct for the identity operator is ?
a)x is y is True if the values of x and y are equal.
b) x is y is True if x and y refer to the same object.
c)x is y is True if the type of x and y is the same.
d)x is y is True if x and y are both None

ans : b

4) Which membership opclearerator is used to check if a value is not present in a sequence?
a)in
b)not in

ans: b
"""
"""Coding Exercise:1.
#Exercise:
1)Create a program that takes user input for their name and age. Use formatted strings (f-strings)
to print a message welcoming the user andstating their age."""
name=input("Enter a name :")
age=int(input("Enter your age :"))
print(f"my name is {name}\nmy age is {age}")

"""
2.Create a list called numbers that contains integers from 1 to 10.
Check if the number 5 is in the list.
Check if the number 15 is not in the list."""
list=[1,2,3,4,5,6,7,8,9,10]
print(5 in list)
print(15 not in list)

""""
Quiz Questions:
1)What is the value of result in the following code?
x = 15
y = 4
result = x // y
a) 3.75
b) 3
c) 4
d) 4.5

ans: b

2)What is the output of the following code?
a = 7
b = 3
c = a % b
print(c)
a) 2
b) 1
c) 3
d) 4

ans: b

3)Which assignment operator is equivalent to x = x * 5 ?
a) x **= 5
b) x //= 5
c) x *= 5
d) x %= 5

ans: c

4)What is the result of the expression 5 < 3 or 2 == 2 ?
a) True
b) False
c) Error
d) None of the above

ans: a

5)If a = True and b = False , what is the value of not a or b ?
a) True
b) False
c) Error
d) None of the above

ans: b

Coding Exercise:
Exercise 1:
1)Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user."""
length=int(input("Enter a length value: "))
width=int(input("Enter a width valuec:"))
area=length*width
print(area)

"""Exercise 2:
2)Write a Python program to demonstrate incrementing and decrementing a variable"""
n1=20
print(f"Before incremented: {n1}")
n1+=12
print(f"After incremented: {n1}")
n1-=12
print(f"Before decremented: {n1}")
n1-=5
print(f"After decremented: {n1}")

"""Exercise 3:
Write a Python program to convert temperature from Celsius to Fahrenheit. The
formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user."""
celsius=float(input("Enter the value: "))
f=(celsius*9/5 +32)
print(f"To convert temperature from Celsius to Fahrenheit is {f}")

"""Exercise 4:
4)Write a Python program to calculate the simple interest given the principal
amount, rate, and time (in years)."""
amount=5000
rate=15
time=3
tot=(amount*rate*time)/100
print(f"Amount is: {amount}\nRate of interest: {rate}%\nTime is given by {time} years\nTotal:{tot}")

"""Exercise 5:
5)Write a Python program to concatenate two strings and display the result. The
strings should be taken as input from the user."""
u_name=input("Enter the u_name: ")
s_name=input("Enter the s_name: ")
res=u_name+" "+s_name
print(f"concatenate two strings and display the result: {res}")

"""Exercise 6:
Write a Python program to convert a distance from kilometers to miles."""
km=float(input("Enter the km = "))
conv=0.62
miles=km*conv
print("convert a distance from kilometers to miles :",miles)









