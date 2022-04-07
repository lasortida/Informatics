# 04/07

# def f(a, b):
#     return a % b == 0
#
# for A in range(1, 10000):
#     OK = True
#     for x in range(1, 10000):
#         if not((f(x, 15) and not f(x, 21)) <= (not f(x, A) or not f(x, 15))):
#             OK = False
#             break
#     if OK:
#         print(A)
#         break

# 04/08

import itertools

def k22(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return k22(start + 1, end) + k22(start + 3, end) + k22(start + 5, end)

lst = []
for i in range(3, 26):
    if i % 2 == 0:
        lst.append(i)

lst = itertools.combinations(lst, 6)
result = 0
for i in lst:
    idk = 1
    previous = 3
    for el in i:
        idk *= k22(previous, el)
        previous = el
    result += idk

print(result)


def executor(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return executor(start + 1, end) + executor(start * 3, end)

print(executor(1, 30) * executor(30, 50) * executor(50, 150))
