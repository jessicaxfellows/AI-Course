def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winning combination
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_idx = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[current_player_idx]
        row, col = map(int, input(f"Player {player}, enter your move (row[1-3] col[1-3]): ").split())
        row -= 1
        col -= 1

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player
            print_board(board)

            if check_winner(board, player):
                print(f"Player {player} wins! Congratulations!")
                break

            if is_board_full(board):
                print("It's a draw! Good game!")
                break

            current_player_idx = 1 - current_player_idx
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
