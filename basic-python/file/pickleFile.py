import pickle

# Example Python object to pickle (a dictionary in this case)
data = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'skills': ['Python', 'Machine Learning', 'Data Science']
}

# File to save the pickled object
filename = 'details.text'

### Pickling ###
with open(filename, 'wb') as file:  # 'wb' mode for writing in binary
    pickle.dump(data, file)
    print("Data pickled and saved to file:", filename)

### Unpickling ###
with open(filename, 'rb') as file:  # 'rb' mode for reading in binary
    loaded_data = pickle.load(file)
    print("Data unpickled and loaded from file:")
    print(loaded_data)
