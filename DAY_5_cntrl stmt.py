"""1. Indentation is crucial in Python to:r

A. Improve code readability
B. Indicate the end of the program
C. Separate code blocks
D. Define the scope of a code block

ans: D

2. What will be the output of the following code? python
x = 10
if x > 5:
print("Greater than 5")
else:
print("5 or less")

A. Greater than 5
B. 5 or less
C. Both A and B
D. None of the above

ans: A

3. In the if-elif-else statement, how many conditions can be checked?
A. Only one
B. Two
C. Multiple
D. None

ans: C

4. What is the purpose of the else statement in Python?
A. To handle errors
B. To provide an alternative block of code when the if condition is false
C. To terminate the program
D. To declare variables

ans: B

5. Which of the following statements is true about a nested if statement?
A. It is not allowed in Python
B. It allows for more complex conditional logic
C. It always leads to syntax errors
D. It can only contain one level of nesting

ans: B
"""
"""Exercises:
1. Vowel Checker:
Write a Python program that takes a character as input and checks whether
it is a vowel or not. Use the if-else statement."""

chr = input("Enter the charcter :")
if chr in "aeiouAEIOU":
    print("it is a vowel")
else:
    print("it is not vowel")

"""2. Age Group Classification
Write a program that takes an age as input and classifies the person into
one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older"""

age=int(input("Enetr the Age :")) 
if age>=0 and age<=12:
    print("you are a child")
elif age>=13 and age<=17:
    print("you are teenager")
elif age>=18 and age<=64:
    print("you are adult")
else:
    print("you are older")    

"""3. Number Classifier:
Write a program that takes an integer as input and classifies it as positive,
negative, or zero. Use the if-elif-else statement."""

num=int(input("Enter the Number: "))
if num>0:
    print(f"it is a positive number: {num}")
elif num<0:
    print(f"it is a negative number: {num}")  
else:
    print("it is zero ")  

"""4.Leap Year Checker:
Create a program that checks whether a given year is a leap year or not. A
leap year is divisible by 4, but not by 100 unless it is divisible by 400."""

yr=int(input("Enter the year: "))
if(yr%4==0 and yr%100!=0) or (yr%400==0):
    print(f"{yr} it is leap year")
else:
    print(f"{yr} it is not leap year")    

"""5.Build a simple calculator program that takes two numbers and an operator
(+, -, *, /) as input and performs the corresponding operation."""

n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2:"))
opr=(input("Enter the operator(+,-,*,/):"))
if opr=="+":
    print("ADDITION:",n1+n2)
elif opr=="-":
    print("SUBTRACTION:",n1-n2)
elif opr=="-":
    print("MULTIPLICATION:",n1-n2)
else:
    print("DIVISION:",n1/n2)


"""6. Short Hand If:
Rewrite the following code using the short-hand
if statement:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"
"""
x=3
res="Even" if x%2==0 else "odd"
print(f"{x}:The number is {res}")

"""7.Discount Calculator:
Create a program that calculates the final price after applying a discount.
The program should take the original price and the discount percentage as
input."""

org_price=float(input("Enter the Original price: "))
dis_perc=float(input("Enter the discount percentage: "))
discount=org_price*dis_perc/100
final_price=org_price -discount
print(f"Discount you got: {discount}\n The final price is:{final_price}")

"""BMI Calculator:
Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input."""

weight=int(input("Enter the weight: "))
height=int(input("Enter the height: "))
BMI = (weight/(height**2))
print(f"BMI is: {BMI}")
