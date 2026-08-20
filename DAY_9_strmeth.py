# Quiz Questions:
# Question 1:
# What is the main characteristic of Python strings?
# a) Mutable
# b) Immutable
# c) Dynamic
# d) Static

# ans: b

# Question 2:
# How can you access the last character of a string in Python?
# a) my_string[-1]
# b) my_string[last]
# c) my_string[last_char]
# d) my_string(end)

# ans: a

# Question 3:
# Which method is used to convert a string to uppercase in Python?
# a) to_upper()
# b) uppercase()
# c) .upper()
# d) case_upper()

# ans: c

# Question 4:
# What does the split() method do?
# a) Combines strings
# b) Splits a string into a list of substrings
# c) Finds a substring in a string
# d) Converts a string to lowercase

# ans: b

# Question 5:
# Which method is used to check if a string starts with a specific prefix?
# a) startswith()
# b) startwith()
# c) beginwith()
# d) initwith()

# ans: a

# Coding Exercise :
# Problem:
# You are given a string sentence . Print the characters at even indices.
# Example:
# sentence = "Python is amazing"
# Output: "Pto saaig"

sentence="Python is amazing"
res=""
for i in range(0,len(sentence),2):
    res=res+sentence[i]
print(res)

# Problem:
# You are given a string s . Replace all spaces in the string with underscores ( _ )
# and print the modified string.
# Example:
# s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"

s="Python is fun and powerful"
new=s.replace(" ","_")
print(new)

# Problem:
# You are given a string s . Check if the string contains only digits.
# Example:
# s = "12345"

s = "12345"
res=s.isdigit()
print(res)

# Problem:
# You are given a string s . Print the string in reverse order.
# Example:
# Quiz Questions: 3
# s = "Python is amazing"
# Output: "gnizama si nohtyP

s = "Python is amazing"
s1=s[::-1]
print(s1)
print(s)

# Problem:
# You are given a string s . Capitalize the first letter of each word in the string
# and print the modified string.
# Example:
# s = "python programming is fun"
# Output: "Python Programming Is Fun"
s = "python programming is fun"
s1=s.title()
print(s1)




