# def f(x, a):
#     return (x & 30 != 4) or ((x & 35 == 1) <= (x & a == 0))
#
#
# for a in range(1000, 1, -1):
#     OK = True
#     for x in range(1, 1000):
#         OK *= f(x, a)
#         if (not OK):
#             break
#     if (OK):
#         print(a)
#         break
#

def f(x, a):
    return (x & 57 != 0) and (x & 38 != 0) or (x & 9 == 0) or (x & a == 0)


for a in range(1, 1000):
    OK = True
    for x in range(-1000, 1000):
        OK *= f(x, a)
        if (not OK):
            break
    if (OK):
        print(a)
        break