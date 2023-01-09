# Webapp

This webapp is a tool for tracking and storing information about pilots who violate regulations while operating drones.
Features

    fetch_recent_naughty_pilots: This endpoint allows users to retrieve a list of pilots who have violated regulations in the past 10 minutes.
    insert_recent_naughty_pilots: This function stores information about pilots who have violated regulations in a MySQL database.

## Technologies

This webapp was built using:

    Python and the Flask web framework
    MySQL for storing data
    Requests for making HTTP requests
    xmltodict for parsing XML data
    Threading for fetching data at regular intervals

## Usage

### To run this webapp, follow these steps:

    Install the necessary dependencies by running pip install -r requirements.txt.
    Set up a MySQL database and update the config.py file with the necessary information (username, password, host, and database name).
    Run python app.py to start the server.

Note: This webapp will automatically fetch and store data about pilots who violate regulations at regular intervals (the interval is set in the POOL_TIME constant in the config.py file).
