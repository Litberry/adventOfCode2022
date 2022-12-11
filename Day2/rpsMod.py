def battle(opp, pl): # Simulates the rps game and returns result
    if (ord(opp)-65) == (ord(pl)-88): # draw
        return 3
    elif (ord(opp)-64) == (ord(pl)-88) or (opp == 'C' and pl == 'X'): # win
        return 6
    else:
        return 0

def determineRPS(opp, pl): # Returns the character of what you should play 
    match pl:
        case 'X':
            if opp == 'A':
                return 'Z'
            elif opp == 'B':
                return 'X'
            else:
                return 'Y'
        case 'Y':
            if opp == 'A':
                return 'X'
            elif opp == 'B':
                return 'Y'
            else:
                return 'Z'
        case 'Z':
            if opp == 'A':
                return 'Y'
            elif opp == 'B':
                return 'Z'
            else:
                return 'X'

file1 = open("dataf.txt", "r+")

'''
A = Rock      = 1 pt
B = Paper     = 2 pt
C = Scissors  = 3 pt

0 pts loss = X
3 pts draw = Y
6 pts win  = Z

Temp output = 15
'''
    
score = 0

for row in file1:
    opponent = row[0]
    player = row[2]
    choose = determineRPS(opponent, player)
    score += ord(choose)-87 # subtracts the ascii value by 'w'
    score += battle(opponent, choose)

print(score)

file1.close()

print("done")

