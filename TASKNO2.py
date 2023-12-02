Instructions = '''
This will be our tic tac toe board number positions.

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

*instructions:
1. Insert the spot number(1-9) to put your sign,
2. You must fill all 9 spots to get result,
3. AI bot will go first.
'''

name = input("Hello, What is your name? ")
print("\nHi, " + name)
print("Welcome to the Tic-Tac-Toe Game!!")

print(Instructions)
print("Let's Begin!!")

print("\nBot goes first! Good luck.")
print("\nPlayer = 'O'")
print("Bot = 'X'")

def print_board(board):
    print(f'{board[1]}  | {board[2]} | {board[3]}')
    print('---|---|---')
    print(f'{board[4]}  | {board[5]} | {board[6]}')
    print('---|---|---')
    print(f'{board[7]}  | {board[8]} | {board[9]}')
    print("\n")


def space_is_free(position, board):
    return board[position] == ' '


def insert_letter(letter, position, board):
    if space_is_free(position, board):
        board[position] = letter
        print_board(board)
        return True
    else:
        print("Can't insert there!")
        return False     # Indicate failure and provide an error message


def check_for_win(mark, board):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [7, 5, 3]
    ]
    for condition in win_conditions:
        if all(board[pos] == mark for pos in condition):
            return True
    return False


def check_draw(board):
    return all(board[key] != ' ' for key in board)


def player_move(board):
    while True:
        position = int(input("Enter the position for 'O': "))
        if insert_letter(player, position, board):
            return


def comp_move(board):
    best_score = -800
    best_move = 0      # Find the best move based on the minimax score without side effects
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key

    insert_letter(bot, best_move, board)


# Assuming the minimax algorithm is for a game like tic-tac-toe,
# and that the utility values for win, loss, and draw are 1, -1, and 0 respectively.

def minimax(board, depth, is_maximizing):
    if check_for_win(bot, board):
        return 1
    elif check_for_win(player, board):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                best_score = min(score, best_score)
        return best_score


board = {i: ' ' for i in range(1, 10)}

player = 'O'
bot = 'X'

while not (check_for_win(player, board) or check_for_win(bot, board) or check_draw(board)):
    comp_move(board)
    player_move(board)

if check_for_win(bot, board):
    print("BOT wins!")
elif check_for_win(player, board):
    print("Player wins!")
else:
    print("Draw!")