import numpy as np

#2.	Write a code that creates an array containing a range of evenly spaced intervals from 0 to 20 with a step size of 5. Display the output.

def arrSpaced():
    arr = np.arange(0, 21, 5)
    print("array:", arr)

arrSpaced()