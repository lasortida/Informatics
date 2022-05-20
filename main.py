import math


def isRight(a):
    countOfDel = 0
    dels = []
    start = 2
    while start <= math.sqrt(a):
        if (a % start == 0):
            countOfDel += 2
            dels.append(start)
            dels.append(a / start)
        if (countOfDel > 2):
            break
        start += 1
    return dels

for i in range(174457, 174506):
    array = isRight(i)
    if len(array) == 2:
        print(array[0])
        print(array[1])
        print()

