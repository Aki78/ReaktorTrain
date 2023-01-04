import requests
import time
import xmltodict
from hashlib import sha256
import json
# print(test["report"]["deviceInformation"])
sha_old = ""
while True:
    # Parse the XML data
    xml_data = requests.get('http://assignments.reaktor.com/birdnest/drones').text
    sha_value = sha256(xml_data.encode('utf-8')).hexdigest()
    # Checking if it is the same or not from before
    if sha_value != sha_old:
        sha_old = sha_value
        test = xmltodict.parse(xml_data)
        incoming_drones =  test["report"]["capture"]["drone"]
        if type(incoming_drones) != list:
            raise Exception(TypeError)
        drone_data = []
        # position int because there is no point storing data in micrometers or nanometers
        for i in  incoming_drones:
            x =  int(float(i["positionX"]))
            y =  int(float(i["positionY"]))
            pilot_url = "http://assignments.reaktor.com/birdnest/pilots/" + i["serialNumber"]
            pilot = requests.get(pilot_url).json()
            drone_data.append({"id":pilot["pilotId"],"number":i["serialNumber"], "pos":(x,y)})
        print(drone_data)
        time.sleep(1)
