# stringA = "Die Polizei untersucht eine Straftat im IT-Bereich."
# stringB = "untersucht eine Straftat.hciereB-TI mi  ieziloP eiD"

# identify start string
# identify end string
# reverse both

stringA = "cbaaaa"
stringB = "aaaabc"

firstIndex = 0 
nextIndex = 1

pattern = stringB[firstIndex:nextIndex]
nextIndex = stringA.find(pattern)
x = 10

while(x != 1):
    nextIndex += 1
    pattern = stringB[firstIndex:nextIndex]
    x -= 1
    if(stringA.find(pattern) == -1):
        break

nextIndex -= 1
pattern = stringB[firstIndex:nextIndex]
print("final pattern: "+pattern)

# for x in range(0, len(stringA)):
#     nextIndex += 1
#     pattern = stringB[firstIndex:nextIndex]
