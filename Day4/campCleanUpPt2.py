def encompass(p1, p2): # Returns a boolean of if one range encompasses another's or at least part of another's
    pair1 = p1.split('-')
    pair2 = p2.split('-')
    pair2[1].strip()
    pi1 = int(pair1[0]) # Declaring variables for each part of the pair as ints
    pi2 = int(pair1[1])
    pi3 = int(pair2[0])
    pi4 = int(pair2[1])
    if pi1 <= pi4 and pi2 >= pi3: 
        return True
    else:
        return False

file1 = open("dataf.txt", "r+")
    
score = 0

for row in file1:
    pairs = row.split(",")
    score += encompass(pairs[0], pairs[1]) 

print(score)

file1.close()

print("done")