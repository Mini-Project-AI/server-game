# server-game
the server side of the game implementation of the game that is relied between the web status and the model deployed in python

## File Structure

Below is the file structure of the project:

│
├── routes
│ ├── init.py
│ └── /health
│ └── init.py
├── algorithm
├── config
├── util
├── test
│ └── post-man_collection.json
│
├── server.py
├── requirements.txt
├── .gitignore
└── README.md

### Description of Key Files and Directories

- `/routes`: This directory contains modular routing configurations.
  - `__init__.py`: Allows Python to recognize the directory as a package.
  - `/health`: Submodule for health-related routes.

- `/algorithm`: Contains the core algorithms used in the project.

- `/config`: Stores configuration files and scripts.

- `/util`: Includes utility scripts and helper functions.

- `/test`: Contains test files for the application.
  - `post-man_collection.json`: Postman collection for API testing.

- `server.py`: The main entry point for the Flask application.

- `requirements.txt`: Lists all the dependencies required by the project.

- `.gitignore`: Specifies intentionally untracked files to ignore.

- `README.md`: Provides an overview and documentation for the project.