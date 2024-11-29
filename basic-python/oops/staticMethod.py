class Emp:
    def readEmpValues(self):
        self.Ename = str(input('Enter Emp Name: '))
        self.EAge = int(input('Enter Emp Age: ')) 

class Std:
    def readStdValues(self):
        self.Sname = str(input('Enter Std Name: '))
        self.SAge = int(input('Enter Std Age: '))
        
class Teacher:
    def readTeacherValues(self):
        self.Tname = str(input('Enter Teacher Name: '))
        self.TAge = int(input('Enter Teacher Age: '))
        
class Hyd:
    @staticmethod 
    def dispValues(obj):
        for k, v in obj.__dict__.items():
            print('Key:', k, '| Value:', v)
            
# Main program 
e = Emp()
s = Std()
t = Teacher()

# Read values 
print('\nRead Emp Values')
e.readEmpValues()

print('\nRead Std Values')
s.readStdValues()

print('\nRead Teacher Values')
t.readTeacherValues() 

# Display and type of values
print('\nDisplaying Emp Values')
Hyd.dispValues(e)  # Corrected to call Hyd.dispValues() with Emp instance as argument

print('\nDisplaying Std Values')
Hyd.dispValues(s)  # Corrected to call Hyd.dispValues() with Std instance as argument

print('\nDisplaying Teacher Values')
Hyd.dispValues(t)  # Corrected to call Hyd.dispValues() with Teacher instance as argument
