from flask import Flask, jsonify
import mysql.connector
import datetime
import requests
import time
import xmltodict
import threading
from hashlib import sha256
import utils as utils

import config

#Global Constants
USR = config.USER
PSW = config.PASSWORD 
HST = config.HOST 
DB = config.DB 
BASE_URL = config.BASE_URL
BASE_PILOT_URL = config.BASE_PILOT_URL
PILOT_TABLE_NAME = config.PILOT_TABLE_NAME 
VIOLATION_TABLE_NAME = config.VIOLATION_TABLE_NAME 
POOL_TIME = config.POOL_TIME 

#Global Variables
sha_old = ""
past_10_min_pilots = []

app = Flask(__name__)

@app.route('/fetch_recent_naughty_pilots', methods=['GET'])
def fetch_recent_naughty_pilots():
    print("CALLED")
    resp = jsonify(past_10_min_pilots)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def insert_recent_naughty_pilots(data):

    cnx = mysql.connector.connect(user=USR, password=PSW, host=HST, database=DB)
    cursor = cnx.cursor()
    query = '''SELECT * FROM naughty_pilot_info WHERE pilotID = %s'''
    #dummy value just to check if pilot already exists
    values = ('12345',)
    cursor.execute(query, values)

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

            # Insert pilot data into the table if it doesn't exist
            if cursor.fetchone() is None:
                # Insert a row into the table
                insert_pilot_info = '''
                INSERT INTO {} (pilotID, firstName, lastName, phoneNumber, email)
                VALUES (%s, %s, %s, %s, %s)'''.format(PILOT_TABLE_NAME)

                try:
                    # cursor.execute(insert_query, (pilot_id, first_name, last_name, phone_number,  email, distance,X,Y, timestamp))
                    cursor.execute(insert_pilot_info, (pilot_id, first_name, last_name, phone_number,  email))
                    cnx.commit()
                except mysql.connector.Error as error:
                    print(error)
            else:
                print('PilotID already exists in the table')


            insert_violation_info = '''
                INSERT INTO {} (pilotID, distance, X, Y, timestamp)
                VALUES (%s, %s, %s, %s, %s)'''.format(VIOLATION_TABLE_NAME)
            try:
                cursor.execute(insert_violation_info, (pilot_id, distance, X, Y,  timestamp))
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
    global past_10_min_pilots
    while True:
        past_10_min_pilots = utils.remove_old_objects(past_10_min_pilots)
        print("calld! ")

        # Parse the XML data
        try:
            xml_data = requests.get(BASE_URL).text
        except:
            print("xml_data broken")
            continue

        # checking if it is the same or not from before so there aren't unnessesary calls
        # only reason for sha is for humans to be able to quickly see changes at print time
        global sha_old
        sha_value = sha256(xml_data.encode('utf-8')).hexdigest()
        print(sha_old)
        if sha_value != sha_old:
            sha_old = sha_value

            #Getting full_data from measure
            try:
                full_data = xmltodict.parse(xml_data)
            except:
                print("xml_data_broken")
                continue
            incoming_drones_list =  full_data["report"]["capture"]["drone"]
            timestamp =  full_data["report"]["capture"]["@snapshotTimestamp"]
            timestamp = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
            print(timestamp)

            #small sanity check to make sure drones are stored in list
            if type(incoming_drones_list) != list:
                raise Exception(TypeError)

            past_10_min_pilots += get_temp_naughty_pilots(incoming_drones_list, timestamp)
            print(past_10_min_pilots)
            time.sleep(POOL_TIME)

def get_temp_naughty_pilots(drone_list, timestamp):
    temp_naughty_pilots = []
    for i in  drone_list:
        # pos is int because there is no point storing data in micrometers or nanometers
        x =  int(float(i["positionX"]))
        y =  int(float(i["positionY"]))
        distance = utils.get_distance_in_meters(x, y)
        if utils.is_in_bad_zone(x,y):
            naughty_pilot_url = BASE_PILOT_URL  + i["serialNumber"]

            try:
                naughty_pilot = requests.get(naughty_pilot_url).json()
                print("request_get pilot_url failed.")
                if check_if_pilot_already_exists(naughty_pilot["pilotId"], temp_naughty_pilots):
                    temp_naughty_pilots.append({"pilot_id":naughty_pilot["pilotId"],
                                                "firstName":naughty_pilot["firstName"],
                                                "lastName":naughty_pilot["lastName"],
                                                "phoneNumber":naughty_pilot["phoneNumber"],
                                                "email":naughty_pilot["email"],
                                                "distance": distance, "X":x, "Y":y, "timestamp":timestamp
                                                })
            except:
                print("pilot doesn't exist")

    #Adding to database
    insert_recent_naughty_pilots(temp_naughty_pilots)
    return temp_naughty_pilots


def check_if_pilot_already_exists(new_pilot_id, pilots):
    for i in pilots:
        try:
            if new_pilot_id == i["pilotId"]:
                return False
        except:
            print("Couldn't find Pilot")
            return False
    return True


def replace_pilot_closer_than_before(new_pilot, pilots):
    for i in range(len(pilots)):
       if new_pilot["pilotId"] == pilots[i]["pilotId"]:
           if new_pilot["distance"] < pilots[i]["distance"]:
               pilots[i] = new_pilot

if __name__ == '__main__':
    global yourThread

    yourThread = threading.Thread(target=fetch_drone_data)
    yourThread.start()  

    app.run(port=12345)
