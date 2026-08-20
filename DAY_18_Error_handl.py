#ValueError
try:
    num_1=int(input("Enter the number: "))
    num_2=int(input("Enter the number: "))
    obj=num_1+num_2
    print(obj)
except ValueError as e:
    print(e)  

#TypeError
try:
    roll_no= 25
    marks="TEN"
    obj= roll_no+marks
    print(obj)
except TypeError as e:
    print(e)
finally:
    print("Last line of code")

#FileNotFoundError
try:
    file=open("demo2.txt",mode='r')
    obj=file.read()
    print(obj)
except FileNotFoundError as e:
    print("FileNotFoundError",e)         

#ZeroDivisionError
try:
    n1=25
    n2=0
    print(n1/n2)
except ZeroDivisionError as e:
    print("ZeroDivisionError",e)

#AttributeError
try:    
    name="srikar"
    obj=name.append("Student")
    print(obj)
except AttributeError as e:
    print(e)      

#IndexError
list=[1,2,3,4,5]
print(list[1])
try:
    print(list[6])
except IndexError as e:
    print(e)

#SyntaxError
# try:
    print("Srikar is a name")
except SyntaxError as e:
    print(e)    

#I/OError
file=open("demo2.txt",mode='r')
obj=file.read()
print(obj)   

#OverflowError
try:
    import math
    print(math.exp(1000))
except OverflowError as e:
    print(e)    

#RuntimeError
try:
    num_1=int(input("Enter the number: "))
    num_2=int(input("Enter the number: "))
    obj=num_1+num_2
    print(obj)
except RuntimeError as e:
    print("RuntimeError",e) 




























