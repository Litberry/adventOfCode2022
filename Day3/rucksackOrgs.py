def findDup(word1, word2): # Finds the duplicate character
    for ch in word1:
        if word2.find(ch) > -1:
            return ch

file1 = open("dataf.txt", "r+")

'''
Split string in half
'''
    
score = 0


for row in file1:
    comp1 = row[0 : len(row)//2]
    comp2 = row[len(row)//2 : len(row)-1]
    ch = findDup(comp1, comp2)
    if ch.isupper():
        score += ord(ch) - ord('A') + 27
    else:
        score += ord(ch) - ord('a') + 1


print(score)

file1.close()

print("done")