import csv

count = 0
summ = 0
specCount = 0

with open("task.csv", newline='') as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        if row['предмет'] == 'информатика' and int(row['балл']) > 600:
            count += 1
        if row['предмет'] == 'информатика':
            specCount += 1
            summ += int(row['балл'])
print(count)
print(summ / specCount)