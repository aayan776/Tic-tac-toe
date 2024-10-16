def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
    #Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    #Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None
def is_full(board):
    return all(cell != " " for choice_row in board for cell in choice_row)
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        try:
            choice_row = int(input(f"{current_player}, choose row to place (0-2): "))
            choice_column = int(input(f"{current_player}, choose column to place (0-2): "))
            if board[choice_row][choice_column] == " ":
                board[choice_row][choice_column] = current_player
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print("Player has won!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("Its a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell already taken. Try again!")
        except (ValueError, IndexError):
            print("Error detected")
if __name__ == "__main__":
    main()