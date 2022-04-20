# def f(n, m):     760
#     return n % m == 0
#
# for A in range(1, 1001):
#     OK = True
#     for x in range(1, 1000):
#         if not((f(x, A) and f(x, 16)) <= (not(f(x, 16)) or f(x, 24))):
#             OK = False
#             break
#     if OK:
#         print(A)
#         break

# def f(n, m):   1128
#     return n % m == 0
#
# globalCount = 0
#
# for A in range(1, 1001):
#     OK = True
#     for x in range(1, 1000):
#         if not(f(A, 9) and (f(280, x) <= (not(f(A, x)) <= (not(f(730, x)))))):
#             OK = False
#             break
#     if OK:
#         globalCount += 1
#
# print(globalCount)
