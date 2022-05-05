fileInput = open("input.txt")
output = open("output.txt", "w")
ver, gor = map(int, fileInput.readline().split())
x, y = map(int, fileInput.readline().split())
NEW_COLOR = int(fileInput.readline())
matrix = [[int(i) for i in fileInput.readline().split()] for _ in range(ver)]

queue = []
color = matrix[y][x]
queue.append((y, x))

while len(queue) > 0:
    y, x = queue.pop(0)
    if matrix[y][x] == color:
        matrix[y][x] = NEW_COLOR
        if x > 0: queue.append((y, x - 1))
        if x < gor - 1: queue.append((y, x + 1))
        if y > 0: queue.append((y - 1, x))
        if y < ver - 1: queue.append((y + 1, x))

for i in range(ver):
    for j in range(gor):
        print(matrix[i][j], end="\t")
    print()