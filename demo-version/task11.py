# task calculator
def calculate(start, end):
    if start > end:
        return 0
    if start == 24:
        return 0
    if start == end:
        return 1
    if start < end:
        return calculate(start + 1, end) + calculate(start * 3, end)

print(calculate(2, 12) * calculate(12, 72))
print(calculate(2, 12))