def f(n, m):
    return n % m == 0

globalCount = 0

for A in range(1, 1001):
    OK = True
    for x in range(1, 1000):
        if not(f(A, 35) and (f(730, x) <= (not (f(A, x)) <= (not f(110, x))))):
            OK = False
            break
    if OK:
        globalCount += 1

print(globalCount)