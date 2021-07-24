#------------tick-tack-toe-----------------------------

#  game board data
board=["-","-","-",
       "-","-","-",
       "-","-","-",]

# Lets us know if the game is over yet
game_still_going=True

# Tells us who the current player is (X goes first)
current_player='X'

# Tells us who the winner is
winner=None

#--------------functions----------------------
#game play main function
def game():

    display_board()
    
    while (game_still_going) :

        handle_turn(current_player)

        check_if_game_is_over()

        flip()
    
    if winner=="X" or winner=="O" :
        print(winner+"won")

    elif winner==None :
        print ("Tie")

#to give chance to next playe
def flip() :
    
    global current_player
    current_player= "O" if current_player=="X" else "X"


# Display the game board to the screen
def display_board():
     
     print("\n\n")
     for i in range(0,3) :
         print(board[i*3]+" | "+board[i*3+1]+" | "+board[i*3+2],end="           ")
         print(str(i*3)+" | "+str(i*3+1)+" | "+str(i*3+2))
     print("\n\n")    


# Handle a turn for an arbitrary player
def handle_turn(playe) :
    
    print(current_player + "'s turn.")
    position=int(input("select your next move in above board :"))

    while (position)>8 or (position)<0 or board[position] !="-":
        print("invalid input")
        position=int(input("select your next move correctly in above board :"))
    
    # Put the game piece on the board
    board[position]=current_player

    display_board()

# Check to see if somebody has won
def check_if_game_is_over() :

    global winner
    global game_still_going
    
    #checking the rows if any winner possible
    row=check_rows()
    #checking the columns if any winner possible
    column=check_column()
    #checking the diagonal if any winner possible
    diagonal=check_diagonal()


    if row != "-" :
        winner=row 
        game_still_going=False

    elif column != "-" :
        winner=column 
        game_still_going=False 
    
    elif diagonal != "-" :
        winner=diagonal
        game_still_going=False
    else :
        if "-" not in board :
            game_still_going=False
        winner=None

#checking the rows if any winner possible
def check_rows() :

    r0=(board[0]==board[1]==board[2]!="-")
    r1=(board[3]==board[4]==board[5]!="-")
    r2=(board[6]==board[7]==board[8]!="-")

    if  r0:
         return board[0]
    elif r1:
         return board[3]
    elif r2:
         return board[6]
    return "-"

#checking the columns if any winner possible
def check_column() :
    c0=(board[0]==board[6]==board[3]!="-")
    c1=(board[1]==board[4]==board[7]!="-")
    c2=(board[2]==board[5]==board[8]!="-")
    
    if c0:
         return board[0]
    elif c1:
         return board[1]
    elif c2 :
        return board[2]
    return "-"

#checking the diagonal if any winner possible
def check_diagonal() :
     
     d1=(board[0]==board[4]==board[8]!="-")
     d2=(board[2]==board[4]==board[6]!="-")

     if d1 :
         return board[4]
     elif d2 :
         return board[4]
     return "-" 


game()