def find3(word1, bigString): # Finds the common character common in all 3 strings
    for ch in word1:
        if bigString.count(ch) == 3:
            return ch

file1 = open("dataf.txt", "r+")

'''
Split string in half
'''
    
score = 0
bigWord = ''
count = 0

for row in file1:
    comp1 = row
    bigWord += row[0:len(comp1)-1]
    count += 1
    if count == 3:
        ch = find3(comp1, bigWord)
        if ch.isupper():
            score += ord(ch) - ord('A') + 27
        else:
            score += ord(ch) - ord('a') + 1


print(score)

file1.close()

print("done")

