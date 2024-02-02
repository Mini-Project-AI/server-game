class AlphaBetaAlgorithm:
    EMPTY = 0
    MAX_PLAYER = 1
    MIN_PLAYER = -1

    def __init__(self, board):
        """
        Initializes the AlphaBetaAlgorithm with the given board.

        Args:
            board (Board): The current state of the game board.
        """
        self.board = board

    def alpha_beta_best_move(self):
        """
        Calculates the best move using the Alpha-Beta Pruning algorithm.

        Returns:
            tuple or None: The best move coordinates (row, col) if available, None otherwise.
        """
        def max_value(board, alpha, beta):
            """
            Helper function for Alpha-Beta Pruning algorithm to calculate max value.

            Args:
                board (Board): The current state of the game board.
                alpha (float): The alpha value for pruning.
                beta (float): The beta value for pruning.

            Returns:
                float: The maximum utility value for the maximizing player.
            """
            if board.is_game_over():
                return board.utility()

            best_score = float('-inf')

            for move in board.get_possible_moves():
                new_board = board.make_move(move, self.MAX_PLAYER)
                score = min_value(new_board, alpha, beta)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Beta cut-off
            return best_score

        def min_value(board, alpha, beta):
            """
            Helper function for Alpha-Beta Pruning algorithm to calculate min value.

            Args:
                board (Board): The current state of the game board.
                alpha (float): The alpha value for pruning.
                beta (float): The beta value for pruning.

            Returns:
                float: The minimum utility value for the minimizing player.
            """
            if board.is_game_over():
                return board.utility()

            best_score = float('inf')

            for move in board.get_possible_moves():
                new_board = board.make_move(move, self.MIN_PLAYER)
                score = max_value(new_board, alpha, beta)
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Alpha cut-off
            return best_score

        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        for move in self.board.get_possible_moves():
            new_board = self.board.make_move(move, self.MAX_PLAYER)
            score = min_value(new_board, alpha, beta)
            if score > alpha:
                alpha = score
                best_move = move
        return best_move
