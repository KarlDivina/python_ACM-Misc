cases = int(input())
ans, facts = [], []

for i in range(cases):
    inputs = input().split()
    locks, symbols = int(inputs[0]), int(inputs[1])
    ctr, fact = 0, 1

    for i in range(2, locks+1, 1):
        fact *= i
        cond = 1
        print("OUTSIDE WHILE", fact)
        while(fact % symbols == 0):
            ctr += 1
            fact /= symbols
            print("INSIDE WHILE", fact)
            cond = 0
    print("Counter: ", ctr)