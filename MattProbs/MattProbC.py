import numpy as np

#3.	Write a code that merges the following arrays and in order. Display the output.
#X=1, 4, 8, 7
#Y=2, 6, 3, 9

def arrMerge(x, y):
    arr = np.sort(np.concatenate((x, y)))
    print(arr)

x = np.array([1, 4, 8, 7])
y = np.array([2, 6, 3, 9])
arrMerge(x, y)
