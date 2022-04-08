file = open("14.txt")
globalCount = 0
max = -100000
previous = int(file.readline())
for element in file:
    if int(element) % 4 == 0 and previous % 4 == 0:
        globalCount += 1
        if int(element) + int(previous) > max:
            max = int(element) + int(previous)
    previous = int(element)

print(globalCount)
print(max)
