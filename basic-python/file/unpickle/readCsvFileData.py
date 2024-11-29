import pickle 

try:
    with open("stdDetails.csv", 'rb') as file:
        while (True):
            try:
                loadFile = pickle.load(file)
                print('loadFile data ===<<<>>>', loadFile)
                for val in loadFile:
                    print('Val ===<<<>>>>', val)
            except EOFError:
                break
            
except FileNotFoundError:
    print('File Not Found')
except FileExistsError:
    print('File Exists Error')