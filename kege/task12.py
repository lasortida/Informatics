# minimum = 500    2572
# result = 500
#
# for i in range(251, 500):
#     row = "5" * i
#     while "55555" in row:
#         row = row.replace("55555", "88", 1)
#         row = row.replace("888", "555", 1)
#     if len(row) < minimum:
#         minimum = len(row)
#         result = i
#
# print(result)

# maximum = 0  2354
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

