AndroLab Back-end Server README
==========

This project is the Python3 backend server for the Android InsecureBankv2 application which can be found at https://github.com/dineshshetty/Android-InsecureBankv2


This is an insecure bank application implemented in Python3. It consists of four main files:

1. `database.py`: This file contains the database setup code using SQLAlchemy to establish a connection to the SQLite database.

2. `models.py`: This file defines the data models for the users and accounts using SQLAlchemy's declarative base.

3. `app.py`: This is the main application file that contains the Flask web server implementation for the bank application. It provides various routes for user authentication, account management, and transactions.
4. `mydb.db`: This is the sample SQLite 3.X database with the two default accounts- dinesh and jack, to initialize the server database.

## Installation and Setup

To run the Insecure Bank Application on your Ubuntu, Debian, Windows, or MacOS system, follow these steps:

### Prerequisites

- Python 3.x should be installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

### Clone the Repository

1. Open a terminal or command prompt.

2. Clone the repository using the following command:
	```
	git clone <repository_url>
	```

3. Navigate to the project directory:
	```
	cd insecure-bank-application
	```


### Install Dependencies

1. Create a virtual environment (optional but recommended):
	```
	python3 -m venv venv
	```

2. Activate the virtual environment:
- For Ubuntu, Debian, or MacOS:
  ```
  source venv/bin/activate
  ```
- For Windows:
  ```
  venv\Scripts\activate
  ```

3. Install the required packages using `pip`:
	```
	pip3 install -r requirements.txt
	```


### Database Setup

1. Initialize the database by running the following command:
	```
	python3 database.py
	```


### Start the Application

1. Run the application using the following command:
	```
	python3 app.py --help
	python3 app.py
	```


2. The Flask web server will start running and listening on `http://localhost:8888` by default.

## Usage

You can access the Insecure Bank Application by opening a web browser and navigating to `http://localhost:8888`. The application provides various routes for user authentication, account management, and transactions. Refer to the source code comments for detailed information on the available routes and their functionality.

**Note: This application is for educational purposes only and should not be used in a production environment. It is intentionally insecure and does not implement proper security measures. Use it at your own risk.**

## TO-DO
1. Configure logging of server HTTP responses

2. Use requirements.txt file to install Python packages in Dockerfile