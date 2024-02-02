""" routes/ai/bestMove.py

Function Description:
This function handles the best move of the min-max of alpha-beta,
fetching the board status and the algorithm used ( min-max / alpha-beta) and return the best move that computer have to play

Dependencies:
- Flask: Micro web framework for Python.
- util.generate_response: Module for generating standardized response messages.

Usage:
1. Ensure that the board get from the request is the type (table with 9 cases with values 1, -1, 0 )  e.g: [1,0,-1, 0,0,1, -1,0,1].
2. Ensure that the request get the algorithm type min-max or alpha-beta ( boolean True for min-max and False for alpha-beta)
3. import the function best move created to calculate the position of the best move and return it index
4. return this response at the data response

"""
from flask import Blueprint, request
from util.generate_response import response_ok, response_bad_request, response_not_found
from algorithm.bestMove.heuristic import calculate_best_move_heuristic
from util.transform_board import convert_to_linear_index as index
est_move_heuristic_blueprint = Blueprint('heuristic', __name__)

@est_move_heuristic_blueprint.route("/ai/heuristic", methods=["POST"])
def get_best_move():
    data = request.json
    algorithm = data.get("algorithm", True)

    # Ensure that the required data is present in the request
    if "board" not in data:
        return response_bad_request("Missing required data")

    board = data["board"]
    spend_time = data.get("time", False)

    # Validate the spend_time type
    if not isinstance(spend_time, bool):
        return response_bad_request("Invalid algorithm type")

    # Calculate the best move
    best_move = calculate_best_move_heuristic(board, algorithm, spend_time)
    if(best_move == None):
        return response_not_found("Game finished")
    if(str(best_move) == best_move):
        return response_bad_request(best_move)
    print(f"best_move_index {best_move} ")
    best_move_index = index(best_move["best_move"][0], best_move["best_move"][1], board)
    # Return the best move as the response
    return response_ok("Computer best move", {"best_move": best_move_index, "spend_time": best_move["spend_time"]/1000} if spend_time else {"best_move": best_move_index})
