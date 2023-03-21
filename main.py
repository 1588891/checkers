
board1 = ['X', '', 'X', 'O', 'O', '', '', 'X', 'O']
board2 = ['X', '', 'X', 'O', 'O', 'O', 'X', 'X', 'O']
board3 = ['X', '', 'X', 'X', 'O', 'O', 'X', '', 'O']
board4 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O']
board5 = ['', '', '', '', 'O', '', 'X', '', '']


def get_winner(board):
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return 'winner to X'
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        return 'winner to X'
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return 'winner to X'
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        return 'winner to X'
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        return 'winner to X'
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return 'winner to X'
    elif board[0] == 'X' and board[4] == 'X' and board[2] == 'X':
        return 'winner to X'
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return 'winner to X'
    

    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        return 'winner to O'
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        return 'winner to O'
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return 'winner to O'
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        return 'winner to O'
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        return 'winner to O'
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return 'winner to O'
    elif board[0] == 'O' and board[4] == 'O' and board[2] == 'O':
        return 'winner to O'
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return 'winner to O'

    else:
        return 'no winner'






print(get_winner(board1))
print(get_winner(board2))
print(get_winner(board3))
print(get_winner(board4))
print(get_winner(board5))