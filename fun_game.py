# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Robert Schaab
#               Nate Barrera
#               Joe Badawy
# Section:      ENGR-102-535
# Assignment:   fun_game.py
# Date:         16/11/2022

#the goal of this program is to play a game of connect four
import turtle as tu

board = [['_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_']]
redPiece = 'R'
orangePiece = 'Y'


######## FUNCTIONS ########
# drawBoard
def drawBoard(turtle, screen):
    '''This function draws the layout of the connect 4 board'''

    screen.setup(width=550, height=500, startx=200, starty=150)
    screen.title("CONNECT 4")
    turtle.screen.bgpic("connectBoard.png")
    turtle.screen.screensize(490, 490)

    turtle.setposition(-206, -230)
    turtle.pendown()
    turtle.write('1', True, align='right', font=('Arial', 15, 'normal'))
    turtle.penup()

    turtle.setposition(-136, -230)
    turtle.pendown()
    turtle.write('2', True, align='right', font=('Arial', 15, 'normal'))
    turtle.penup()

    turtle.setposition(-66, -230)
    turtle.pendown()
    turtle.write('3', True, align='right', font=('Arial', 15, 'normal'))
    turtle.penup()

    turtle.setposition(6, -230)
    turtle.pendown()
    turtle.write('4', True, align='right', font=('Arial', 15, 'normal'))
    turtle.penup()

    turtle.setposition(76, -230)
    turtle.pendown()
    turtle.write('5', True, align='right', font=('Arial', 15, 'normal'))
    turtle.penup()

    turtle.setposition(146, -230)
    turtle.pendown()
    turtle.write('6', True, align='right', font=('Arial', 15, 'normal'))
    turtle.penup()

    turtle.setposition(216, -230)
    turtle.pendown()
    turtle.write('7', True, align='right', font=('Arial', 15, 'normal'))
    turtle.penup()

def welcomeScreen():
    '''Displays the rules of the game'''

    print(f"Howdy! You have started playing a game Connect Four! Here are the rules:\n"
                 "1. Players take alternating turns placing pieces on a 6x7 board.\n"
                 "2. Each player will try to get their color piece to be four-in-a-row "
                        "horizontally, vertically, or diagonally.\n"
                 "3. If the board becomes full and no winner is declared, the game will end in a draw.\n")
    print(f'Here are your options as Player 1 or Player 2:\n'
            "Player one will have red pieces, and Player Two will have orange pieces.\n"
            "First, enter a column in the box to place a piece of your color into.\n"
            "The column you select will add your color piece to the stack of pieces (if one exists) in that column.\n"
            "The current state of the board will display after each turn so you can strategize you next move.\n")
    choice = input(f'Hit any key to start the game: ')


# player1
def playerOne(turtle, screen, turn):
    '''This creates the moves for player One'''

    move = screen.numinput(f"Player 1: turn: {turn + 1}", "Your Move(1 - 8)(8 quits):", 0, minval=1, maxval=8)
    row, move = isValid(move, 1, screen, redPiece)
    drawPiece(row, move, redPiece, turtle)

    # Display the board in console
    print('\n' * 8)
    for i in range(len(board)):
        print('| ', end='')
        for j in range(len(board)+1):
            print(board[i][j], end=' | ')
        print()

    # Check if 4 pieces are connected
    winCond = winCondition()
    return move, winCond


# player2
def playerTwo(turtle, screen, turn):
    '''This creates the moves for player Two'''

    move = screen.numinput(f"Player 2: turn: {turn + 1}", "Your Move(1 - 8)(8 quits):", 0, minval=1, maxval=8)
    row, move = isValid(move, 2, screen, orangePiece)
    drawPiece(row, move, orangePiece, turtle)

    # Display the board in console
    print('\n' * 8)
    for i in range(len(board)):
        print('| ', end='')
        for j in range(len(board)+1):
            print(board[i][j], end=' | ')
        print()

    # Check if 4 pieces are connected
    winCond = winCondition()
    return move, winCond

# isValid
def isValid(move, player, screen, piece):
    '''is valid determines if a spot on the board is already taken. If the spot is taken the board will move up'''

    row = 0
    move = int(move)
    while True:
        try:
            # If a player hits 8, the player surrenders
            if move == 8:
                break
            else:
                move = move - 1

            # Move the piece to bottom of the column where a spot isn't taken
            if board[5][move] == redPiece or board[5][move] == orangePiece:
                if board[4][move] == redPiece or board[4][move] == orangePiece:
                    if board[3][move] == redPiece or board[3][move] == orangePiece:
                        if board[2][move] == redPiece or board[2][move] == orangePiece:
                            if board[1][move] == redPiece or board[1][move] == orangePiece:
                                if board[0][move] == redPiece or board[0][move] == orangePiece:
                                    move = screen.numinput(f"Player {player}",
                                                           "Column Taken. Move again: (1 - 7):",
                                                           0, minval=1, maxval=7)
                                    move = int(move)

                                else:
                                    board[0][move] = piece
                                    row = 0
                                    break

                            else:
                                board[1][move] = piece
                                row = 1
                                break
                        else:
                            board[2][move] = piece
                            row = 2
                            break
                    else:
                        board[3][move] = piece
                        row = 3
                        break
                else:
                    board[4][move] = piece
                    row = 4
                    break
            else:
                board[5][move] = piece
                row = 5
                break
        except:
            move = screen.numinput(f"Player {player}", "Invalid move. Move again: (1 - 7):",
                                   0, minval=1, maxval=7)
            move = int(move)

    return row, move


# drawPiece
def drawPiece(row, move, piece, turtle):
    '''moves the turtle to the spot to draw a circle'''

    if move == 0:
        if row == 0:
            turtle.setpos(-209.5, 173)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 1:
            turtle.setpos(-209.5, 103)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 2:
            turtle.setpos(-209.5, 33)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 3:
            turtle.setpos(-209.5, -37)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')


        elif row == 4:
            turtle.setpos(-209.5, -107)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 5:
            turtle.setpos(-209.5, -177)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')


    elif move == 1:
        if row == 0:
            turtle.setpos(-139.5, 173)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 1:
            turtle.setpos(-139.5, 103)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 2:
            turtle.setpos(-139.5, 33)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 3:
            turtle.setpos(-139.5, -37)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 4:
            turtle.setpos(-139.5, -107)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 5:
            turtle.setpos(-139.5, -177)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

    elif move == 2:
        if row == 0:
            turtle.setpos(-69.5, 173)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 1:
            turtle.setpos(-69.5, 103)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 2:
            turtle.setpos(-69.5, 33)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 3:
            turtle.setpos(-69.5, -37)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 4:
            turtle.setpos(-69.5, -107)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 5:
            turtle.setpos(-69.5, -177)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

    elif move == 3:
        if row == 0:
            turtle.setpos(.5, 173)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 1:
            turtle.setpos(.5, 103)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 2:
            turtle.setpos(.5, 33)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 3:
            turtle.setpos(.5, -37)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 4:
            turtle.setpos(.5, -107)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 5:
            turtle.setpos(.5, -177)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

    elif move == 4:
        if row == 0:
            turtle.setpos(70.5, 173)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 1:
            turtle.setpos(70.5, 103)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 2:
            turtle.setpos(70.5, 33)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 3:
            turtle.setpos(70.5, -37)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 4:
            turtle.setpos(70.5, -107)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 5:
            turtle.setpos(70.5, -177)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

    elif move == 5:
        if row == 0:
            turtle.setpos(140.5, 173)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 1:
            turtle.setpos(140.5, 103)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 2:
            turtle.setpos(140.5, 33)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 3:
            turtle.setpos(140.5, -37)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 4:
            turtle.setpos(140.5, -107)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 5:
            turtle.setpos(140.5, -177)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

    elif move == 6:
        if row == 0:
            turtle.setpos(210.5, 173)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 1:
            turtle.setpos(210.5, 103)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 2:
            turtle.setpos(210.5, 33)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 3:
            turtle.setpos(210.5, -37)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 4:
            turtle.setpos(210.5, -107)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')

        elif row == 5:
            turtle.setpos(210.5, -177)
            if piece == 'R':
                turtle.dot(54, 'red')

            if piece == 'Y':
                turtle.dot(54, 'orange')


# wind condition
def winCondition():
    '''finds if 4 pieces of the same color are in the same row'''

    boardHeight = len(board[0])
    boardWidth = len(board)
    # check horizontal spaces
    for yCoord in range(boardHeight):
        for xCoord in range(boardWidth - 3):
            if (board[xCoord][yCoord] == redPiece and board[xCoord + 1][yCoord] == redPiece and
                board[xCoord + 2][yCoord] == redPiece and board[xCoord + 3][yCoord] == redPiece):
                return True

            elif (board[xCoord][yCoord] == orangePiece and board[xCoord + 1][yCoord] == orangePiece and
                board[xCoord + 2][yCoord] == orangePiece and board[xCoord + 3][yCoord] == orangePiece):
                return True

    # check vertical spaces
    for xCoord in range(boardWidth):
        for yCoord in range(boardHeight - 3):
            if (board[xCoord][yCoord] == redPiece and board[xCoord][yCoord + 1] == redPiece and
                board[xCoord][yCoord + 2] == redPiece and board[xCoord][yCoord + 3] == redPiece):
                return True

            elif (board[xCoord][yCoord] == orangePiece and board[xCoord][yCoord + 1] == orangePiece and
                board[xCoord][yCoord + 2] == orangePiece and board[xCoord][yCoord + 3] == orangePiece):
                return True

    # check / diagonal spaces
    for xCoord in range(boardWidth - 3):
        for yCoord in range(3, boardHeight):
            if (board[xCoord][yCoord] == redPiece and board[xCoord + 1][yCoord - 1] == redPiece and
                board[xCoord + 2][yCoord - 2] == redPiece and board[xCoord + 3][yCoord - 3] == redPiece):
                return True

            elif (board[xCoord][yCoord] == orangePiece and board[xCoord + 1][yCoord - 1] == orangePiece and
                board[xCoord + 2][yCoord - 2] == orangePiece and board[xCoord + 3][yCoord - 3] == orangePiece):
                return True

    # check \ diagonal spaces
    for xCoord in range(boardWidth - 3):
        for yCoord in range(boardHeight - 3):
            if (board[xCoord][yCoord] == redPiece and board[xCoord + 1][yCoord + 1] == redPiece and
                board[xCoord + 2][yCoord + 2] == redPiece and board[xCoord + 3][yCoord + 3] == redPiece):
                return True

            elif (board[xCoord][yCoord] == orangePiece and board[xCoord + 1][yCoord + 1] == orangePiece and
                board[xCoord + 2][yCoord + 2] == orangePiece and board[xCoord + 3][yCoord + 3] == orangePiece):
                return True

    return False

######## MAIN ########
def main():
    '''The main function executes the program'''
    welcomeScreen()
    turtle = tu.Turtle()
    screen = tu.Screen()
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    drawBoard(turtle, screen)
    for turn in range(42):
        if turn % 2 == 0:
            move, winCond = playerOne(turtle, screen, turn)
            if move == 8:
                screen.title('Player Two WINS!!! (Click to Exit the game)')
                break

            if winCond:
                screen.title('Player One WINS!!! (Click to Exit the game)')
                break

        else:
            move, winCond = playerTwo(turtle, screen, turn)
            if move == 8:
                screen.title('Player One WINS!!! (Click to Exit the game)')
                break

            if winCond:
                screen.title('Player Two WINS!!! (Click to Exit the game)')
                break

        if turn == 42:
            screen.title('Tie Game!')
    tu.exitonclick()


if __name__ == '__main__':
    main()
