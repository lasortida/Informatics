file = open("input.txt", "r")
output = open("output.txt", "w")
stack = []
error = False
lst = file.read().split("\n")
lst.pop()
for row in lst:
    if row == "DROP":
        if len(stack) != 0:
            stack.pop()
        else:
            error = True
            break
    elif row == "SWAP":
        if len(stack) >= 2:
            first = stack.pop()
            second = stack.pop()
            stack.append(first)
            stack.append(second)
        else:
            error = True
            break
    elif row == "DUP":
        if len(stack) != 0:
            top = stack.pop()
            stack.append(top)
            stack.append(top)
        else:
            error = True
            break
    elif row == "OVER":
        if len(stack) >= 2:
            const = stack.pop()
            copy = stack.pop()
            stack.append(copy)
            stack.append(const)
            stack.append(copy)
        else:
            error = True
            break
    elif row in "+-*/":
        if len(stack) >= 2:
            second = stack.pop()
            first = stack.pop()
            if row == "+":
                result = first + second
            if row == "-":
                result = first - second
            if row == "*":
                result = first * second
            if row == "/":
                result = first // second
            stack.append(result)
        else:
            error = True
            break
    else:
        stack.append(int(row))

if error:
    output.write("ERROR")
elif len(stack) == 0:
    output.write("EMPTY")
else:
    result_stack = []
    while len(stack) != 0:
        result_stack.append(stack.pop())
    while len(result_stack) != 0:
        if len(result_stack) == 1:
            output.write(str(result_stack.pop()))
        else:
            output.write(str(result_stack.pop()) + " ")