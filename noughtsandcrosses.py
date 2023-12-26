import random #generates random numbers

import os.path #implemets some useful function or path name

import json #user will be able to import and parse json data into google sheets 

random.seed() # sets the random number generator 

def draw_board(board):

 # board [0][0] = rows and coloums i.e row = 0 coloum = 0

    print('-----------')

    print('|' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]+'|')

    print('-----------')

    print('|' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2]+'|')

    print('-----------')

    print('|' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2]+'|')

    print('-----------')

def welcome(board):

    print('Welcome to the "Unbeatable Noughts and crosses" game.\nThe board layout is shown below: ')

#calling above board 

    draw_board(board) 

    print('When prompted, enter the number corresponding to the square you want.')

def initialise_board(board): 

# to make rows and coloum together with no space

    for row in range(3):

        for coloum in range(3):

            board[row][coloum] = ' '

def get_player_move(board):

    while True: 

#while loop because we dont know how long will the game continue for

        player_move= input(" 1,2,3 \n 4,5,6 \n 7,8,9 \n choose your square : ")

        if player_move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: 

#checking if user input is in any of these

            player_move = int(player_move) -1

#checking if the cell user wants to enter is empty or occupied 

            if board[int(player_move/3)][player_move % 3] == ' ':  

#returning values if cell is empty 

                return int(player_move /3), player_move % 3 

            else:

                print("This block is already captured.Please enter value in another space")

        else:

            print("Invalid input. Please enter a number between 1 and 9.")

def choose_computer_move(board):

    for row in range(3):

        for coloum in range(3):

#asking computer to check cell is empty or not 

            if board[row][coloum] == ' ': 
# if its empty then com will asked to return value 
                return row, coloum
def check_for_win(board, mark):

    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
    
        (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
        
        (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
        
        (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
        
        (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
        
        (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
        
        (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
        
        (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):

        return True

    else:

        return False


def check_for_draw(board):

    for row in range(3):

        for coloum in range(3):

            if board[row][coloum] == ' ':

                return False

    return True

def play_game(board):

    initialise_board(board)

    while True:

        player_move = get_player_move(board)

        if player_move != None:

            board[player_move[0]][player_move[1]] = "X"

            draw_board(board)

            if check_for_win(board, "X"):

                return 1

            elif check_for_draw(board):

                return 0

            computer_move = choose_computer_move(board)

            board[computer_move[0]][computer_move[1]] = "O" #computer inputs 0

            print("Computer made the choice now your turn")

            draw_board(board)

            if check_for_win(board, "O"):

                return -1 #if computer wins return -1 as players score

            elif check_for_draw(board):

                return 0 #if draw then show 0

            else:

                continue

def menu():

    # Loop run continuously until user input correct data

    while True:

        choice = input("Enter one of the given options : \n 1 - Play the game \n 2 - Save your score in the leaderboard \n 3 - load and display the leaderboard  \n q - End the program \n 1,2,3 or q ? ")

        if choice in ['1', '2', '3', 'q']:

            return choice

        else:

            print("Invalid input. Please enter data from only given options")


def load_scores():

    try:
        f = open("leaderboard.txt", "r")
        file = f.read()
        leaderboard = json.load(file)

        with open("leaderboard.txt", "r") as file:

            leaderboard = json.load(file)

    except:
#if the text file doesnt exist, the new file will be created 

        leaderboard = {}

    return leaderboard

def save_score(score):

    player_name = input("Enter your name: ")

    try:
    
       f = open("leaderboard.txt", "r")
       file = f.read()
       data = json.load(file)

    except:

        data = {}

    data[player_name] = score

    with open("leaderboard.txt", "w") as file:

        json.dump(data, file)


def display_leaderboard(leaders):

    print("Name: Score")

    for name, score in leaders.items():

        print(f"{name}: {score}")

def main():

    board = [ ['1','2','3'],\ #giving value to board
              ['4','5','6'],\
              ['7','8','9']]

    welcome(board) #printing the outline of board
    
    total_score = 0
    
    while True:
        choice = menu()

        if choice == '1':

            score = play_game(board)

            total_score += score

            print('Your current score is:',total_score)

        if choice == '2':

            save_score(total_score)

        if choice == '3':

            leader_board = load_scores()
            
            display_leaderboard(leader_board)

        if choice == 'q':
        
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            
            print('Good bye')
            
            return

# Program execution begins here
if __name__ == '__main__':

    main()
