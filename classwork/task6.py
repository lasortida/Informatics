row = "2" + ("8" * 99) + "2"
print(len(row))
while "81" in row or "882" in row or "8883" in row:
    if "81" in row:
        row = row.replace("81", "2", 1)
    elif "882" in row:
        row = row.replace("882", "3", 1)
    else:
        row = row.replace("8883", "1", 1)
print(row)
