import math

board = [' ' for x in range(9)]

def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return board[combination[0]]
    
    if ' ' not in board:
        return 'Draw'
    return None

#applying minimax algorithm to tic tac toe game
#here x is the maximizing player and o is the minimizing player
#we are considering the both the players are playing optimally

def minimax_search(board, is_maximizing):
    # Check for terminal states
    if check_winner(board, 'x'):
        return 1
    elif check_winner(board, 'o'):
        return -1
    elif ' ' not in board:  # Draw
        return 0
    
    #defining the best score for the maximizing player
    if is_maximizing:
        best_score  = -float('inf')
        #here -float('inf') is used to represent the worst score for the maximizing player
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'x'
                score = minimax_search(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i  in range(9):
            if board[i] == ' ' :
                board[i] = 'o'
                score = minimax_search(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
    
def finding_best_move(board):
        best_score = - float(math.inf)
        move = None

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'x'
                score = minimax_search(board, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i

        return move

#driving code
while True:
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == ' ':
        board[player_move] = 'o'
    else:
        print("Invalid move. Try again.")
        continue
    
    if check_winner(board, 'o'):
        print("Congratulations! You win!")
        break
    
    ai_move = finding_best_move(board)
    print(f"AI chooses move: {ai_move}")
    if ai_move is not None:
        board[ai_move] = 'x'
    
    if check_winner(board, 'x'):
        print("AI wins! Better luck next time.")
        break
    
    if check_winner(board, None) == 'Draw':
        print("It's a draw!")
        break

    