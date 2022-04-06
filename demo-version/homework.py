def f(a, b):
    return a % b == 0

for A in range(1, 10000):
    OK = True
    for x in range(1, 10000):
        if not((f(x, 15) and not f(x, 21)) <= (not f(x, A) or not f(x, 15))):
            OK = False
            break
    if OK:
        print(A)
        break