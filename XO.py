def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)



def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False



def player_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False



def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        display_board(board)
        player = players[turn % 2]
        print(f"Ход игрока {player}")

        row = int(input("Введите номер строки (0, 1, 2): "))
        col = int(input("Введите номер столбца (0, 1, 2): "))

        if player_move(board, row, col, player):
            if check_win(board, player):
                display_board(board)
                print(f"Игрок {player} победил!")
                break
            if all([cell != " " for row in board for cell in row]):
                display_board(board)
                print("Ничья!")
                break
            turn += 1
        else:
            print("Некорректный ход. Попробуйте снова.")


tic_tac_toe()
