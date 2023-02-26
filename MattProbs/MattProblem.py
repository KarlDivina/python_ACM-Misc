import numpy as np

# Initializing an empty array
arr = np.array([])

# Parameters: 'item' number you want to add to the array | 'array' you want to append to
def addItem (item, array):
    # Appending item to the array
    array = np.append(array, item)
    return array

# Parameters: 'array' you want to reverse order
def reverseOrder(array):
    # Reversing the order of the array
    return array[::-1]

# Parameters: 'array' you want to see info of
def arrayInfo(array = arr):
    for x in array:
        # Current Element
        print(f"Element: {x}")
        # Length of Element
        print(f"Length: {len(str(x))}")
        # Memory Address
        print(f"Memory Address: {hex(id(x))}\n")

    # Numpy has built in feature to find memory buffer in bytes
    # See documentation:
    # https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nbytes.html
    bufferSize = array.nbytes
    print(f"Memory buffer size: {bufferSize} bytes")

# Parameters: 'index' of the array you want to remove | 'array' you want to mutate
def deleteItem(index, array):
    # Deleting an element by index
    array = np.delete(array, index)
    return array

# Parameters: 'array' you want to compare
def searchMissing(array):
    # Creates an Array of values 10 - 20 as basis
    base = np.array([10,11,12,13,14,15,16,17,18,19,20])

    # Iterates through the array
    for i in range(len(array)):
        # Iterates through the base
        for j in range(len(base)):
            # Compare array[i] for every element in base
            # and if number exist then we shall delete
            # that number from the base and break from the base j loop
            if array[i] == base[j]:
                base = np.delete(base, j)
                break

    return base


print("Program/Application 1")
arr = addItem(1, arr)
arr = addItem(2, arr)
arr = addItem(3, arr)
print(arr)

print("\n\nProgram/Application 2")
# Display reverse order
print( reverseOrder(arr) )
# Reverse order permanently
# arr = reverseOrder(arr)

print("\n\nProgram/Application 3")
print( arrayInfo(arr) )

print("\n\nProgram/Application 4")
print( deleteItem(0, arr) )

print("\n\nProgram/Application 5")
print( searchMissing( np.array( [10,12,14,16,18,20] )))