'''
 Programmed by : Mugdha Wadikar
 Date: 1st july 2019
 Play a tic-tac-toe game with the computer
 A round is completed with Player selecting a position and the opponent/computer playing a move.
 There are 5 rounds with the last round played only by the player
'''


# The game matrix is the playground for the tic-tac-toe game
gameMatrix=[['','',''],['','',''],['','','']]

# track moves: row0, row1, row2, col0, column1, column2, diagonal0, diagonal1
# track moves tracks rows, columns and diagonals for each player and opponent 
playerMatrix=[0,0,0,0,0,0,0,0]
opponentMatrix=[0,0,0,0,0,0,0,0]
# blank checks remaining empty spaces in the game matrix
blank = 9

# print the current game matrix with X and O
def printGameMatrix():
    print(gameMatrix[0][0],' | ',gameMatrix[0][1],' | ',gameMatrix[0][2])
    print('-----------')
    print(gameMatrix[1][0],' | ',gameMatrix[1][1],' | ',gameMatrix[1][2])
    print('-----------')
    print(gameMatrix[2][0],' | ',gameMatrix[2][1],' | ',gameMatrix[2][2])
    
# Grid to ease user options for selecting position
def userOptions():
    print('LL | LM | LH')
    print('---+----+---')
    print('ML | MM | MH')
    print('---+----+---')
    print('HL | HM | HH')
    
# Whenever a player makes a move, two steps are followed:
# Check if player/opponent had already marked the position. If yes, player is asked to chose another position.
# If player move is valid, the game matrix and player matrix is updated.
    
def checkPlayerMatrix(playerMove)->bool:
    if playerMove=='LL' and gameMatrix[0][0]=='':
        compute(playerMatrix,'X',0,0)
        return True
    elif playerMove=='LM' and gameMatrix[0][1]=='':
        compute(playerMatrix,'X',0,1)
        return True
    elif playerMove=='LH' and gameMatrix[0][2]=='':
        compute(playerMatrix,'X',0,2)
        return True
    elif playerMove=='ML' and gameMatrix[1][0]=='':
        compute(playerMatrix,'X',1,0)
        return True
    elif playerMove=='MM' and gameMatrix[1][1]=='':
        compute(playerMatrix,'X',1,1)
        return True
    elif playerMove=='MH' and gameMatrix[1][2]=='':
        compute(playerMatrix,'X',1,2)
        return True
    elif playerMove=='HL' and gameMatrix[2][0]=='':
        compute(playerMatrix,'X',2,0)
        return True
    elif playerMove=='HM' and gameMatrix[2][1]=='':
        compute(playerMatrix,'X',2,1)
        return True
    elif playerMove=='HH' and gameMatrix[2][2]=='':
        compute(playerMatrix,'X',2,2)
        return True
    else:
        print('Select another move. This one was used before')
        return False
    

# player/opponent matrix based on respective moves. The game matrix, player matrix and opponent matrix is updated row wise, column wise or diagonally.
def compute(matrix,symbol,i,j):
    if i==0 and j==0:
        gameMatrix[0][0]=symbol
        matrix[0]+=1
        matrix[3]+=1
        matrix[6]+=1
    elif i==0 and j==1:
        gameMatrix[0][1]=symbol
        matrix[0]+=1
        matrix[4]+=1
    elif i==0 and j==2:
        gameMatrix[0][2] =symbol
        matrix[0]+=1
        matrix[5]+=1
        matrix[7]+=1
    elif i==1 and j==0:
        gameMatrix[1][0]=symbol
        matrix[1]+=1
        matrix[3]+=1
    elif i==1 and j==1:
        gameMatrix[1][1]=symbol
        matrix[1]+=1
        matrix[4]+=1
        matrix[6]+=1
        matrix[7]+=1
    elif i==1 and j==2:
        gameMatrix[1][2] =symbol
        matrix[1]+=1
        matrix[5]+=1
    elif i==2 and j==0:
        gameMatrix[2][0]=symbol                              
        matrix[2]+=1
        matrix[3]+=1
        matrix[7]+=1
    elif i==2 and j==1:
        gameMatrix[2][1]=symbol                        
        matrix[2]+=1
        matrix[4]+=1
    elif i==2 and j==2:
        gameMatrix[2][2] =symbol
        matrix[2]+=1
        matrix[5]+=1
        matrix[6]+=1
    
    
# calls compute function to update the game matrix and opponent matrix based on opponent movies
def computeOpponentMatrix(i):
    if i==0:
        j = gameMatrix[0].index('')
        compute(opponentMatrix,'O',0,j)
        
    elif i==1:
        j = gameMatrix[1].index('')
        compute(opponentMatrix,'O',1,j)
        
    elif i==2:
        j = gameMatrix[2].index('')
        compute(opponentMatrix,'O',2,j)
        
    elif i==3:
        j = [gameMatrix[0][0],gameMatrix[1][0],gameMatrix[2][0]].index('')
        compute(opponentMatrix,'O',j,0)
        
    elif i==4:
        j = [gameMatrix[0][1],gameMatrix[1][1],gameMatrix[2][1]].index('')
        compute(opponentMatrix,'O',j,1)
        
    elif i==5:
        j = [gameMatrix[0][2],gameMatrix[1][2],gameMatrix[2][2]].index('')
        compute(opponentMatrix,'O',j,2)
        
    elif i==6:
        j = [gameMatrix[0][0],gameMatrix[1][1],gameMatrix[2][2]].index('')
        compute(opponentMatrix,'O',j,j)
        
    else:
        j = [gameMatrix[0][2],gameMatrix[1][1],gameMatrix[2][0]].index('')
        compute(opponentMatrix,'O',j,abs(2-j))
                
# actual function where computeOpponentMatrix() function is called
# case 1: if 3 'X' in a row/col/diagonal: Player wins
# case 2: if 2 'X' in a row/col/diagonal and a blank present, opponent puts 'O' in blank space.
def checkOpponentMatrix():
    maxPlayer = max(playerMatrix)
    notFound = True
    maxComputer = max(opponentMatrix)
    if maxPlayer==3:
        print('\n---You Win---\n')
        exit()
    while notFound:
        for i in range(8):
            if opponentMatrix[i]==2 and playerMatrix[i]==0:
                computeOpponentMatrix(i)
                notFound=False
                break
        if notFound==False:
            break
        for i in range(8):
            if opponentMatrix[i]==0 and playerMatrix[i]==2:
                computeOpponentMatrix(i)
                notFound=False
                break
        if notFound==False:
            break
        for i in range(8):
            if opponentMatrix[i]==0 and playerMatrix[i]==1:
                computeOpponentMatrix(i)
                notFound=False
                break
        
                            
# take user input and show ganme matrix after each round 
userOptions()   
while blank:
    #userOptions()
    while True:
        playerMove = input()
        mv = checkPlayerMatrix(playerMove)
        if mv:
            blank-=1
            break
    
    if blank==8 and gameMatrix[1][1]=='':
        compute(opponentMatrix,'O',1,1)
    elif blank==8 and gameMatrix[1][1]!='':
        compute(opponentMatrix,'O',0,0)
    else:
        if blank==0:
            printGameMatrix()
            print('\n---game draw---\n')
            exit()
        checkOpponentMatrix()
                
    print('\n---After this round---\n')
    printGameMatrix()
    print('\n\n\n')
    if max(opponentMatrix)==3:
        print('\n---You lose---\n')
        exit()
    blank-=1
