class Board:
    """
    Represents the game board for a Tic-Tac-Toe game.

    Attributes:
        matrix (list): A 2D list representing the game board.
    """

    EMPTY = 0
    MAX_PLAYER = 1
    MIN_PLAYER = -1
    def __init__(self, matrix):
        """
        Initializes the Board with the given matrix.

        Args:
            matrix (list): A 2D list representing the initial state of the game board.
        """
        self.matrix = matrix

    def is_game_over(self):
        """
        Checks if the game is over (i.e., if any player has won or if the board is full).

        Returns:
            bool: True if the game is over, False otherwise.
        """
        if self.check_winner(self.MAX_PLAYER) or self.check_winner(self.MIN_PLAYER) or not self.get_possible_moves():
            return True
        else:
            return False

    def check_winner(self, player):
        """
        Checks if the specified player has won the game.

        Args:
            player (int): The player for whom to check for a winning condition (MAX_PLAYER or MIN_PLAYER).

        Returns:
            bool: True if the specified player has won, False otherwise.
        """
        n = len(self.matrix)  # Assuming the matrix is square (n x n)

        # Check rows and columns
        for i in range(n):
            row_win = all(self.matrix[i][j] == player for j in range(n))
            col_win = all(self.matrix[j][i] == player for j in range(n))
            if row_win or col_win:
                return True

        # Check main diagonal
        main_diag_win = all(self.matrix[i][i] == player for i in range(n))
        if main_diag_win:
            return True

        # Check anti-diagonal
        anti_diag_win = all(self.matrix[i][n - 1 - i] == player for i in range(n))
        if anti_diag_win:
            return True

        return False

    def utility(self):
        """
        Calculates the utility value of the current board state.

        Returns:
            int: The utility value indicating the outcome of the game
                 (1 for MAX_PLAYER win, -1 for MIN_PLAYER win, 0 for draw or ongoing game).
        """
        if self.check_winner(self.MAX_PLAYER):
            return 1  # Max player wins
        elif self.check_winner(self.MIN_PLAYER):
            return -1  # Min player wins
        else:
            return 0  # Draw or game still ongoing

    def get_possible_moves(self):
        """
        Retrieves a list of possible moves on the board.

        Returns:
            list: A list of tuples representing the coordinates (row, col) of empty cells on the board.
        """
        possible_moves = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == self.EMPTY:
                    possible_moves.append((i, j))
        return possible_moves

    def make_move(self, move, player):
        """
        Makes a move on the board for the specified player.

        Args:
            move (tuple): The coordinates (row, col) where the move is to be made.
            player (int): The player making the move (MAX_PLAYER or MIN_PLAYER).

        Returns:
            Board: A new Board instance representing the updated state of the game board.
        """
        new_board = [row[:] for row in self.matrix]  # Create a deep copy of the board
        new_board[move[0]][move[1]] = player
        return Board(new_board)
