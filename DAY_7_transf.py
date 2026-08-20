"""Quiz:
1. What does the break statement do?
a) Skips the current iteration of a loop
b) Exits the loop immediately
c) Continues to the next iteration of a loop
d) Does nothing

ans: b

2. When is the continue statement used?
a) To exit a loop prematurely
b) To skip the rest of the code for the current iteration and move to the next
c) As a placeholder statement
d) To iterate through a list

ans: b

3. What is the purpose of the pass statement?
a) Exits a loop
b) Skips the current iteration of a loop
c) Acts as a null operation, doing nothing
d) Skips the rest of the code for the current iteration

ans: c
"""
# Coding Exercise:
# Problem 1: Using break in a While Loop
# Write a Python program that takes a list of numbers as input numbers = [25, 30,
# 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds
# 100, stop adding numbers and print "Sum exceeded 100".
list=[25,30,20,40,15,25]
sum=0
for i in list:
    sum=sum+i
    if sum>100:
        break
print(sum)
print(f"last iteration {i}")

# Problem 2: Using continue in a For Loop
# Write a Python script that uses a for loop to iterate through numbers from 1 to
# 600. Print only the odd numbers, skipping the even ones using the continue
# statement.
for i in range(1,601):
    if i%2==0:
        continue
    print(i)

# Problem 3: Using pass in Conditional Statements
# Write a Python script that checks if a number is even or odd. If the number is
# even, print "Even"; if odd, do nothing (use the pass statement).

num=int(input("Enetr any number: "))
if num%2==0:
    print(f"The number is even: {num}")
else:
    pass   

# Problem 4: Combining Transfer Statements
# Write a Python script that iterates through a list of words. If the word is "break,"
# exit the loop using the break statement. If the word is "skip," skip the rest of the
# code for the current iteration using the continue statement. For any other word,
# print the word.

list=["bunny","sunny","vijay","skip","binnu","lucky","break","dhanush","praneeth"]
for i in list:
    if i=="break":
        break
    elif i=="skip":
        continue
    else:
        print(i)