# def f(n, m):
#     return n % m == 0
#
# for A in range(1, 100000000):
#     print(A)
#     Ok = True
#     for x in range(1, 10000):
#         if not(f(A, 45) and (f(750, x) <= ((not(f(A, x))) <= (not(f(120, x)))))):
#             Ok = False
#             break
#     if Ok:
#         print(A)
#         break


# for i in range(1, 10000):
#     x = i
#     a = 0
#     b = 1
#     while x > 0:
#         if x % 2 > 0:
#             a += x % 12
#         else:
#             b *= x % 12
#         x //= 12
#     if a == 5 and b == 16:
#         print(i)
#         break

# def executor(start, end):
#     if start > end or start == 12:
#         return 0
#     if start == end:
#         return 1
#     return executor(start + 1, end) + executor(start + 2, end) + executor(start * 3, end)
#
# print(executor(2, 9) * executor(9, 19))


file = open("17.txt")
array = file.readlines()
summ_sr = 0
count_sr = 0
for i in range(len(array)):
    if int(array[i]) % 2 != 0:
        summ_sr += int(array[i])
        count_sr += 1

sr = summ_sr / count_sr

count = 0
max_sum = 0
for i in range(1, len(array)):
    first_el = int(array[i - 1])
    second_el = int(array[i])
    if (first_el % 5 == 0 or second_el % 5 == 0) and (first_el < sr or second_el < sr):
        count += 1
        if (first_el + second_el) > max_sum:
            max_sum = first_el + second_el

print(count)
print(max_sum)
file.close()
