# for i in range(1, 100000000000):  //3068
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#         a += 1
#         if (x % 11) > b:
#             b = x % 11
#         x //= 11
#     if a == 7 and b == 7:
#         print(i)
#         break



# for i in range(200, 100000):  //3066
#     x = i
#     print(i)
#     a = 5 * x + 345
#     b = 5 * x - 807
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     if a == 96:
#         print("The last number is answer")
#         break
