class TicTacToe:
    def __init__(self):
        # Initialize the board as a 3x3 grid (list of lists)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X goes first
        self.winner = None
        # Counters for node evaluations (for comparison)
        self.minimax_nodes = 0
        self.alphabeta_nodes = 0

    def print_board(self):
        """Print the current board state with borders"""
        print("-------------")
        for row in self.board:
            print("|", end=" ")
            for cell in row:
                print(cell, end=" | ")
            print("\n-------------")

    def make_move(self, row, col):
        """Make a move on the board"""
        # Check if the position is valid and empty
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.check_winner(row, col)
            self.switch_player()
            return True
        return False

    def switch_player(self):
        """Switch between X and O players"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        """Check if the last move caused a win"""
        # Check row
        if all(cell == self.current_player for cell in self.board[row]):
            self.winner = self.current_player
            return
        
        # Check column
        if all(self.board[i][col] == self.current_player for i in range(3)):
            self.winner = self.current_player
            return
        
        # Check diagonals
        if (row == col and all(self.board[i][i] == self.current_player for i in range(3))):
            self.winner = self.current_player
            return
        
        if (row + col == 2 and all(self.board[i][2-i] == self.current_player for i in range(3))):
            self.winner = self.current_player
            return

    def is_board_full(self):
        """Check if the board is full (tie)"""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_game_over(self):
        """Check if the game has ended"""
        return self.winner is not None or self.is_board_full()

    def get_empty_cells(self):
        """Return list of (row,col) for empty cells"""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def minimax(self, is_maximizing):
        """Original minimax algorithm (unchanged)"""
        self.minimax_nodes += 1  # Count node evaluation
        # Base cases - return score if game over
        if self.winner == 'X': return 1   # AI wins
        if self.winner == 'O': return -1  # Human wins
        if not self.get_empty_cells(): return 0  # Tie

        if is_maximizing:  # AI's turn (X)
            best_score = -1000
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        self.check_winner(row, col)
                        score = self.minimax(False)
                        self.board[row][col] = ' '
                        self.winner = None
                        best_score = max(score, best_score)
            return best_score
        else:  # Human's turn (O)
            best_score = 1000
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'O'
                        self.check_winner(row, col)
                        score = self.minimax(True)
                        self.board[row][col] = ' '
                        self.winner = None
                        best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        """Find the best move for the AI using minimax (unchanged)"""
        best_score = -1000
        best_move = None
        
        for (r, c) in self.get_empty_cells():
            self.board[r][c] = 'X'  # AI's move
            self.check_winner(r, c)  # Update winner status
            score = self.minimax(False)
            self.board[r][c] = ' '  # Undo move
            self.winner = None      # Reset winner
            
            # Prioritize immediate wins
            if score == 1: 
                return (r, c)

            if score > best_score:
                best_score = score
                best_move = (r, c)
        
        return best_move

    def alphabeta(self, is_maximizing, alpha, beta):
        """Alpha-beta pruning algorithm"""
        self.alphabeta_nodes += 1  # Count node evaluation
        # Base cases - return score if game over
        if self.winner == 'X': return 1   # AI wins
        if self.winner == 'O': return -1  # Human wins
        if not self.get_empty_cells(): return 0  # Tie

        if is_maximizing:  # AI's turn (X)
            best_score = -1000
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        self.check_winner(row, col)
                        score = self.alphabeta(False, alpha, beta)
                        self.board[row][col] = ' '
                        self.winner = None
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)  # Update alpha
                        if beta <= alpha:  # Prune if beta <= alpha
                            break
                if beta <= alpha:  # Prune outer loop too
                    break
            return best_score
        else:  # Human's turn (O)
            best_score = 1000
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'O'
                        self.check_winner(row, col)
                        score = self.alphabeta(True, alpha, beta)
                        self.board[row][col] = ' '
                        self.winner = None
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)  # Update beta
                        if beta <= alpha:  # Prune if beta <= alpha
                            break
                if beta <= alpha:  # Prune outer loop too
                    break
            return best_score

    def find_best_move_alphabeta(self):
        """Find the best move for the AI using alpha-beta pruning"""
        best_score = -1000
        best_move = None
        
        for (r, c) in self.get_empty_cells():
            self.board[r][c] = 'X'  # AI's move
            self.check_winner(r, c)  # Update winner status
            score = self.alphabeta(False, -1000, 1000)  # Start with wide alpha/beta
            self.board[r][c] = ' '  # Undo move
            self.winner = None      # Reset winner
            
            # Prioritize immediate wins
            if score == 1: 
                return (r, c)

            if score > best_score:
                best_score = score
                best_move = (r, c)
        
        return best_move

def play_game(use_alphabeta=False):
    """Play a game of Tic-Tac-Toe, comparing minimax and alpha-beta pruning"""
    game = TicTacToe()
    # Initialize cumulative node counters
    total_minimax_nodes = 0
    total_alphabeta_nodes = 0
    
    while not game.is_game_over():
        game.print_board()
        
        if game.current_player == 'X':  # AI's turn
            print("AI is thinking...")
            # Reset node counters for this move
            game.minimax_nodes = 0
            game.alphabeta_nodes = 0
            
            # Run both algorithms to compare nodes (but only apply one move)
            minimax_move = game.find_best_move()  # Run minimax
            minimax_nodes = game.minimax_nodes    # Store node count
            game.minimax_nodes = 0                # Reset for next use
            
            alphabeta_move = game.find_best_move_alphabeta()  # Run alpha-beta
            alphabeta_nodes = game.alphabeta_nodes            # Store node count
            game.alphabeta_nodes = 0                          # Reset for next use
            
            # Choose which move to apply based on use_alphabeta
            row, col = alphabeta_move if use_alphabeta else minimax_move
            game.make_move(row, col)
            
            # Update cumulative counters
            total_minimax_nodes += minimax_nodes
            total_alphabeta_nodes += alphabeta_nodes
            
            # Print per-move comparison
            print(f"\nMove Comparison:")
            print(f"Nodes evaluated by Minimax: {minimax_nodes}")
            print(f"Nodes evaluated by Alpha-Beta: {alphabeta_nodes}")
            print(f"Alpha-Beta saved {minimax_nodes - alphabeta_nodes} nodes this move")
        
        else:  # Human's turn
            print(f"Player {game.current_player}'s turn")
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if game.make_move(row, col):
                        break
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter numbers 0, 1, or 2!")
    
    game.print_board()
    if game.winner:
        print(f"Player {game.winner} wins!")
    else:
        print("It's a tie!")
    
    # Final comparison
    print("\nPerformance Comparison:")
    print(f"Total nodes evaluated by Minimax: {total_minimax_nodes}")
    print(f"Total nodes evaluated by Alpha-Beta: {total_alphabeta_nodes}")
    savings = total_minimax_nodes - total_alphabeta_nodes
    print(f"Alpha-Beta saved {savings} nodes compared to Minimax")
    if total_minimax_nodes > 0:
        percent_saved = (savings / total_minimax_nodes) * 100
        print(f"Percentage of nodes saved: {percent_saved:.2f}%")
# Start the game (choose True for alpha-beta, False for minimax)
play_game(use_alphabeta=True)  # Change to False to test minimax