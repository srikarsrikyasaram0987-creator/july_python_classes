file=open('example.txt',mode='r')
read_data=file.read()
print(read_data)
file.close()

file=open("example.txt",'r')
print(file.readline())
print(file.readline())
file.close()

file=open('example.txt',mode='r')
read_data=file.readlines()
print(read_data)
file.close()


file=open('example.txt',mode='w')
print(file.write("APPLE\n"))
print(file.write("I PHONE"))
file.close()

file=open('example.txt',mode='w+')
file.write("srikar\n")
file.write("SONY")
file.seek(0)
s=file.read()
print(s)

import os
fn="example.txt"
nn="demo.txt"
os.rename(fn,nn)

file=open('demo.txt',mode='r+')
read_data=file.read()
print(read_data)
print(file.write("\nMother is love is always precious innocence love"))
file.seek(0)
file.close()

file=open('demo.txt',mode='a+')
print(file.write("\nlove is life"))
file.seek(0)
s=file.read()
print(s)
file.close()





