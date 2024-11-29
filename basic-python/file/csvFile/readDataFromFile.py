import csv 

try:
    with open('csvFile.csv', 'r') as file:
            dataFile = csv.DictReader(file)
            print('dataFile ===<<<>>>', dataFile)
            for rows in dataFile:
                for k, v in rows.items():
                    print("{} ===<<>>> {}".format(k,v))
                    
                print("=====Record of data =====")
except FileExistsError:
    print('File Exist Error')
except FileNotFoundError:
    print('File Not Found')
        