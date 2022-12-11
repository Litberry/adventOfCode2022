def battle(opp, pl): # Simulates the rps game and returns result
    if (ord(opp)-65) == (ord(pl)-88): # draw
        return 3
    elif (ord(opp)-64) == (ord(pl)-88) or (opp == 'C' and pl == 'X'): # win
        return 6
    else:
        return 0

file1 = open("dataf.txt", "r+")

'''
A = Rock      = X = 1 pt
B = Paper     = Y = 2 pt
C = Scissors  = Z = 3 pt

0 pts loss, 3 pts draw, 6 pts win

Temp output = 15
'''
    
score = 0

for row in file1:
    opponent = row[0]
    player = row[2]
    score += ord(player)-87 # subtracts the ascii value by 'w'
    score += battle(opponent, player)

print(score)

file1.close()

print("done")

