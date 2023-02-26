# input = n = number of arrangements of prime factors
# output = smallest value of k with n number of factors

primeNumbers = [2, 3, 5, 7, 11, 13, 17]

def factorial():
    factorial = 1
    if n < 0:
        print ("Factorial cannot be calculated, non-integer input")
    elif n == 0:
        print ("Factorial of the number is 1")
    else:
        for i in range (1, n+1):
            factorial = factorial *i
            print ("Factorial of the given number is: ", factorial)


inputArr = []

for i in range(0, 4):
    n = int(input())
    inputArr.append(n)

for n in inputArr:
    print(n)

# given n, which is the number of arrangements of prime factors,
# identify the smallest value of k, such that f(k) = n

