def f(a, b):
    return a % b == 0

for A in range(1, 10000):
    OK = True
    for x in range(1, 10000):
        if not((not (f(x, 54)) or not(f(x, 80))) <= (not(f(x, A)))):
            OK = False
            break
    if OK:
        print(A)
        break
