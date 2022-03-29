import math

def translate(a, ns):
    string = ""
    if (a > ns - 1):
        string += translate(a // ns, ns)
    return string + str(a % ns)


def toAnother(a, ns):
    string = ""
    while a:
        string = str(a % ns) + string
        a //= ns
    return string

def toTen(a, ns):
    result = 0
    while a != "":
        result += int(a[0]) * (ns ** (len(a) - 1))
        a = a[1:]
    return result


first = 81 ** 820 - 9 ** 761 - 3 ** 2022 + 14
second = 5 * 7 ** 153 + 4 * 49 ** 85 - 3 * 7 ** 15
third = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875

print("2676: ", toAnother(first, 9).count("8"))

for i in range(1000):
    if toTen("4646", i) + toTen("387", i + 2) == toTen("3746", i + 1):
        print("2523: ", i)

count = 0
for i in toAnother(second, 7):
    if int(i) % 2 == 0:
        count += 1

print("1369: ", count)
print("1222: ", toAnother(third, 6).count("5") - toAnother(third, 6).count("0"))