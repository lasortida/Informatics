for A in range(1, 100000):
    OK = True
    for x in range(1, 100000):
        if ((not(x % 54 == 0) or not(x % 80 == 0)) <= (not(x % A == 0))):
            OK *= True
        else:
            OK = False
            break
    if OK:
        print(A)
        break
