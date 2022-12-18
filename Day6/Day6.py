def findMarker(word): # Simulates whether there is a marker
    for ch in word:
        if word.count(ch) > 1:
            return False
    return True


file1 = open("dataf.txt", "r+")
    
word = file1.read()
print(word)

score = 0
found = False

for i in range(len(word)-14):
    subs = word[i:i+14]
    if findMarker(subs) and not found:
        found = True
        print('found it')
        print(i+14)
        print(subs)

file1.close()

print("done")