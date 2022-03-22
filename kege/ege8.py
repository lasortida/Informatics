import itertools

# globalCount = 0
# a = itertools.product("НИЧЬЯ", repeat=7)
# lst = list(map("".join, a))
# for row in lst:
#     if not("ИЯ" in row or "ЯИ" in row or "ИИ" in row or "ЯЯ" in row) and (row.count("И") + row.count("Я") == 2):
#         globalCount += 1
# print(globalCount)


globalCount = 0
a = itertools.product("123456789", repeat=6)
lst = list(map("".join, a))
for row in lst:
    if row[0] != "5" and row.count("2") == 2:
        globalCount += 1
print(globalCount)