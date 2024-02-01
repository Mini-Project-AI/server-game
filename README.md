# server-game
the server side of the game implementation of the game that is relied between the web status and the model deployed in python

## File Structure

Below is the file structure of the project:

```
server_Flask_min-max/
│
│
├── routes
│ ├── init.py
│ ├── health.py
│ ├── login.py
│ ├── register.py
│ └── init.py
├── algorithm
├── config
│ └── connect.py
├── util
│ ├── generate_response.py
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


### Description of Key Files and Directories

- `/routes`: This directory contains modular routing configurations.
  - `__init__.py`: Allows Python to recognize the directory as a package.
  - `health.py`: Handles routes related to the health status of the server.
  - `login.py`: Manages routes for user login functionality.
  - `register.py`: Handles routes for user registration.

- `/algorithm`: Contains the core algorithms used in the project.

- `/config`: Stores configuration files and scripts.
  - `connect.py`: Manages the connection to the MongoDB database.

- `/util`: Includes utility scripts and helper functions.
  - `generate_response.py`: Provides functions for generating standardized responses.
  - `validation_inputs.py`: Contains functions for input validation.

- `/test`: Contains test files for the application.
  - `post-man_collection.json`: Postman collection for API testing.

- `server.py`: The main entry point for the Flask application.

- `requirements.txt`: Lists all the dependencies required by the project.

- `.gitignore`: Specifies intentionally untracked files to ignore.

- `render.yaml`: configuration settings or instructions related to deploying Flask application after each new PR accepted

- `README.md`: Provides an overview and documentation for the project.