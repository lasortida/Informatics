def executor(start, end):
    if start > end or start == 8:
        return 0
    if start == end:
        return 1
    return executor(start + 2, end) + executor(start * 3, end)

print(executor(2, 50) * executor(50, 60))