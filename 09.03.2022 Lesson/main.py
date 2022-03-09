import csv

fileOut = open("answer.csv", "w")

fieldnames = ['Ученик', 'Район', 'Математика', 'Физика']
writer = csv.DictWriter(fileOut, fieldnames=fieldnames, delimiter=";")
writer.writeheader()

with open("task.csv") as file:
    reader = csv.DictReader(file, delimiter=";")
    min = 200
    count = 0
    for row in reader:
        if row['Район'] == 'Подгорный' and int(row['Математика']) + int(row['Физика']) < min:
            min = int(row['Математика']) + int(row['Физика'])
        if row['Ученик'] != '' and int(row['Математика']) == int(row['Физика']):
            count += 1
            writer.writerow(row)

print(min)
print(count)
