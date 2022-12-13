def simulate(q, i, f): # Simulates a crane moving boxes
    rIndex = len(stashes[i])-q
    for t in range(q):
        stashes[f].append(stashes[i][rIndex])
        del stashes[i][rIndex]


file1 = open("dataf.txt", "r+")
    
rows = file1.readlines()

score = 0
count = 0
data = [] # List of rows in the data representing positions
stashes = [] # Creates a list of lists to represent stashes

while True:
    row = rows[count]
    if row == '\n':
        break
    data.append(row) # Start splitting up the list
    count += 1

NUM_OF_STASHES = int(data[count-1].split().pop()) # Finds the number of stashes using the last row of the list

for i in range(NUM_OF_STASHES): # Populates stashes with empty lists
    stashes.append([])

for q in range(NUM_OF_STASHES): # Populates stash lists
    row = data[q]
    for i in range(NUM_OF_STASHES):
        element = row[(i*4+1):(i*4+2)]
        if element != ' ':
            stashes[i].append(element)

for i in range(NUM_OF_STASHES): # Reverses each list to create a stack data structure
    stashes[i].reverse()

# Processes the commands
mQuantities = [] # number of boxes moved 
iLocation = []
fLocation = []

while count < len(rows)-1:
    count += 1
    row = rows[count]
    commands = row.split()
    mQuantities.append(int(commands[1]))
    iLocation.append(int(commands[3])-1)
    fLocation.append(int(commands[5])-1)

for i in range(len(mQuantities)):
    simulate(mQuantities[i], iLocation[i], fLocation[i])

for item in stashes:
    print(item.pop())

file1.close()

print("done")