# server-game
the server side of the game implementation of the game that is relied between the web status and the model deployed in python

## File Structure

Below is the file structure of the project:

```
server_Flask_min-max/
│
│
├── routes
│ ├── ai
│ | └── bestMove.py
│ ├── __init__.py
│ ├── health.py
│ ├── login.py
│ ├── register.py
│ └── init.py
├── algorithm
│ ├── bestMove
│ | ├── __init__.py
│ | ├── alphaBeta.py
│ | └── minMax.py
│ └── model
│   └── Board.py
├── config
│ └── connect.py
├── util
│ ├── generate_response.py
│ ├── transform_board.py
│ └── validation_inputs.py
├── test
│ └── post-man_collection.json
│
├── server.py
├── requirements.txt
├── .gitignore
├── render.yaml
└── README.md
```


## Description of Key Files and Directories

- `/routes`: This directory contains modular routing configurations.
  - `ai/`: Subdirectory containing AI-related routes.
    - `bestMove.py`: Handles routes related to calculating the best move.
  - `__init__.py`: Initialization file to recognize the directory as a package.
  - `health.py`: Manages routes related to the health status of the server.
  - `login.py`: Handles routes for user login functionality.
  - `register.py`: Manages routes for user registration.

- `/algorithm`: Contains the core algorithms used in the project.
  - `bestMove/`: Subdirectory containing algorithm-related files.
    - `__init__.py`: Initialization file for the algorithm package.
    - `alphaBeta.py`: Implementation of the Alpha-Beta Pruning algorithm.
    - `minMax.py`: Implementation of the Minimax algorithm.
  - `model/`: Subdirectory containing the model-related files.
    - `Board.py`: Defines the Board class used in the algorithms.

- `/config`: Stores configuration files and scripts.
  - `connect.py`: Manages the connection to the MongoDB database.

- `/util`: Includes utility scripts and helper functions.
  - `generate_response.py`: Provides functions for generating standardized responses.
  - `transform_board.py`: Contains functions for transforming the game board.
  - `validation_inputs.py`: Includes functions for input validation.

- `/test`: Contains test files for the application.
  - `post-man_collection.json`: Postman collection for API testing.

- `server.py`: The main entry point for the Flask application.

- `requirements.txt`: Lists all the dependencies required by the project.

- `.gitignore`: Specifies intentionally untracked files to ignore.

- `render.yaml`: Configuration settings or instructions related to deploying the Flask application after each new PR accepted.

## Usage

To run the server, execute the `server.py` file. Make sure to install the required dependencies listed in `requirements.txt`.

## Testing

The `/test` directory contains test files, including a Postman collection (`post-man_collection.json`), for testing the APIs and functionalities.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
