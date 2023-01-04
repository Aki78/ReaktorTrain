import requests
import math
import time
import xmltodict
from hashlib import sha256

#TODO#
#Refactor Drones to Classes
#Set Up Endpoints
#Dev Front End

def is_in_bad_zone(x,y):
    return math.sqrt((x - center_point)**2+(y - center_point)**2 ) < zone_range

#Globals
sha_old = ""
center_point = 250000 # In mm, both X_0 and Y_0 being the same
zone_range = 100000 # In mm
sleep_time = 1 # make sure to have smaller than 2 seconds for realtime update

while True:

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
        print(all_naughty_pilots)
        #timer to make sure it doesn't run too many requests per second
        time.sleep(sleep_time) 


