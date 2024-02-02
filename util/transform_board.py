""" /util/transform_board.py
Transforms a flat array representation of the board into a nD array.

Args:
    board_data (list): A flat array representing the board.

Returns:
    list: A nD array representing the board.

Raises:
    ValueError: If the length of board_data does not represent a square board.
"""

def transform_flat_to_nd(board_data):

    # Calculate the dimension of the square board
    n = int(len(board_data) ** 0.5)

    # Check if the length of the board data represents a square board
    if n * n != len(board_data):
        return "Board data length does not represent a square board."

    # Convert the flat array representation to a nD array
    return [board_data[i:i+n] for i in range(0, len(board_data), n)]

"""
Convert row and column indices to a linear index in a flattened representation of the board.

Args:
    row (int): Row index.
    col (int): Column index.
    num_cols (int): Number of columns in the board.

Returns:
    int: Linear index.
"""
def convert_to_linear_index(row, col, board_data):
    num_cols = int(len(board_data) ** 0.5)

    return row * num_cols + col