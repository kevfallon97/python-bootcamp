import random

'''
Step 1: Write a function that can print out a board.
Set up your board as a list, where each index 1-9 corresponds with a number
on a number pad, so you get a 3 by 3 board representation.
'''
def display_board(board):
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")

'''
Step 2: Write a function that can take in a player input 
and assign their marker as 'X' or 'O'.
Think about using while loops to continually ask until you get a correct answer.
'''
def player_input():
    valid_marker = False
    while not valid_marker:
        player_marker = input("Please select player marker: ")
        if player_marker == "X" or player_marker == "O":
            valid_marker == True
            print(f"{player_marker} selected")
            return player_marker
        else:
            print("Invalid marker selected, please select a valid X or O marker")

'''
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), 
and a desired position (number 1-9) and assigns it to the board.
'''
def place_marker(board, marker, position):
    board[position] = marker

'''
Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
'''
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

'''
Step 5: Write a function that uses the random module to randomly
decide which player goes first.
You may want to lookup random.randint() Return a string of which player went first.
'''
def choose_first():
    if random.randint(1,10)%2 == 0:
        return "Player 1 is first."
    else:
        return "Player 2 is first."

'''
Step 6: Write a function that returns a boolean indicating whether 
a space on the board is freely available.
'''
def space_check(board, position):
    return board[position] == " "

'''
Step 7: Write a function that checks if the board is full and 
returns a boolean value. True if full, False otherwise.
'''
def full_board_check(board):
    for item in board:
        if item == " ":
            return False
        else:
            return True

'''
Step 8: Write a function that asks for a player's next position (as a number 1-9) 
and then uses the function from step 6 to check if it's a free position.
If it is, then return the position for later use.
'''
def player_choice(board):
    empty_position = False
    while not empty_position:
        position = int(input("Select a postion (1-9) "))
        if space_check(board, position):
            break
        else:
            print("This position is already filled.")
    return position

'''
Step 9: Write a function that asks the player if they want to play again and 
returns a boolean True if they do want to play again.
'''
def replay():
    play_again = input("Would you like to play again? ")
    if play_again == "Y":
        return True
    else:
        return False



# GAME LOGIC
test_board = ['#', ' ', ' ', ' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,' ']
player1marker = player_input()
if player1marker == 'X':
	player2marker = 'O'
else:
	player2marker = 'X'
markers = [player1marker, player2marker]

print(choose_first())
playing = True
while playing:
   for index, marker in enumerate(markers):
    	print(f"Player {index+1} turn.")

    	# display the current board state
    	display_board(test_board)

    	# enact the player's turn
    	position = player_choice(test_board)
    	place_marker(test_board, marker, position)
    	
    	# check victory conditions
    	if win_check(test_board, marker):
        	print(f"player {index+1} wins")
        	playing = False
        	break
    	else:
       		pass

