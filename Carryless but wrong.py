import math
# given an integer n, output the smallest possible carryless square root
# 17 
# 17

# identify correct square
# get correct square root

#n = int(input())
n = 123476544 

sqrtN = math.sqrt(n)

lastcharN = str(n)
lastchar = lastcharN[-1]


if (n % sqrtN == 0):
    print(sqrtN)
elif (lastchar == 2) or (lastchar == 3) or (lastchar == 7):
    print(-1)
elif (lastchar == 1):
    breakpoint
elif (lastchar == 4):
    breakpoint
elif (lastchar == 9):
    breakpoint
elif (lastchar == 6):
    breakpoint
elif (lastchar == 5):
    if lastcharN[-2] == 0:
        breakpoint
    else:
        print('-1')
elif (lastchar == 0):
    breakpoint




