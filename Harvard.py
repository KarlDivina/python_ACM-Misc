banksNumber, banksTotal = input("").split()
commands = input().split()

rep = 0
result = 0
preRsum = 0
counter = 0 

arrayV = []
arrayR = []
arrayV1 = []
arrayR1 = [] #position in overall array 

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(commands):
        if value == item_to_find:
            indices.append(idx)
    return indices

for m in commands:
    if (m.startswith("R")):
        indexR = m[1:]
        indexR = int(indexR)
        arrayR.append(indexR)

        counter -= 1
        arrayR1.append(counter)
        

    if (m.startswith("V")):
        indexV = m[1:]
        indexV = int(indexV)

        if indexV not in arrayV:
            preRsum += 1
            arrayV.append(indexV)

        arrayV1.append(indexV)

    counter += 1


allindexE = find_indices(commands, 'E')
newIndexE = []

for i in allindexE:
    newIndexE.append(i - (allindexE.index(i) + 3))

rPair = []

if len(newIndexE) > 1:
    for i in newIndexE:
        if arrayR1[-1 - newIndexE.index(i)] < newIndexE[0 + newIndexE.index(i)]:
            pair = [arrayR1[-1 - newIndexE.index(i)] +1, newIndexE[0 + newIndexE.index(i)]]
            rPair.append(pair)
            # arrayR1.remove(arrayR1[-1])
            # newIndexE.remove(newIndexE[0])
        elif(arrayR1[-1 - newIndexE.index(i)] > newIndexE[0 + newIndexE.index(i)]):
            pair = [arrayR1[-1 - newIndexE.index(i)] +1, newIndexE[-1 + newIndexE.index(i)]]
            rPair.append(pair)
            # arrayR1.remove(arrayR1[-1])
            # newIndexE.remove(newIndexE[0])
        
print(arrayV1, arrayR1, newIndexE, rPair)

####solution part        

#print(commands)

# set BSR
# if a == 0, BSR == 0
# else a == 1 is current bank, value of f is location of variable in bank a

# a=0 f=1
# bsr(1)
# a=1 f=1
# a=0 f=1
# a=0 f=1
# a=1 f=1

# repeat 10 times
# a=0 f=1
# a=0 f=1
# a=0 f=2

# a=0 f=1
