import pickle , sys

def saveStudentDetails():
    
    with open('stdDetails.txt', 'ab') as file:
        while(True):
            sno = int(input("Enter Student No. : "))
            Sname = input("Enter Student Details : ")
            Marks = int(input("Enter Student Marks : "))
            
            studentList = []
            studentList.append(sno)
            studentList.append(Sname)
            studentList.append(Marks)
            
            # store data into file by using dump 
            pickle.dump(studentList, file)
            print('Student Record Stored into File')
            
            choice = input("Do You Want Add More Record (Yes/ No) : ")
            
            if(choice.lower() == "no"):
                print("Thanks For Using This Program")
                sys.exit() 


# Function Call To Dump Data
saveStudentDetails()
        
        