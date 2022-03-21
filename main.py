lst = []

with open("27B.txt") as file:
    for row in file:
       lst.append(int(row))

left = 0
right = 2
count = 0
while (left - 2 < len(lst)):
    if (right >= len(lst)):
        left += 1
        right = left + 2
        continue

    if (right - left > 1):
        if ((lst[left] + lst[right]) % 3 == 0):
            sum = 0
            for i in range(left + 1, right):
                sum += lst[i]
            if (sum % 2 == 0):
                count += 1

    right += 1

print(count)
