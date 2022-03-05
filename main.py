import csv

main = []
with open("task.csv", newline='') as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        if row['предмет'] == 'информатика' and int(row['балл']) > 600:
            main.append(row)

fileIn = open("input.txt", "w")
fieldnames = ["округ", "фамилия", "предмет", "балл"]
writer = csv.DictWriter(fileIn, fieldnames=fieldnames, delimiter=";")
writer.writeheader()
writer.writerows(main)
