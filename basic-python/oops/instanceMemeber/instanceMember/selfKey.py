# acces instance data member by using implicitly method of using self keyword

class Student: 
    def dispValues(self, name, age):
        self.name = name 
        self.age = age
        return name, age

# main program 
s1 = Student()
# access instance member by using of creat object
data = s1.dispValues('Ankit', 27)

print(data)
    
        