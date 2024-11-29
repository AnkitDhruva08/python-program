import csv , sys

header = list(map(str,input("Enter Header Names : ").split(',')))

dataList = []
while (True):
    rows = list(map(str,input("Enter Fields Data : ").split(',')))
    dataList.append(rows)
    
    print('Rows Inserted into dataList')
    choice = input("Do you Want To Insert More Record Yes/No :")
    if(choice.lower() == 'no'):
        print("Thanks to insert the record")
        break
csvFileName = "csvFile.csv"

with open(csvFileName, 'w') as file:
    writeDataIntoCsv = csv.writer(file)
    # write header into csv
    writeDataIntoCsv.writerow(header)
    # write rows into csv 
    writeDataIntoCsv.writerows(dataList)
    
    print('csv file is created')
    
        
    
    