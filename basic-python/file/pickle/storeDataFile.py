import pickle 

data = {
    'name' : 'Ankit Mishra',
    'education' : 'MCA',
    'cgpa' : 8.4
}

filename = 'myDetails.txt'

with open(filename, 'wb') as file:
    pickle.dump(data, file)
    print('Data Dump Store in file')