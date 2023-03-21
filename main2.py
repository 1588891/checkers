board1 = ['X', '', 'X', 'O', 'O', '', '', 'X', 'O']
board2 = ['X', '', 'X', 'O', 'O', 'O', 'X', 'X', 'O']
board3 = ['X', '', 'X', 'X', 'O', 'O', 'X', '', 'O']
board4 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O']
board5 = ['', '', '', '', 'O', '', 'X', '', '']


def get_winner(board):
    winner = None
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        winner = "X"
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        winner = "X"
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        winner = "X"
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        winner = "X"
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        winner = "X"
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        winner = "X"
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        winner = "X"
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        winner = "X"
    

    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        winner = "O"
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        winner = "O"
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        winner = "O"
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        winner = "O"
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        winner = "O"
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        winner = "O"
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        winner = "O"
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        winner = "O"

    return winner


def tic_tac_toe(move,place):
    if move == str(move) and place == str(place):
        place = int(place)
        list[place] = move.upper()
        string = f'Tic,Tac,Toe\n   {list[0]}|{list[1]}|{list[2]}    0|1|2\n   {list[3]}|{list[4]}|{list[5]}    3|4|5\n   {list[6]}|{list[7]}|{list[8]}    6|7|8'
        return string
    else:
        return 'Not valid input'

list = ['_','_','_','_','_','_','_','_','_']
string = f'Tic,Tac,Toe\n   {list[0]}|{list[1]}|{list[2]}    0|1|2\n   {list[3]}|{list[4]}|{list[5]}    3|4|5\n   {list[6]}|{list[7]}|{list[8]}    6|7|8'
print(string)
turn = "X"
while True:

    game_winner = get_winner(list)

    if game_winner:
        print(f'{game_winner} has won.')
        break 

    else:
        # user_input = input('\nType an ( X ) or ( O )\nLets play! --->')
        print(f"{turn}, It's your turn!")
        user_input2 = input('Select a number from the diagram to choose where would you like to go: ')
        print(tic_tac_toe(turn,user_input2))
        if turn == "X":
            turn = 'O'
        else:
            turn = "X"




# print(get_winner(board2))
# print(get_winner(board3))
# print(get_winner(board4))
# print(get_winner(board5))
