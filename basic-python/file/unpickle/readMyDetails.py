import pickle 

try:
    filename = 'myDetails.txt'
    
    with open(filename, 'rb') as file:
        data = pickle.load(file) 
        print('data ===<<<>>>>', data)
except FileNotFoundError:
    print('File not found')
except FileExistsError:
    print('File Exist Error')