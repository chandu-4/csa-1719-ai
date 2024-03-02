def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate(board):
    # Check rows, columns, and diagonals for a win or loss
    for row in board:
        if all(cell == "X" for cell in row):
            return -1  # Player X wins
        elif all(cell == "O" for cell in row):
            return 1  # Player O wins

    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return -1  # Player X wins
        elif all(board[row][col] == "O" for row in range(3)):
            return 1  # Player O wins

    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return -1  # Player X wins

    if all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return 1  # Player O wins

    return 0  # No winner

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score != 0:
        return score

    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float("-inf")
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        player_move = input("Enter your move (row, col) or 'q' to quit: ")
        if player_move == 'q':
            break

        row, col = map(int, player_move.split(','))

        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Invalid move, try again.")
            continue

        if evaluate(board) == -1:
            print_board(board)
            print("You win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print("Computer's move:")
        comp_row, comp_col = best_move(board)
        board[comp_row][comp_col] = "O"

        if evaluate(board) == 1:
            print_board(board)
            print("Computer wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
