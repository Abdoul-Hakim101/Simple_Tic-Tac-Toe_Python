def print_board(game_board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(game_board[i][j], end=" ")
        print("|")
    print("---------")


def create_board():
    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(" ")
    return board


def check_coordinates(coordinate):
    try:
        i = int(coordinate[0])
        j = int(coordinate[1])
    except Exception:
        print("You should enter numbers!")
        return False
    else:
        if i > 3 or i < 1 or j > 3 or j < 1:
            print("Coordinates should be from 1 to 3!")
            return False
    return True


def make_move(char):
    x = int(coordinates[0])
    y = int(coordinates[1])
    if game_board[x - 1][y - 1] == " ":
        game_board[x - 1][y - 1] = char
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False


def check_game_states(char):
    for i in range(3):
        # horizontal
        if game_board[i][0] == char and game_board[i][1] == char and game_board[i][2] == char:
            print(f"{char} wins")
            exit(0)
        # vertical
        if game_board[0][i] == char and game_board[1][i] == char and game_board[2][i] == char:
            print(f"{char} wins")
            exit(0)
    # diagonal
    for i in range(0, 4, 2):
        if game_board[0][i] == char and game_board[1][1] == char and game_board[2][2 - i] == char:
            print(f"{char} wins")
            exit(0)
    # draw
    count = 0
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == 'X' or game_board[i][j] == "O":
                count += 1
    if count == 9:
        print('Draw')
        exit(0)


game_board = create_board()
print_board(game_board)
x_turn = True
while True:
    coordinates = input().split()
    if check_coordinates(coordinates):
        if x_turn:
            if make_move("X"):
                print_board(game_board)
                check_game_states('X')
                x_turn = False
        else:
            if make_move("O"):
                print_board(game_board)
                check_game_states('O')
                x_turn = True
