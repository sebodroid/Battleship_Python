import string
import pprint

#THIS IS A FUNCTION THAT WILL CREATE THE BOARD AND PLACE THE SHIPS FOR THE USER 
def create_board(a, b): 
    lst = [[ [0 for col in range(a)] for col in range(b)]]

    #Numbering the board columns and rows
    number = 0
    for i in range(10):
        lst [0][0][number] = number
        lst [0][number][0] = number
        number+=1

    ship1 = 2
    ship2 = 3 
    ship3 = 4
    move = 0

    #POSITIONING FOR SHIP 1
    ship1_row = input("\nRow for ship one(1-9): ")
    ship1_row = int(ship1_row)

    ship1_colum = input("Colunm for ship one(1-9): ")
    ship1_colum = int(ship1_colum)

    up_down_left_right = input("Choose up, down, left, right: ")

    if up_down_left_right == "right":
        for ship in range(ship1):
            lst[0][ship1_colum][ship1_row + move] = ship1
            move = move + 1
  
    elif up_down_left_right == "left":
        for ship in range(ship1):
            lst[0][ship1_colum][ship1_row - move] = ship1
            move = move + 1
    
    elif up_down_left_right == "up":
        for ship in range(ship1):
            lst[0][ship1_colum - move][ship1_row] = ship1
            move = move + 1
    
    elif up_down_left_right == "down":
        for ship in range(ship1):
            lst[0][ship1_colum + move][ship1_row] = ship1
            move = move + 1
    
    #POSITIONING FOR SHIP 2
    move = 0
    ship2_row = input("\nRow for ship two(1-9): ")
    ship2_row = int(ship2_row)

    ship2_colum = input("Colunm for ship two(1-9): ")
    ship2_colum = int(ship2_colum)

    up_down_left_right = input("Choose up, down, left, right: ")

    if up_down_left_right == "right":
        for ship in range(ship2):
            lst[0][ship2_colum][ship2_row + move] = ship2
            move = move + 1
  
    elif up_down_left_right == "left":
        for ship in range(ship2):
            lst[0][ship2_colum][ship2_row - move] = ship2
            move = move + 1
    
    elif up_down_left_right == "up":
        for ship in range(ship2):
            lst[0][ship2_colum - move][ship2_row] = ship2
            move = move + 1
    
    elif up_down_left_right == "down":
        for ship in range(ship2):
            lst[0][ship2_colum + move][ship2_row] = ship2
            move = move + 1

#POSITIONING FOR SHIP 3
    move = 0
    ship3_row = input("\nRow for ship three(1-9): ")
    ship3_row = int(ship3_row)

    ship3_colum = input("Colunm for ship two(1-9): ")
    ship3_colum = int(ship3_colum)

    up_down_left_right = input("Choose up, down, left, right: ")

    if up_down_left_right == "right":
        for ship in range(ship3):
            lst[0][ship3_colum][ship3_row + move] = ship3
            move = move + 1
  
    elif up_down_left_right == "left":
        for ship in range(ship3):
            lst[0][ship3_colum][ship3_row - move] = ship3
            move = move + 1
    
    elif up_down_left_right == "up":
        for ship in range(ship3):
            lst[0][ship3_colum - move][ship3_row] = ship3
            move = move + 1
    
    elif up_down_left_right == "down":
        for ship in range(ship3):
            lst[0][ship3_colum + move][ship3_row] = ship3
            move = move + 1

    return lst 

#Create the empty boards for the players to use to attack
def create_emptyboard(a, b): 
    lst = [[ [0 for col in range(a)] for col in range(b)]]
    
    number = 0
    for i in range(10):
        lst [0][0][number] = number
        lst [0][number][0] = number
        number+=1
    
    return lst

def attack(enemy_board, board_to_attack,row, column):

    ship_number = 0

    if enemy_board[0][column][row] == 2 or enemy_board[0][column][row] == 3 or enemy_board[0][column][row] == 4: 
        print("Hit at Row:" + str(row) + "\tColumn:" + str(column))

        board_to_attack[0][column][row] = 'X'

    else:
        print("\nMISS\n")
        board_to_attack[0][column][row] = 'O'

    pprint.pprint(board_to_attack)

    if enemy_board[0][column][row] == 2:
        ship_number = 2
        return ship_number 
    
    elif enemy_board[0][column][row] == 3:
        ship_number = 3
        return ship_number
    
    elif enemy_board[0][column][row] == 4:
        ship_number = 4
        return ship_number
    
def ship_destroyed(ship1,ship2,ship3):

    Game_Over = False

    if ship1 == 2:
        print("The SMALL ship has been destroyed")
    if ship2 == 3:
        print("The MEDIUM ship has been destroyed")
    if ship3 == 4:
        print("The LARGE ship has been destroyed")
    
    if ship1 == 2 and ship2 == 3 and ship3 == 4:
        Game_Over = True
        print("The game is over")

    
    return Game_Over










#CALLING THE FUNCTION create_board TO CREATE THE BOARD FOR USER 2
#board1 = create_board(10,10)
empty_board1 = create_emptyboard(10,10)


#CALLING THE FUNCTION create_board TO CREATE THE BOARD FOR USER 2
print("\nUser 2 pick your ships")
board2 = create_board(10,10)
empty_board2 = create_emptyboard(10,10)


#USER 1 SHIPS
user1_ship1 = 0
user1_ship2 = 0
user1_ship3 = 0

#USER 2 SHIPS
user2_ship1 = 0
user2_ship2 = 0
user2_ship3 = 0

print('\n\n')
pprint.pprint(board2)

numm = 0

attack_row = 0

attack_column = 0

attacks = None

Game = False

while Game == False:

    attack_row = int(input("Pick a row to attack: "))
    attack_column = int(input("Pick a column to attack: "))

    attacks = attack(board2,empty_board1,attack_row,attack_column)

    numm+= 1

    if attacks == 2:
        user2_ship1 += 1
    if attacks == 3:
        user2_ship2 += 1
    if attacks == 4:
        user2_ship3 += 1

    Game = ship_destroyed(user2_ship1,user2_ship2,user2_ship3)
