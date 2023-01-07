from flask import Flask, jsonify, request
import mysql.connector
import datetime
import requests
import time
import xmltodict
import threading
from hashlib import sha256
import Python.utils as utils

#TODO
#get logic working
#Optimize memory and speed

#Globals
USR = "root"
PSW = "root"
HST = "localhost"
DB = "naughty"
BASE_URL = 'http://assignments.reaktor.com/birdnest/drones'
BASE_PILOT_URL = "http://assignments.reaktor.com/birdnest/pilots/"
table_name = "naughty_pilots"

sha_old = ""
POOL_TIME = 1 # make sure to have smaller than 2 seconds for realtime update
all_naughty_pilots = []

app = Flask(__name__)

# def interrupt():
#     global yourThread
#     yourThread.cancel()

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

# @app.route('/insert_naughty_pilots', methods=['POST'])
def insert_recent_naughty_pilots(data):

    cnx = mysql.connector.connect(user=USR, password=PSW, host=HST, database=DB)
    cursor = cnx.cursor()
    try:
        print("Adding", data)

        # data = request.get_json()
        for i in data:
            print("i", i)
            pilot_id = i['pilot_id']
            first_name = i['firstName']
            last_name = i['lastName']
            phone_number = i['phoneNumber']
            timestamp = i['timestamp']
            email = i['email']
            distance = i['distance']
            X = i['X']
            Y = i['Y']
            print(i)

            # Insert the data into the table
            insert_query = '''
            INSERT INTO {} (pilotID, firstName, lastName, phoneNumber, email, distance,  X, Y, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)
            '''.format(table_name)
            try:
                print(insert_query)
                cursor.execute(insert_query, (pilot_id, first_name, last_name, phone_number,  email, distance,X,Y, timestamp))
                cnx.commit()
            except mysql.connector.Error as error:
                print(error)
        cnx.close()

        # Return a success message
        return jsonify({'message': 'Pilot added successfully'})

    except mysql.connector.Error as err:
        print("Not adding: ", err)
        return jsonify({'status': 'error', 'message': str(err)})


def fetch_drone_data():
    app.app_context().push()
    global all_naughty_pilots
    while True:
        print("calld! ")

        # Parse the XML data
        xml_data = requests.get(BASE_URL).text

        # checking if it is the same or not from before so there aren't unnessesary calls
        # only reason for sha is for humans to be able to quickly see changes at print time
        global sha_old
        sha_value = sha256(xml_data.encode('utf-8')).hexdigest()
        print(sha_old)
        if sha_value != sha_old:
            sha_old = sha_value

            #Getting full_data from measure
            full_data = xmltodict.parse(xml_data)
            incoming_drones_list =  full_data["report"]["capture"]["drone"]
            timestamp =  full_data["report"]["capture"]["@snapshotTimestamp"]
            timestamp = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            print(timestamp)

            #small sanity check to make sure drones are stored in list
            if type(incoming_drones_list) != list:
                raise Exception(TypeError)

            # pos is int because there is no point storing data in micrometers or nanometers
            temp_all_naughty_pilots = []
            for i in  incoming_drones_list:
                x =  int(float(i["positionX"]))
                y =  int(float(i["positionY"]))
                distance = utils.get_distance_in_meters(x, y)
                if utils.is_in_bad_zone(x,y):
                    naughty_pilot_url = BASE_PILOT_URL  + i["serialNumber"]
                    naughty_pilot = requests.get(naughty_pilot_url).json()
                    # timestamp = datetime.datetime.now() 
                    temp_all_naughty_pilots.append({"pilot_id":naughty_pilot["pilotId"], "firstName":naughty_pilot["firstName"], "lastName":naughty_pilot["lastName"], "phoneNumber":naughty_pilot["phoneNumber"], "email":naughty_pilot["email"], "distance": distance, "X":x, "Y":y, "timestamp":timestamp })
            insert_recent_naughty_pilots(temp_all_naughty_pilots)
            all_naughty_pilots += temp_all_naughty_pilots
            print(all_naughty_pilots)
            time.sleep(POOL_TIME)


if __name__ == '__main__':
    global yourThread

    yourThread = threading.Thread(target=fetch_drone_data)
    yourThread.start()  
    app.run(port=12345)
