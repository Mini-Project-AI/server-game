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

    def __init__(self, board, heuristic=False, depth=0):
        """ Initializes the MinMaxAlgorithm with the given board.

        Args:
            board (Board): The current state of the game board.
        """
        self.board = board
        self.heuristic = heuristic
        self.depth = depth

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
            if (self.heuristic == False):
                score = min_value(new_board)
            else:
               score = self.heuristic_evaluation(new_board)
            # Update the best move and score if the current move is better
            if score > best_score:
                best_move = move
                best_score = score
        return best_move

    """
    Heuristic game 
    """

    def heuristic_evaluation(self):
        """
        Evaluates the current board state using a heuristic function and returns a numerical score.

        Returns:
            int: The numerical score representing the desirability of the current board state.
        """
        # Define heuristic weights for different board configurations
        heuristic_weights = {
            "win": 100,    # Winning move
            "block": 50,   # Blocking opponent from winning
            "fork": 30,    # Creating a fork (two winning paths)
            "center": 10,  # Occupying the center cell
            "edge": 5,     # Occupying an edge cell
            "corner": 3    # Occupying a corner cell
        }

        # Evaluate the board state based on heuristic weights
        score = 0
        # Check for winning moves (rows, columns, diagonals)
        if self.board.check_winner(self.MAX_PLAYER):
            score += heuristic_weights["win"]
        elif self.board.check_winner(self.MIN_PLAYER):
            score -= heuristic_weights["win"]
        else:
            # Check for potential winning moves and blocking moves
            for move in self.board.get_possible_moves():
                new_board = self.board.make_move(move, self.MAX_PLAYER)
                if new_board.check_winner(self.MAX_PLAYER):
                    score += heuristic_weights["block"]
                new_board = self.board.make_move(move, self.MIN_PLAYER)
                if new_board.check_winner(self.MIN_PLAYER):
                    score -= heuristic_weights["block"]
            # Check for creating forks
            forks = self.check_forks()

            # Check for occupying center cell
            score += forks * heuristic_weights["fork"]
            if self.board.matrix[1][1] == self.MAX_PLAYER:
                score += heuristic_weights["center"]

            # Check for occupying edge cells
            edge_score = self.check_edge_occupancy()
            score += edge_score * heuristic_weights["edge"]

             # Check for occupying corner cells
            corner_score = self.check_corner_occupancy()
            score += corner_score * heuristic_weights["corner"]
            return score
    
    def check_forks(self):
        """
        Checks for the presence of forks in the current board state.

        Returns:
                int: The number of forks found.
        """
        # Initialize counter for forks
        forks = 0

        # Implement logic to count forks
        # Example: Iterate through possible moves and check if they lead to multiple winning paths
        for move in self.board.get_possible_moves():
            # Simulate move for maximizing player
            new_board_max = self.board.make_move(move, self.MAX_PLAYER)
            # Check if move creates multiple winning paths for maximizing player
            if new_board_max.check_winner(self.MAX_PLAYER):
                forks += 1
        return forks


    def check_edge_occupancy(self):
        """
        Checks the occupancy of edge cells in the current board state.

        Returns:
                int: The number of edge cells occupied by the maximizing player.
        """
        # Initialize counter for occupied edge cells
        occupied_edges = 0

        # Implement logic to count occupied edge cells
        # Example: Iterate through edge cells and count those occupied by the maximizing player
        for edge in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            if self.board.matrix[edge[0]][edge[1]] == self.MAX_PLAYER:
                occupied_edges += 1

        return occupied_edges


    def check_corner_occupancy(self):
        """
        Checks the occupancy of corner cells in the current board state.

        Returns:
            int: The number of corner cells occupied by the maximizing player.
        """
        # Initialize counter for occupied corner cells
        occupied_corners = 0

        # Implement logic to count occupied corner cells
        # Example: Iterate through corner cells and count those occupied by the maximizing player
        for corner in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if self.board.matrix[corner[0]][corner[1]] == self.MAX_PLAYER:
                occupied_corners += 1

        return occupied_corners
