def details(sno, name, crs="python"):
    lst = [sno, name, crs]
    keys = ["sno", "name", "course"]
    # Create a dictionary by zipping keys and list values
    distList = dict(zip(keys, lst))
    return distList
        
        
print(details(10, 'Ankit'))