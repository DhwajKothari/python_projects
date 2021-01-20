import random
random.seed()

def display(board):
    print(f"""{board[7]} | {board[8]} | {board[9]}
- - - - -
{board[4]} | {board[5]} | {board[6]}
- - - - -
{board[1]} | {board[2]} | {board[3]}""")


def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input('Player1: Please decide your marker: "X" or "O" ')
    if marker == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def place_marker(board, marker, position):
    board[position] = marker


def choose_first():
    if random.randint(0, 1) == 0:
        return "P1"
    return "P2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def win_check(board, mark):
    if board[9] == mark and board[8] == mark and board[7] == mark:
        return True
    elif board[6] == mark and board[5] == mark and board[4] == mark:
        return True
    elif board[3] == mark and board[2] == mark and board[1] == mark:
        return True

             # Columns
    elif board[3] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True

             # Diagonals
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    else:
        return False
    pass


def player_choice(board, player):
    pos = 0
    while pos not in range(1, 10) or not space_check(board, pos):
        if player == "P1":
            pos = int(input("Player 1: What is your next position, 1-9? "))
        else:
            pos = int(input("Player 2: What is your next position, 1-9? "))
    return pos


def replay():
    return input("Play again? Y or N? ") == 'Y'


print('Welcome to Tic Tac Toe!')

while True:
    board = [" " for _ in range(0, 10)]
    sel = player_input()
    player1_mark, player2_mark = sel
    turn = choose_first()
    print(turn + ' you go first!')
    game_on = True

    while game_on:
        position = player_choice(board, turn)
        if turn == "P1":
            place_marker(board, player1_mark, position)
            display(board)
            if win_check(board, player1_mark):
                print("Player 1 wins!")
                game_on = False
            elif full_board_check(board):
                print("Tie!!!!")
                game_on = False
            turn = "P2"
        else:
            place_marker(board, player2_mark, position)
            display(board)
            if win_check(board, player2_mark):
                print("Player 2 wins!")
                game_on = False
            elif full_board_check(board):
                print("Tie!!!!")
                game_on = False
            turn = "P1"

    if not replay():
        print()
        break
