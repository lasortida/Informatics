# min = 10000
#
# for N in range(0, 1000):
#     if N % 2 == 0:
#         string = bin(N)
#         string = string[:2] + "1" + string[2:] + "0"
#         a = int(string[2:], 2)
#     else:
#         string = bin(N)
#         string = string[:2] + "11" + string[2:] + "11"
#         a = int(string[2:], 2)
#     if a > 52:
#         if a < min:
#             min = a
#
# print(min)

# print("x y z w") #xzyw
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x and z) or ((w <= x) == (z <= y))):
#                     print(x, y, z, w, sep="-")

# print("x y z w")   #xwyz
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(not((x == y) or (x == z)) or w or not(y <= z)):
#                     print(x, y, z, w, sep="-")