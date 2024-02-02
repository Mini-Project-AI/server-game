class MinMaxAlgorithm:
    """  Represents a Minimax algorithm for finding the best move in a game.

    This class implements the Minimax algorithm for finding the best move in a 
    two-player game represented by a board.

    Attributes:
        EMPTY (int): A constant representing an empty cell on the game board.
        MAX_PLAYER (int): A constant representing the maximizing player.
        MIN_PLAYER (int): A constant representing the minimizing player.
    """

    EMPTY = 0
    MAX_PLAYER = 1
    MIN_PLAYER = -1

    def __init__(self, board):
        """ Initializes the MinMaxAlgorithm with the given board.

        Args:
            board (Board): The current state of the game board.
        """
        self.board = board


    def min_max_best_move(self):

        """ Calculates the best move using the Minimax algorithm.

        Returns:
            tuple or None: The best move coordinates (row, col) if available, None otherwise.
        """
        def max_value(board):
            """ Helper function for Minimax algorithm to calculate max value.

            Args:
                board (Board): The current state of the game board.

            Returns:
                float: The maximum utility value for the maximizing player.
            """

            # Base case: If the game is over, return the utility value
            if board.is_game_over():
                return board.utility()

            # Initialize the best score for maximizing player
            best_score = float('-inf')

            # Loop through all possible moves
            for move in board.get_possible_moves():
                # Apply the move to a copy of the board
                new_board = board.make_move(move, self.MAX_PLAYER)
                # Recursively find the max value for the next level (minimizing player's turn)
                score = min_value(new_board)
                # Update the best score
                best_score = max(best_score, score)

            return best_score


        def min_value(board):
            """ Helper function for Minimax algorithm to calculate min value.

            Args:
                board (Board): The current state of the game board.

            Returns:
                float: The minimum utility value for the minimizing player.
            """
            # Base case: If the game is over, return the utility value
            if board.is_game_over():
                return board.utility()

            # Initialize the best score for minimizing player
            best_score = float('inf')

            # Loop through all possible moves
            for move in board.get_possible_moves():
                # Apply the move to a copy of the board
                new_board = board.make_move(move, self.MIN_PLAYER)
                # Recursively find the min value for the next level (maximizing player's turn)
                score = max_value(new_board)
                # Update the best score
                best_score = min(best_score, score)

            return best_score

        # Start with the maximizing player (e.g., computer)
        best_move = None
        best_score = float('-inf')

        # Loop through all possible moves
        for move in self.board.get_possible_moves():
            # Apply the move to a copy of the board
            new_board = self.board.make_move(move, self.MAX_PLAYER)
            # Calculate the score using the min_value function
            score = min_value(new_board)
            # Update the best move and score if the current move is better
            if score > best_score:
                best_move = move
                best_score = score

        return best_move