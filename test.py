# stringA = "Die Polizei untersucht eine Straftat im IT-Bereich."
# stringB = "untersucht eine Straftat.hciereB-TI mi  ieziloP eiD"

# # identify start string
# # identify end string
# # reverse both

# # accept string a 
# # accept string b
# # verify length of a and b

# # 


cases = int(input())
ans = []

for i in range(cases):
    case = input().split()
    stars, paradoxes = int(case[0]), int(case[1])
    lefts, rights, elements, spare, sortedArray = [], [] ,[] ,[], []
    cond, val = 1, 0

# check if paradoxes exist
    if paradoxes == 0:
        for i in range(stars, 0, -1):
            sortedArray.append(i)
        ans.append(sortedArray)
    else:
# sort paradox conditions
        for i in range(paradoxes):
            paradox = input().split()
            leftValue, rightValue = int(paradox[0]), int(paradox[1])
            lefts.append(leftValue)
            lefts.sort()
            occ = lefts.count(leftValue)
            firstIndex = lefts.index(leftValue)
            if occ > 1:
                for i in range(occ):
                    if i != occ-1:
                        if rightValue < rights[firstIndex + i]:
                            rights.insert(firstIndex + i, rightValue)
                            break
                    else:
                        rights.insert(firstIndex + i, rightValue)
                        break
            else:
                rights.insert(firstIndex, rightValue)

# determine unique values
        elements = lefts + rights
        uniqueArray = set(elements)
        elements = list(uniqueArray)

        for i in range(stars):
            val = i+1
            if (val) not in elements:
                spare.append(val)

# insert restricted into list
        for i in range(paradoxes):
            leftValue, rightValue = lefts[i], rights[i]
            if leftValue not in sortedArray and rightValue not in sortedArray:
                sortedArray.append(leftValue)
                sortedArray.append(rightValue)
            elif leftValue in sortedArray and rightValue in sortedArray:
                leftIndex, rightIndex = sortedArray.index(leftValue), sortedArray.index(rightValue)
                if leftIndex > rightIndex:
                    sortedArray.insert(rightIndex, leftValue)
            elif leftValue in sortedArray:
                sortedArray.insert(sortedArray.index(leftValue) + 1, rightValue)
            elif rightValue in sortedArray:
                sortedArray.insert(sortedArray.index(rightValue), leftValue)
                
# verify list is unique
        if len(elements) != len(sortedArray):
            ans.append("IMPOSSIBLE")
        else:
# insert spares into list
            for i in range(len(spare)):
                val = spare[i]
                ins = 1
                for j in range(len(sortedArray)):
                    if val > sortedArray[j]:
                        sortedArray.insert(j, val)
                        ins = 0
                        break
                if ins == 1:
                    sortedArray.append(val)
            ans.append(sortedArray)

for i in range(len(ans)):
    if(type(ans[i]) == list):
        print(' '.join(str(val) for val in ans[i]))
    else:
        print(ans[i])