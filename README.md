# CT-22097
# Tic-Tac-Toe with Minimax and Alpha-Beta Pruning

This Python implementation of Tic-Tac-Toe demonstrates two AI algorithms:
1. Minimax algorithm
2. Minimax with Alpha-Beta pruning

The program allows you to play against the AI and compares the performance of these two algorithms in terms of nodes evaluated.

## Features

- Classic 3x3 Tic-Tac-Toe game
- Human vs AI gameplay
- Two AI algorithms implemented:
  - Standard Minimax
  - Minimax with Alpha-Beta pruning
- Performance comparison showing nodes evaluated by each algorithm
- Visual board display

## How It Works

### Game Logic
- The game board is represented as a 3x3 grid
- Player 'X' (AI) goes first, followed by player 'O' (human)
- The game checks for wins after each move
- The game ends when either player wins or the board is full

### AI Algorithms

#### Minimax
- Recursively evaluates all possible moves
- Assigns scores: +1 for AI win, -1 for human win, 0 for tie
- Chooses moves that maximize the AI's advantage

#### Alpha-Beta Pruning
- An optimized version of Minimax
- Prunes branches that cannot affect the final decision
- Maintains alpha (best already explored for maximizer) and beta (best already explored for minimizer) values
- Cuts off search when beta <= alpha

### Performance Comparison
- Tracks nodes evaluated by both algorithms
- Shows per-move and total node counts
- Calculates percentage of nodes saved by Alpha-Beta pruning

## How to Run

1. Copy the code into a Python file (e.g., `tictactoe.py`)
2. Run the file with Python 3: `python tictactoe.py`
3. To switch between algorithms, change the last line:
   - `play_game(use_alphabeta=True)` for Alpha-Beta pruning
   - `play_game(use_alphabeta=False)` for standard Minimax

## Gameplay Instructions

1. The AI (X) moves first
2. On your turn (O), enter row and column numbers (0-2)
   - Example: Enter "1" for row and "1" for column to select the center square
3. The game continues until someone wins or the board is full
4. After each game, you'll see performance statistics comparing the algorithms

## Implementation Notes

- The AI always plays as 'X' and goes first
- The board is reset after each game
- Node counts are cumulative across all moves in a game
- The program shows both algorithms' node counts even when using just one, for comparison

## Performance Observations

- Alpha-Beta pruning typically evaluates significantly fewer nodes than standard Minimax
- The savings are most dramatic in the early game when more moves are possible
- Both algorithms always choose the same optimal moves - pruning doesn't affect move quality

Enjoy playing Tic-Tac-Toe against an unbeatable AI opponent!
