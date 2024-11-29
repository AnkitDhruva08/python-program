myFile = open("abc1.text", 'w')
print("myFile type of file", type(myFile))


data = str({"name" : 'ankit', "age": 27})
myFile.write(data)
print('File created succesfully')