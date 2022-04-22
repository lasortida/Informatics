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


a = 6 * 343 ** 1156 - 5 * 49 ** 1147 + 4 * 7 ** 1153 - 875
row = toAnother(a, 7)

summ = 0

c = int(row)
while c != 0:
    summ += c % 10
    c //= 10

print(summ)