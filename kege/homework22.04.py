# def executor(start, end):      1038
#     if start > end or start == 8:
#         return 0
#     if start == end:
#         return 1
#     return executor(start + 2, end) + executor(start * 3, end)
#
# print(executor(2, 50) * executor(50, 60))


# for i in range(16000000, 1, -1):   3065
#     print(i)
#     x = i
#     a = 2
#     b = 3
#     while x > 0:
#         d = x % 4
#         a *= d
#         if d < 3:
#             b += d
#         x //= 4
#     if a == 24 and b == 16:
#         print(i)
#         break


# a = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875   1222
# countFive = 0
# countZero = 0
# while a != 0:
#      number = a % 6
#      if (number == 0): countZero += 1
#      if (number == 5):  countFive += 1
#      a //= 6
#
# print(countFive - countZero)
import math

# file = open("17.txt")   1993
# add_el = int(file.readline())
# summa_max = -20000
# count = 0
# for el in file:
#     summa = int(el) + add_el
#     multiply = int(el) * add_el
#     if summa % 3 == 0 and summa % 6 != 0 and abs(multiply) % 10 == 8:
#         count += 1
#         print(f"Numbers: {add_el}, {el} Sum is {summa}. Multiply is {multiply}")
#         if (summa  > summa_max):
#             summa_max = summa
#     add_el = int(el)
# print(count, summa_max)
# file.close()
