import collections

fileIn = open("input.txt")

deque = collections.deque()
error = False

small_deque = collections.deque()

for command in fileIn:
    if (command[0] == "+"):
        small_deque.append(command[1:])
        if (small_deque in deque):
            error = True
            break
        small_deque.clear()
        deque.append(command[1:])
    if (command[0] == "#"):
        small_deque.append(command[1:])
        if (small_deque in deque):
            error = True
            break
        small_deque.clear()
        deque.appendleft(command[1:])
    if (command[0] == "^"):
        if len(deque) == 0:
            error = True
            break
        deque.pop()
    if (command[0] == "/"):
        if len(deque) == 0:
            error = True
            break
        deque.popleft()

out = open("output.txt", "w")

if error:
    out.write("ERROR")
elif len(deque) == 0:
    out.write("EMPTY")
else:
    for i in range(len(deque)):
        out.write(deque.pop() + " ")