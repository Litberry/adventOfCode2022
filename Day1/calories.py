file1 = open("dataf.txt", "r+")

total = 0
highest = -1
  
for row in file1:
    if row == '\n':
        total = 0
        continue
    total += int(row)
    highest = max(highest, total)

highest = max(highest, total)

print(highest)

file1.close() 

print("done")