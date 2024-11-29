class Animal:
    def speak(self):
        return "Animal Can Speak"
    
class Dog(Animal):
    def bark(self):
        return "Dog Bark"
    
# main program 

d= Dog()

print(d.speak())
print(d.bark())