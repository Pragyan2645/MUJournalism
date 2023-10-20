# Tic-Tac-Toe Game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:              # this for loop is checking row wise combinations for winning
        if all(cell == player for cell in row):
            return True

    for col in range(3):           # this for loop is for checking winning probability column wise
        if all(board[row][col] == player for row in range(3)):
            return True

# this condition is to check winning probability diagonally
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):       # this function checks if all cells are filled
    if all(cell != " " for row in board for cell in row):
        return True

if __name__ == "__main__":
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":               # this condition checks if user is not entering invalid index value or overwritting any cell because lists are mutable
            print("Invalid move. Try again.")
            continue

        board[row][col] = player

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


        # if we put any invalid input
