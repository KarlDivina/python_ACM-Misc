testcase = int(input())
systems = list()
stars = list()

for i in range(testcase):    
    systems.append(input())
    stars.append(list(map(int, input().split("(?!^)"))))

for array in stars:
    x = 1
    ctr = 0
    for i in array:
        print(i)
        if(i != x):
            ctr += 1
            x = i
    print(ctr)