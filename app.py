from flask import Flask, jsonify, request
import mysql.connector
import datetime
import requests
import time
import xmltodict
import threading
import atexit
from hashlib import sha256

#TODO
#Optimize memory and speed

#Globals
USR = ""
PSW = ""
HST = ""
DB = ""

sha_old = ""
POOL_TIME = 1 # make sure to have smaller than 2 seconds for realtime update

app = Flask(__name__)

def interrupt():
    global yourThread
    yourThread.cancel()

@app.route('/fetch_recent_naughty_pilots')
def fetch_recent_naughty_pilots():
    try:
        cnx = mysql.connector.connect(user=USR, password=PSW, host=HST, database=DB)
        cursor = cnx.cursor()
        ten_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
        query = 'SELECT * FROM data_table WHERE timestamp > %s'
        cursor.execute(query, (ten_minutes_ago,))
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        return jsonify(err)

@app.route('/insert_naughty_pilots', methods=['POST'])
def insert_recent_naughty_pilots():
    try:
        cnx = mysql.connector.connect(user=USR, password=PSW, host=HST, database=DB)
        cursor = cnx.cursor()
        data = request.json

        data = request.get_json()
        first_name = data['firstName']
        last_name = data['lastName']
        phone_number = data['phoneNumber']
        create_dt = data['createDt']
        email = data['email']
        datetime = data['datetime']

        # Insert the data into the table
        insert_query = '''
        INSERT INTO {} (firstName, lastName, phoneNumber, createDt, email, datetime)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''.format(table_name)
        cursor.execute(insert_query, (first_name, last_name, phone_number, create_dt, email, datetime))
        cnx.commit()

        # Return a success message
        return jsonify({'message': 'Pilot added successfully'})

    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)})


def fetch_drone_data():

    # Parse the XML data
    xml_data = requests.get('http://assignments.reaktor.com/birdnest/drones').text

    # checking if it is the same or not from before so there aren't unnessesary calls
    # only reason for sha is for humans to be able to quickly see changes at print time
    sha_value = sha256(xml_data.encode('utf-8')).hexdigest()
    if sha_value != sha_old:
        sha_old = sha_value

        #Getting full_data from measure
        full_data = xmltodict.parse(xml_data)
        incoming_drones_list =  full_data["report"]["capture"]["drone"]

        #small sanity check to make sure drones are stored in list
        if type(incoming_drones_list) != list:
            raise Exception(TypeError)

        # pos is int because there is no point storing data in micrometers or nanometers
        all_naughty_pilots = []
        for i in  incoming_drones_list:
            x =  int(float(i["positionX"]))
            y =  int(float(i["positionY"]))
            if is_in_bad_zone(x,y):
                naughty_pilot_url = "http://assignments.reaktor.com/birdnest/pilots/" + i["serialNumber"]
                naughty_pilot = requests.get(naughty_pilot_url).json()
                all_naughty_pilots.append({"id":naughty_pilot["pilotId"], "number":i["serialNumber"], "pos":(x,y)})


if __name__ == '__main__':
    yourThread = threading.Timer(POOL_TIME, fetch_drone_data, ())
    yourThread.start()  
    app.run()
