import itertools

# globalCount = 0
# a = itertools.product("НИЧЬЯ", repeat=7)
# lst = list(map("".join, a))
# for row in lst:
#     if not("ИЯ" in row or "ЯИ" in row or "ИИ" in row or "ЯЯ" in row) and (row.count("И") + row.count("Я") == 2):
#         globalCount += 1
# print(globalCount)


# globalCount = 0
# a = itertools.product("123456789", repeat=6)
# lst = list(map("".join, a))
# for row in lst:
#     if row[0] != "5" and row.count("2") == 2:
#         globalCount += 1
# print(globalCount)

# globalCount = 0
# a = itertools.product("012345", repeat=5)
# lst = list(map("".join, a))
# for row in lst:
#     if row[0] != "0":
#         flag = True
#         for i in range(1, len(row)):
#             if row[i] in "024" and row[i - 1] in "024" or row[i] in "135" and row[i - 1] in "135":
#                 flag = False
#                 break
#         if (flag):
#             globalCount += 1
#             print(row)
# print(globalCount)

