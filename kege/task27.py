file = open("27-A.txt")
count = int(file.readline())
list = [int(el) for el in file]
min = 100000000000
number = 0
for i in range(count):
    delivery = 0
    for j in range(count):
        if j != i:
            delivery += list[j] * abs(j - i)
    if delivery < min:
        min = delivery
        number = i + 1
file.close()