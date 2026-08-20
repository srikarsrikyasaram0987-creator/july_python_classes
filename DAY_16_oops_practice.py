#Class usage
class student():
    pass

obj=student()
obj1=student()

#object creation
class student():
    pass

obj=student() #object
obj1=student()

#__init__
class worker():

    def __init__(self):
        print(f"WOrking in IT company")

s=worker()

#Self
class car():

    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

s1=car("Thar Roxx","Mahendra")
print(s1.name)
print(s1.brand)

#inheritence
class Animal():

    def bark(Self):
        print("Dog is barking")

class cat(Animal):

    def eat(self):
        print("Cat is eating")
        
obj=cat()
obj.eat()
obj.bark()    