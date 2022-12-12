def encompass(p1, p2): # Returns a boolean of if one range encompasses another's
    pair1 = p1.split('-')
    pair2 = p2.split('-')
    pair2[1].strip()
    if int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1]): # Checks to see if pair1 encompasses pair2
        return True
    elif int(pair2[0]) <= int(pair1[0]) and int(pair2[1]) >= int(pair1[1]):
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