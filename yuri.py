inp = input()
n = int(inp)
#nString = str(n)

i = 0 #numArr length
x = 0 #forda zeroes
y = 0
z = 0
arr = []
numArrMain = []#To be checked against
numArr2 = [] #starting array
numArrChecking = []

i1 = 0
x1 = i**2
y1 = 0
z1 = 0 #starting number

#getting start number
while (x1 < n):
    i1 += 1
    x1 = i1**2
    z1 = i1 - 1

#for manually carryless squaring


# def getArray(a, numArr):
#     while a != 0:
#         a, d= divmod(a, 10)
#         numArr.append(int(d))
#         numArr.reverse()

# def getCarrylessSquare(numArr2):
#     i = len(numArr2)
#     j = i
#     z = 0
#     for q in numArr2:
#         for w in numArr2:
#             x = 10 ** j
#             y = (numArr2[q] * numArr2[w] * x) / x
#             z = z + (y * x)
#             j = j - 1
#             numArrChecking = []
#             while z != 0:
#                 z, d= divmod(z, 10)
#                 numArrChecking.append(int(d))
#                 numArrChecking.reverse()

while n != 0:
        n, d= divmod(n, 10)
        numArrMain.append(int(d))
        numArrMain.reverse()

# while numArrChecking != numArrMain
while (numArrChecking != numArrMain):
    while z1 != 0:
        z1, d= divmod(z1, 10)
        numArr2.append(int(d))
        numArr2.reverse()


    i = len(numArr2)
    j = i
    z = 0
    for q in numArr2:
        for w in numArr2:
            x = 10 ** j
            y = (q * w * x) / x
            z = z + (y * x)
            j = j - 1
            numArrChecking = []

    while z != 0:
        z, d = divmod(z, 10)
        numArrChecking.append(int(d))
        numArrChecking.reverse()

    if (numArrChecking > numArrMain):
        z1 = z1 - 1
    elif (numArrChecking < numArrMain):
        z1 = z1 + 1
    numArr2 = []
    #if z1 < n, z1-1 [loop]
    #else z1++

print(z1)

    




