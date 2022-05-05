# count = 0
#
# for A in range(10000):
#     Ok = True
#     for x in range(100):
#         for y in range(100):
#             if not(((x < 6) <= ((x ** 2) < A)) and (((y ** 2) <= A) <= (y <= 6))):
#                 Ok = False
#                 break
#     if Ok:
#         count += 1
#
# print(count)

# def F(n):
#     summa  = 0
#     if n > 0:
#         summa += F(n - 4)
#         summa += n
#         summa += F(n // 3)
#     return summa
#
# print(F(9))

# file = open("17.txt")
#
# list = [int(element) for element in file.readlines()]
#
# count = 0
# maximum = 0
#
# for i in range(1, len(list)):
#     first = list[i - 1]
#     second = list[i]
#     summa = first + second
#     if (first % 3 == 0 or second % 3 == 0) and summa % 5 == 0:
#         count += 1
#         if summa > maximum:
#             maximum = summa
#
# print(count, maximum)

# max = 0
#
# for x in range(1000):
#     for y in range(1000):
#         if y > x:
#             z = x
#             x = y
#             y = z
#         a = x
#         b = y
#         while b > 0:
#             r = a % b
#             a = b
#             b = r
#         if a == 7 and x == 42:
#             if y > max:
#                 max = y
#
# print(max)
