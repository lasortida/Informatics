a = 16 ** 8 * 4 ** 20 - 4 ** 5 - 64

count = 0

while a != 0:
    if (a % 4 == 3):
        count += 1
    a //= 4

print(count)