gameboard = [1,2,3,4,5,6,7,8,9]
players = ('X', 'O')
counter = 0

#This function draws game board
def drawBoard(board):
    print('-------------')
    for i in range(3):
        print('|',board[0+i*3],'|',board[1+i*3],'|',board[2+i*3],'|')
    print('-----------------')
    print('Press "Q" to exit')
    print('-----------------')
    
#This function sets player to "X" or "O"
def inputPlayerLetter(counter):
    if counter%2 != 0:
        letter = players[0]       
    else:
        letter = players[1]
    
    return letter

#This function checks who is winner
def isWinner(board, letter):
    return ((board[0] == board[1] and board[1] == board[2]) or \
       (board[3] == board[4] and board[4] == board[5]) or \
       (board[6] == board[7] and board[7] == board[8])  or \
       (board[0] == board[3] and board[3] == board[6]) or \
       (board[1] == board[4] and board[4] == board[7]) or \
       (board[2] == board[5] and board[5] == board[8]) or \
       (board[0] == board[4] and board[4] == board[8]) or \
       (board[2] == board[4] and board[4] == board[6])
    )
          
#This function checks the draw
def isDraw(board):         
    if board.count("X") + board.count("O") == len(board):
        return True
    
#This function sets player move
def playerMove(board, letter):
    global counter
    while True:
        move = input('please select a number (1-9):')
        try:
            move = int(move)
        except ValueError:  
            #Exiting the game
            if move in ('Qq'):
                print('----------')
                print("Exiting...")
                print('----------')
                break     
            #player enters not a number
            else:
                print('------------------------------------------------')
                print(f'Error: you entered ({move}), which is not a number...')
                print('------------------------------------------------')
                continue
                                 
        if move not in range(1,10):
            print('-----------------------------------')
            print('Error: please select a number (1-9)')
            print('-----------------------------------')
            continue
        #spot is taken
        elif board[move-1] == 'X' or board[move-1] == 'O':
            print('-------------------------------------------------------------')
            print(f'Error: the spot ({move}) has been taken.Please select another spot' ) 
            print('-------------------------------------------------------------')
        #right move
        else:
            counter += 1
            letter = inputPlayerLetter(counter)
            board[move - 1] = letter
            drawBoard(board)
            if isWinner(board, letter):
                print('The winner is:', letter)
                break
            if isDraw(board):
                print('Draw')
                break
            
#This is main function
def playTheGame():
    drawBoard(gameboard)
    userLetter = inputPlayerLetter(counter)
    playerMove(gameboard, userLetter)
       
playTheGame()

        
        
        
        