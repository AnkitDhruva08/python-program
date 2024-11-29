def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # Normalize the number of rotations

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse the first d elements
    reverse(0, d - 1)

    # Step 2: Reverse the remaining n-d elements
    reverse(d, n - 1)

    # Step 3: Reverse the entire array
    reverse(0, n - 1)

    return arr


# function call 

arr = list(map(int, input('Enter List Of Values : ').split(',')))
d = int(input("Enter Number of Rotation : "))

print(rotate_array(arr, d))