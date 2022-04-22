def calculate(start, end):
    if start > end or start == 30:
        return 0
    if start == end:
        return 1
    return calculate(start + 1, end) + calculate(start * 3, end) + calculate(start * 4, end)

print(calculate(2, 15) * calculate(15, 100))