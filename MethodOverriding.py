class Animal:
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):  
        print("Bark")

# Example
a = Animal()
a.sound()  

d = Dog()
d.sound() 
