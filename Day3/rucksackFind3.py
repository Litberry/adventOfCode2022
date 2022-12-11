def find3(w1, w2, w3): # Finds the common character common in all 3 strings
    for ch in word1:
        if w2.find(ch) > -1 and w3.find(ch) > -1:
            return ch

file1 = open("dataf.txt", "r+")

'''
Split string in half
'''
    
score = 0
count = 0

# for row in file1:
#     comp1 = row
#     bigWord += row[0:len(comp1)-1]
#     count += 1
#     if count == 3:
#         print(len(file1))
#         count = 0
        # ch = find3(comp1, bigWord)
        # if ch.isupper():
        #     score += ord(ch) - ord('A') + 27
        # else:
        #     score += ord(ch) - ord('a') + 1
        # bigWord = ''

rucksacks = file1.readlines()
count = 0
while count < len(rucksacks):
    word1 = rucksacks[count]
    word2 = rucksacks[count+1]
    word3 = rucksacks[count+2]
    count += 3
    ch = find3(word1, word2, word3)
    if ch.isupper():
        score += ord(ch) - ord('A') + 27
    else:
        score += ord(ch) - ord('a') + 1

print(score)

file1.close()

print("done")

