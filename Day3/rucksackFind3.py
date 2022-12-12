def find3(w1, w2, w3): # Finds the common character common in all 3 strings
    for ch in word1:
        if w2.find(ch) > -1 and w3.find(ch) > -1:
            return ch

file1 = open("dataf.txt", "r+")
    
score = 0
count = 0

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

