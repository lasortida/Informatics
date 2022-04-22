def executor(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    result = executor(start + 1, end) + executor(start * 2, end)
    if (start % 2 == 0):
        result += executor(start + 1, end)
    else:
        result += executor(start + 2, end)
    return result

print(executor(3, 9) * executor(9, 17) * executor(17, 25))