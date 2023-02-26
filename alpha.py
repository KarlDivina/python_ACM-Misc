cases = int(input())
ans = []

for i in range(cases):
    case = input().split()
    stars, paradoxes = int(case[0]), int(case[1])
    lefts, rights, working, spare = [], [] ,[] ,[]
    sorted, check = [], []
    cond = 1

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

    # for i in range(paradoxes):
    #     if cond == 0:
    #         break
    #     else:
    #         u, v = lefts[i], rights[i]
    #         for j in range(paradoxes - 1):
    #             if(u == rights[j+1]) and (v == lefts[j+1]):
    #                 ans.append("IMPOSSIBLE")
    #                 cond = 0
    #                 break

    if(cond == 1):
        working = lefts + rights
        uniqueArray = set(working)
        working = uniqueArray        

        for i in range(stars):
            val = i+1
            if (val) not in working:
                spare.append(val)

# BY INDEX
        # for i in range(paradoxes):
            # leftIndex, rightIndex = working.index(lefts[i]), working.index(rights[i])
            # if working[leftIndex] not in rights and working[rightIndex] not in lefts:
            #     if leftIndex > rightIndex:
            #         working[leftIndex], working[rightIndex] = working[rightIndex], working[leftIndex]
          

            # arrLen = len(working)
            # for i in range(len(spare)):
            #     val = spare[i]
            #     for j in range(arrLen):
            #         if j != arrLen:
            #             if val > working[j]:
            #                 working.insert(j, val)
            #                 break
            #         else:
            #             working.append(val)
            #             break

            # ans.append(working)
  
# BY VALUE
        for i in range(paradoxes):
            leftValue, rightValue = lefts[i], rights[i]
            if leftValue not in sorted and rightValue not in sorted:
                sorted.append(leftValue)
                sorted.append(rightValue)
            elif leftValue in sorted and rightValue in sorted:
                check.append([leftValue, rightValue])
                leftIndex, rightIndex = sorted.index(leftValue), sorted.index(rightValue)
                if leftIndex > rightIndex:
                    sorted[leftIndex], sorted[rightIndex] = sorted[rightIndex], sorted[leftIndex]
            elif leftValue in sorted:
                sorted.insert(sorted.index(leftValue) + 1, rightValue)
            elif rightValue in sorted:
                sorted.insert(sorted.index(rightValue), leftValue)
            else:
                break
                    
        arrLen = len(sorted)
        for i in range(len(spare)):
            val = spare[i]
            for j in range(arrLen):
                if j != arrLen:
                    if val > sorted[j]:
                        sorted.insert(j, val)
                        break
                else:
                    sorted.append(val)
                    break

        if cond == 1:
            ans.append(sorted)
        else:
            continue

for i in range(len(ans)):
    if(type(ans[i]) == list):
        print(' '.join(str(val) for val in ans[i]))
    else:
        print(ans[i])