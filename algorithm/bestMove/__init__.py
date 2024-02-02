import time

from .minMax import MinMaxAlgorithm
from .alphaBeta import AlphaBetaAlgorithm
from util.transform_board import transform_flat_to_nd as transform
from algorithm.model.Board import Board
from util.generate_response import response_bad_request as badRequest

def calculate_best_move(board, algorithm, spend_time):
    """
    Calculates the best move based on the specified algorithm.

    Args:
        board (list): The current state of the game board.
        algorithm (bool): True for Minimax algorithm, False for Alpha-Beta Pruning algorithm.

    Returns:
        tuple or str: The best move coordinates (row, col) if available, or an error message if the input is invalid.
    """
    new_board = transform(board)

    if str(new_board) == new_board:
        return new_board

    new_board = Board(new_board)

    start_time = time.time()

    if algorithm:
        # Use Minimax algorithm
        min_max_algo = MinMaxAlgorithm(new_board)
        best_move = min_max_algo.min_max_best_move()
    else:
        # Use Alpha-Beta Pruning algorithm
        alpha_beta_algo = AlphaBetaAlgorithm(new_board)
        best_move = alpha_beta_algo.alpha_beta_best_move()

    end_time = time.time()
    spend_time = end_time - start_time

    return (best_move, spend_time) if spend_time else (best_move, 0)

