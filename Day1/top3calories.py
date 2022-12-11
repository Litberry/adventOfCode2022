file1 = open("dataf.txt", "r+")

total = 0
elves = []
  
for row in file1:
    if row == '\n':
        elves.append(total)
        total = 0
        continue
    total += int(row)

elves.append(total)
elves.sort()

print(elves[len(elves)-1] + elves[len(elves)-2] + elves[len(elves)-3])

file1.close() 

print("done")