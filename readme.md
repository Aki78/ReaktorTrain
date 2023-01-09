# Drone Monitoring App

This app is designed to monitor and track drones in a 500 by 500 meter square, and provide information about pilots who have recently violated the no-fly zone (NDZ). The no-fly zone is a circle with a 100 meter radius, centered at position (250, 250) meters.

### The app retrieves data about drone positions and pilot information from two endpoints:

    assignments.reaktor.com/birdnest/drones provides snapshot data about drones in the area in XML format. This data is updated about once every 2 seconds.
    assignments.reaktor.com/birdnest/pilots/:serialNumber provides information about a drone's registered owner in JSON format, based on the given serial number.

The app persists pilot information for 10 minutes after their drone was last seen by the monitoring equipment, and displays the closest confirmed distance to the nest. The app also displays the pilot's name, email address, and phone number. When the app is opened, it immediately shows the pilot information from the past 10 minutes. No manual refresh is required to see up-to-date information.
Technologies

This app was built using:

    Python and the Flask web framework
    Requests for making HTTP requests
    xmltodict for parsing XML data
    React
    MySQL

## Usage

To run this app, follow these steps:

    Install the necessary dependencies by running pip install -r requirements.txt.
    Run python app.py to start the server.

Note: This app will automatically fetch and store data about pilots who violate the NDZ at regular intervals. The interval is set in the POOL_TIME constant in the config.py file.


The endpoints in flask are:

    fetch_recent_naughty_pilots: This endpoint allows users to retrieve a list of pilots who have violated regulations in the past 10 minutes.
    insert_recent_naughty_pilots: This function stores information about pilots who have violated regulations in a MySQL database.


Check out the app at [http://aki78.pythonanywhere.com/bird](http://aki78.pythonanywhere.com/bird).

Note: This webapp will automatically fetch and store data about pilots who violate regulations at regular intervals (the interval is set in the POOL_TIME constant in the config.py file).
