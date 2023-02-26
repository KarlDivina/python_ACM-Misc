games = []
gamesToBurn = []
total, length = input("Enter total number of games and length of each name: ").split()
total, length = [int(total), int(length)]
alphabet = input("Enter characters: ")
numberCD = int(input("Enter total number of possible games on CD: "))

for x in range(0, numberCD):
    game = input()
    games.append(game)

gamesOnCD = games.copy()
gamesOnCD.sort()
counter = 0

for x in gamesOnCD:
    if x in alphabet:
        firstIndex = alphabet.find(x)
        game = alphabet[firstIndex: length+1]
        alphabet = alphabet[:firstIndex] + alphabet[length+firstIndex:]
        gamesToBurn.append(games.index(x) + 1)
        if alphabet == "":
            print("YES")
            for x in gamesToBurn:
                print(x, end=" ")
            break
        elif alphabet != "":
            counter += 1
            continue
    else:
        print("NO")
        break

# 4 2
# aabbccdd
# 4
# dd
# ab
# bc
# cd

# 3 1
# abc
# 4
# b
# a
# c
# d