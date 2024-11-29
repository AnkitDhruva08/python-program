try:
    with open('abc.text', "w") as fp:
        data = "Hello everyOne how are you"
        fp.write(data)
        print('File is cerated successfully')
except FileNotFoundError:
    print("File Not Found")
except FileExistsError:
    print('File Existance Error')
else:
    print('File is Written successfully')