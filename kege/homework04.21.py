# maximum = 0       //2354
# result = -1
#
# for i in range(101, 500):
#     row = "1" * i
#     while ("111" in row or "88888" in row):
#         if ("111" in row):
#             row = row.replace("111", "88")
#         else:
#             row = row.replace("88888", "8")
#
#     if row.count("8") > maximum:
#         maximum = row.count("8")
#         result = i
#
# print(result)


# def f(n, m):     //1128
#     return n % m == 0
#
# globalCount = 0
#
# for A in range(1, 1001):
#     OK = True
#     for x in range(1, 1000):
#         if not(f(A, 9) and (f(280, x) <= ((not(f(A, x))) <= (not(f(730, x)))))):
#             OK = False
#             break
#     if OK:
#         globalCount += 1
#
# print(globalCount)


# print("x y z w")  //1731
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((not((x == y) or (x == w))) or z or (not(y <= w))):
#                     print(x, y, z, w, sep="-")
#
# # answer is wyxz




