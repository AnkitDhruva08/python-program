class Animal:
    def speak(self):
        return "Animal speaks"

class Cat(Animal):
    # Overriding the speak method
    def speak(self):
        return "Cat meows"

cat = Cat()
print(cat.speak())  # Calls the overridden speak method in Cat class
