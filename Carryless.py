inp = input()
n = int(inp)
nString = str(n)

i = 0
x = 0
y = 0
z = 0
arr = []
numArr = []
numArr2 = []

# put int in array indiv through divmod
# get array length
# make integer = 10^arr len
# multiply arr[i] arr[j] x integer 
# make int += product of ^

while (x < n): #getting number with closest square 
    i += 1
    x = i**2
    y = i
    z = i - 1

while y != 0: #divmod, array
    y, d= divmod(y, 10)
    numArr.append(int(d))
    numArr.reverse()

while z != 0:
    z, d= divmod(z, 10)
    numArr2.append(int(d))
    numArr2.reverse()


#12 
#num arr = 1,2 
someString = ""
print(y)
print(z)

def doMathYes(integ):
    someString = ""
    for math in numArr:
        for yes in numArr:
            do = (math * yes) % 10
            someString += str(do)
    return(someString)

someString = doMathYes(y)

print("y: ", someString)

if (someString == nString):
    print(y)

someString = doMathYes(z)

if (someString == nString):
    print(z)

print("z: ", someString)

